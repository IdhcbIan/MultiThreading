import time
import random

rnumber = random.random()
print(rnumber)

if rnumber > 0.5:
    print("Action Decided to execute")
elif rnumber < 0.5:
    print("Action Decided not to execute")
    time.sleep(100)



