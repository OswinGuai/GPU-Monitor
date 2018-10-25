import re
import sys
import os
import pwd

result_file = sys.argv[1]
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

    print('GPU is being used by:')
    print(occupy)
    print('User Occupations:')
    print(user_number)

