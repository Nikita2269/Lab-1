import os
import time

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def animation():
    frame1 = '''
           \   /
            \ /  
             * 
           \***/
          \*****/
           \***/
           \* */
           \* */
            * *
            * *
             * 
            '''
    
    frame2 = '''
           \   /
            \ /
            * * 
* * * * * * * * * * * * * *
    * * * * * * * * * *
        * * * * * *
      * * * *** * * *
        * * * * * *
            * * 
            * *
             *
            '''
    
    while True:
        clear_console()
        print(frame1)
        time.sleep(0.5)
        clear_console()
        print(frame2)
        time.sleep(0.5)

animation()