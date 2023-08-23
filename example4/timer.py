import os
import time
import psutil
import subprocess

def check_and_kill():
    status1 = subprocess.run(['pgrep', '-f', 'h1.py'], capture_output=True, text=True) 
    out1 = status1.returncode
    status2 = subprocess.run(['pgrep', '-f', 'h2.py'], capture_output=True, text=True) 
    out2 = status2.returncode
    out = out1 + out2

    if out == 0:
        done = True
    else:
        done = False
    return done
done = True


print('------// Watching!! //---------')
while done == True:
   done = check_and_kill()
   time.sleep(0.1)

if check_and_kill() == False:
    os.system("pkill -f h1.py")
    os.system("pkill -f h2.py")

