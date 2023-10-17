import threading

def task():
    # Code for the task to be performed concurrently
    pass

def multi_threading():
    # Create multiple threads
    thread1 = threading.Thread(target=task)
    thread2 = threading.Thread(target=task)
    thread3 = threading.Thread(target=task)

    # Start the threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for all threads to complete
    thread1.join()
    thread2.join()
    thread3.join()

multi_threading()