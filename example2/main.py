import os                                                                       
from multiprocessing import Pool                                        

processes = ('p1.py', 'p2.py', 'p3.py')                                    
def run_process(process):                                                
    os.system('python3 {}'.format(process))        

pool = Pool(processes=3)                                             
pool.map(run_process, processes)     

