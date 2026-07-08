import threading

counter = 0
# Threading lock object to prevent race conditions
counter_lock = threading.Lock()

def increment_counter(iterations):
    global counter
    for i in range(iterations):
        # for automatically handles lock acquisition and release
        with counter_lock:
            counter = counter + 1

def main():
    thread_iteration = 1000000
    t1 = threading.Thread(target= increment_counter, args= (thread_iteration,))
    t2 = threading.Thread(target= increment_counter, args= (thread_iteration,))
    t3 = threading.Thread(target= increment_counter, args= (thread_iteration,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()  
    t2.join()
    t3.join()

    print(f"Expected counter value: {thread_iteration * 3}")
    print(f"Final Synchronized counter value: {counter}")

if __name__ == "__main__":
    main()