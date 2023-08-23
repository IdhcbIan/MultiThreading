# This program will run both the action program and the timer
import os      
from multiprocessing import Pool

processes = ('h1.py', 'h2.py', 'timer.py')                                    
def run_process(process):                                                
    os.system('python3 {}'.format(process))        

pool = Pool(processes=3)                                             
pool.map(run_process, processes)     

print("Back to main Program!!")




