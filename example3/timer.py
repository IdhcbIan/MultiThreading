import os
import time
import psutil
import subprocess

def check_and_kill():
    status = subprocess.run(['pgrep', '-f', 'action.py'], capture_output=True, text=True) 
    out = status.returncode
    if out != 0:
        done = True
    else:
        done = False
    return done

print('------// Max time: 10s //---------')
for i in range(1, 11):
    print(i)
    if check_and_kill() == True:
        break
    time.sleep(1)

if check_and_kill() == False:
    os.system("pkill -f action.py")

