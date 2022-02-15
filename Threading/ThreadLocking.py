# Thread locking 
# Avoiding the dread race conditions and deadlocks 
# Race conditions: same resource modified by multiple threads 
# Deadlocks: musltiple threads waiting on the same resource 

import logging
import threading
from concurrent.futures import ThreadPoolExecutor, thread 
import time 
import random
from weakref import finalize

counter = 0 # Global variable

# Test func
def test(count):
    global counter
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')

    for x in range(count):
        logging.info(f'Count: {threadname}+= {count}')
    
        #counter += 1   # This is a bad way, multp threads working at the same time

        # Locking: The right way
        #lock = threading.Lock()
        #lock.acquire()
        #lock.acquire() # deadlock - waiting on resources
        #try: 
        #    counter += 1
        #finally:
        #    lock.release()

        # Locking Simplfied
        lock = threading.Lock()
        with lock: 
            logging.info(f'Locked: {threadname}')
            counter += 1
            time.sleep(2)


    logging.info(f'Completed: {threadname}')


def main():
    logging.basicConfig(format = '%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt = '%H:%M:%S', level = logging.DEBUG)
    logging.info('App Start')
    workers = 2

    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers*2):
            v = random.randrange(1,5)
            ex.submit(test, v) # submit to the "test" function the value "v"

    print(f'Counter: {counter}')
    logging.info('App Finished') 


if __name__ == "__main__":
    main()