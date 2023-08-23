# This program will run both the action program and the timer
import os      
from multiprocessing import Pool
import random

#Generating list
l = []
print(int(round(random.random(), 6)*1000))
for i in range(0, 100000):
    l.append(int((round(random.random(),6)*1000000)))

    if i == int(round(random.random(), 6)*100000):
        print("Item Number: " + str(i) + "Is the number to find") 
        l.append("222222")
        print("Add!!")

#print(l)

with open("list.txt", "w") as list:
    for i in l: 
        list.write(str(i) + "\n")



"""
processes = ('h1.py', 'h2.py')                                    
def run_process(process):                                                
    os.system('python3 {}'.format(process))        

pool = Pool(processes=3)                                             
pool.map(run_process, processes)     

print("Back to main Program!!")
"""
