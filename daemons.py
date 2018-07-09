import os
import time
import threading


def check(name):
    '''Check the size of file'''
    counter = 0
    size = 0
    while counter < 100:
        counter += 1
        if os.path.exists(name):
            state = os.stat(name)
            size = state.st_size

        print("thread.name=%s\tcounter=%d\tsize=%d bytes" % (
            threading.current_thread().getName(),
            counter,
            size))

        time.sleep(0.1)


def write_file(name):
    counter = 1
    while counter <= 10:
        with open(name, 'a') as file:
            file.write('1')
            print("thread.name=%s\tcounter=%d" % (
                threading.current_thread().getName(),
                counter)
            )
            time.sleep(0.3)
            counter += 1


file_name = 'file.txt'
if os.path.exists(file_name):
    os.remove(file_name)

thread_1 = threading.Thread(name='check',
                            target=check,
                            args=(file_name,),
                            daemon=True)

thread_2 = threading.Thread(name='write_file',
                            target=write_file,
                            args=(file_name,))
thread_1.start()
thread_2.start()
