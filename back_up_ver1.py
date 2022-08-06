import os
import time
# here are the files and dictionaries
source = ['/Users/mikastarspc/Desktop/python_programs/py_t_1/notes']
# here is the backup
target_dir = '/Users/mikastarspc/Desktop/python_programs/py_t_1/backup'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# all the program is stored as .zip files
# os.sep can automatically change between / and \\ in different systems(macOS and Windows or Linux)
# time.strftime() can get the time of the system now
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
print('zip command is')
print(zip_command)
print('Running')
if os.system(zip_command) == 0:
    print('successful backup tp ', target)
else:
    print('FAIL!')
