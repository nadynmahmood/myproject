import threading
import time

def task():
    print("Start:", threading.current_thread().name)
    time.sleep(1)
    print("End:", threading.current_thread().name)

t1 = threading.Thread(target=task, name="Thread-1")
t2 = threading.Thread(target=task, name="Thread-2")

t1.start()
t2.start()

t1.join()
t2.join()

