import psutil

def is_program_running(name):
    for proc in psutil.process_iter():
        try:
            if proc.name() == name:
                    return True
        except AccessDenied:
            print("Process is not allowing us to view the CPU Usage!")
        except psutil.NoSuchProcess:
            pass
    print("{} program doesn't exist".format(name))
    return False