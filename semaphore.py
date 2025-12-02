import threading
import time

sema = threading.Semaphore(2)

def access(name):
    sema.acquire()
    print(name, "entered")
    time.sleep(1)
    print(name, "exited")
    sema.release()

for i in range(5):
    t = threading.Thread(target=access, args=(f"Thread {i}",))
    t.start()
