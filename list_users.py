import re
import sys
import os
import pwd
import json

def count_device(result_file, result_json):
    if not os.path.exists(result_file):
        return
    with open(result_file) as result:
        lines = result.readlines()
        if len(lines) < 10:
            print('error result')
            sys.exit()
    
        for i,line in enumerate(lines):
            if 'Processes:' in line:
                break
        if i == 0:
            print('error result')
            sys.exit()
        start = i + 3
        processes = lines[start:-1]
        occupy = {}
        user_number = {}
        if len(processes) == 1 and processes[0].find('No running processes found') != -1:
            print('All GPU are idle!')
            return
        for p in processes: 
            m = re.split('\s+',p)
            gpu = m[1]
            pid = m[2]
            proc_stat_file = os.stat("/proc/%d" % int(pid))
            uid = proc_stat_file.st_uid
            username = pwd.getpwuid(uid)[0]
            if gpu not in occupy:
                occupy[gpu] = []
            occupy[gpu].append(username)
            if username not in user_number:
                user_number[username] = 0
            user_number[username] += 1
        result = {}
        result['occupy'] = occupy
        result['user_count'] = user_number
        with open(result_json, 'w') as fp:
            json.dump(result, fp)


if __name__ == '__main__':
    count_device(sys.argv[1], sys.argv[2])
