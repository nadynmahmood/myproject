import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    with lock1:
        time.sleep(1)
        with lock2:
            print("Task 1 finished")

def task2():
    with lock2:
        time.sleep(1)
        with lock1:
            print("Task 2 finished")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()
