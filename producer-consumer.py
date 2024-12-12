
from threading import Thread, Lock
from queue import Queue

q = Queue(maxsize=10) # Bounded queue with a maximum size of 10
final_results = []
lock = Lock() # Lock for thread-safe access to shared resources

def producer():
    for i in range(100):
        q.put(i)
        print(f"Produced: {i}")

def consumer():
    while True:
        number = q.get() #Block if the queue is empty
        result = (number, number**2)

        # Thread-safe appending to final results
        with lock:
            final_results.append(result)
        print(f"Consumed: {result}")
        q.task_done() # Mark the task as done
   
  # Start multiple consumer threads
for i in range(5):
    t = Thread(target=consumer)
    t.daemon = True
    t.start()
    
producer() # Start the producer

q.join() # Wait for all the items to be processed

print ("Final Results:", final_results)