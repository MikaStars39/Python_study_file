import os
import time
source = ['/Users/mikastarspc/Desktop/python_programs/py_t_1/notes']
target_dir = '/Users/mikastarspc/Desktop/python_programs/py_t_1/backup'
# all the same with ver.1
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
comment = input('please enter a comment --->')
if len(comment) == 0:
    target = target_dir + os.sep + time.strftime('%Y%m%d')
else:
    target = target_dir + os.sep + time.strftime('%Y%m%d') + '_' + \
        comment.replace(' ', '_') + '.zip'
if not os.path.exists(today):
    os.mkdir(today)
    print('successfully create dictionary:', today)
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
if os.system(zip_command) == 0:
    print('successfully backup', target)
else:
    print('backup FAILED')
