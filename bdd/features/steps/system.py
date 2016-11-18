import psutil
import pyscreenshot
import time

def is_program_running(name):
    for proc in psutil.process_iter():
        try:
            if proc.name() == name:
                    return True
        except AccessDenied:
            print("Process is not allowing us to view the CPU Usage!")
        except psutil.NoSuchProcess:
            pass
    print("{} was not found in process list".format(name))
    return False

def screenshot_to_file(filename=None):
    if filename is None:
        filename="screenshot"+time.strftime("%c")+".jpg"
    pyscreenshot.grab_to_file(filename)
    
