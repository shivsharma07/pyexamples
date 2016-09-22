import os
import time

source = ['E:\\test2','E:\\test']
target_dir = 'E:\\Backup'
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
if not os.path.exists(today):
    os.mkdir(today)
    print('Today succefully created.',today)

target = today + os.sep + now +'.zip'
#target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S')+'.zip'
zip_command = "zip -r {0} {1}".format(target,' '.join(source))

print(zip_command)
if os.system(zip_command) == 0:
    print("Successfully backup to : ", target)
else:
    print("Backup FAILED")


