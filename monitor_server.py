from flask import Flask
from flask import Blueprint
from pkgutil import extend_path
from list_users import count_device
import os
import json
from result_wrapper import *

xlearn_view = Blueprint('',__name__,)

@xlearn_view.route('/gpu', methods=['GET'])
def count_gpu():
    print('begin to count...')
    os.system('sh count.sh')
    print('finish collecting records.')
    occupy = {}
    user_number = {}
    for i in range(101,112):
        if i != 107:
            result_file = 'result_%s.json' % i
            if not os.path.exists(result_file):
                occupy[i], user_number[i] = {}, {}
            else:
                with open(result_file) as f:
                    result = json.load(f)
                    occupy[i], user_number[i] = result['occupy'], result['user_count']
            print('finish counting %s.' % i)
    print('All counting DONE!')
    result = {}
    result['occupy'] = occupy
    result['user_number'] = user_number
    print(occupy)
    print(user_number)
    return JSONWrapper.success(result)

# start the service    
def create_app():
    app = Flask(__name__)
    return app

if __name__ == '__main__':
    app = create_app()
    app.register_blueprint(xlearn_view)
    app.run(host='0.0.0.0', port=8080, debug=True)
