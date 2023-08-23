╱╱╱╱╱╱╱╭╮╭┳╮╭╮╱╱╱╱╱╱╱╱╭┳╮
╭━━┳┳┳╮┃╰╋┫╰┫╰┳┳┳━┳━╮╭╯┣╋━┳┳━╮
┃┃┃┃┃┃╰┫╭┫┃╭┫┃┃╭┫┻┫╋╰┫╋┃┃┃┃┃╋┃
╰┻┻┻━┻━┻━┻┻━┻┻┻╯╰━┻━━┻━┻┻┻━╋╮┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯
--------------------------------

-----// Main //-------------

-> This is a tutorial on Multithreading in python!!

-> What is Multithreading
  Multithreading is a way to do things simultaniusly in python
this has many uses, and allows more complex problems to arise
from complex program arquitecture.

--------------------------------

-> Modules
  Multithreading can be achieved with two modules, but only
one can be simultanious
 + Modules:
  - time
  -  
--------------------------------

-> Process
  A process is a live set of intructions running on your 
you can run something like btop on your terminal to see witch 
processes are running on your terminal.

  When you run a python file, "$ python3 stall.py" this will 
create a process in your computer

+ Remember:
  - Use "$ pgrep [Name of process]" to get process ID
  - Use "$ kill [PID]" to kill a process
  - Use "$ pkill [Name]" to kill a process by name
  - Use "$ pkill -f [Name Of python File].py"

  Try running "$ python3 stall.py" in example1
--------------------------------
   
-> Time module

  The time module is a module where you can add a wait time
into your program, not only executing time but an actual 
pause. You can use this to count the time of another 
program, to wait some time, or ecen to create a max time
a timeout, counted in seconds to your program.

+ Usage:
  - time.sleep([Number_of_seconds])
--------------------------------

-> OS module 

  The os Module is a way of running terminal commands by
python code, you can ls, change working directory, it intructionsextremely usefull in complex programs that will comunicate
with the os deeply. Is also very used in automation.

+ Usage:
 - os.system('[Terminal_command]')
 - os.chdir('/new_directory')
    Note: remember u have to cd back to "/" if running in 
      another directory

--------------------------------

-> Subprocess Module

  The Subprocess Module is a powerfull tool, it can captue 
outputs, capture exit codes, and this one creates the concempt 
of a pool, that is what allows us to run paralel processes.


+ Usage:
    - subprocess.run(['[Command]', '[Arument1]', '[Argument2]], [Options])
      Options: [capture_output=False, text=True]
      Note: The arguments normally are the flags of a program

--------------------------------

-> Paralel processing
 + Use this function to run paralel processes:
###
def run_process(process):                                                
    os.system('python3 {}'.format(process))        

pool = Pool(processes=3)                                             
pool.map(run_process, processes)     
###
With a tuple

  processes = ('p1.py', 'p2.py', 'p3.py')                                    
  - This will run all processes...

+ See example2

  See how all are called simultaniusly and they do not 
finish in order, because their internal wait times are diferent!!


--------------------------------

-> More Complex examples

+ Example3

  lets make a program watch another... we have a program that 
will run a random function that chooses a number from 0 to 1,
if its bigger than 0.5 it will execute normally, but if its
smaller than 0.5 it will get stuck, but we dont want that so we
make another program that watches the action, and make sure it doesnt
surpass 10 second. If it does it will kill the action.

  I alredy used something like this to download videos, but sometimes
when you are donwloading playlists, one video will take too long, or even
get stuck, with that it was good to make another program the counts they
main one.

  The timer program, can be made in ways so that it displays real time 
information of the program, if you are running a somulation, it is a 
smart idea do make the simulation program and the program that display 
the information in diferent processes.

--------------------------------

+ Example4

  Another big use of paralelism is to speed things up, lets create a 
large list to ilustrate this!

  We now have a list with 1001 numbers, with 4 digits, and one number is 
2222 that we added in a random position, we must find it!!

using the terminal time command we will see the execution time 
if just using a for to compare!!

Watch how "simple_search.py" found the number in:
  - 11.65 secs
And the "runner.py" found in:
  - 5.99 sec

  Half the time, remember, this can change if the number happens to be 
in the beginnin. We can break the seach in even more threads if we want
to!!

--------------------------------

Enge




