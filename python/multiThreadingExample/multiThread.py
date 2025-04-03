#This scropt is made by Sir Nacho on 3/8/2025

import threading

sum = 0


'''

This is a basic code to create, start, and stop threading.

this code is to start a thread (in this case two)
thread1 = threading.Thread(target, args)
thread2 = threading.Thread(target, args)

this code is to start the thread
thread1.start()
thread2.start()

this code is to stop a thread
thread1.join()
thread2.join()


For locking a thread use:

intializing the var:
lock = threading.Lock()

for locking a thread:
lock.acquire()

for releasing a thread:
lock.release()

The bottom code is an example of making a multi-threaded script 
with locking
'''

def increment():
    global sum
    sum += 1

def threadTask(lock):
    for _ in range(1000000):
        lock.acquire()
        increment()
        lock.release()

def mainApp():
    global sum
    sum = 0

    lock = threading.Lock()

    thread1 = threading.Thread(target=threadTask, args=(lock,))
    thread2 = threading.Thread(target=threadTask, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()



if __name__ == "__main__":
    for i in range(10):
        mainApp()
        print("Iterations {0}: x = {1}".format(i, sum))
