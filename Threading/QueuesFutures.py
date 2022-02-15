# Queues and Futures
# Getting values from a thread 
# This is a problem for future me 

from concurrent import futures
from concurrent.futures.thread import _worker
import logging
import threading
from threading import Thread
import random
import time
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

# Queues
# Use the queue to pass messges back and forth

def test_que(name, que): # This is what runs on the thread  
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')
    time.sleep(random.randrange(1,5))
    logging.info(f'Fninished: {threadname}')
    ret = 'Hello ' + name + ' Your random number is: ' + str(random.randrange(1,100))
    que.put(ret)

def queued(): # This creats the thread
    que = Queue()
    t = Thread(target = test_que, args = ['Ayoub', que])
    t.start()
    logging.info(f'Do something on the main thread')
    t.join()
    ret = que.get()
    logging.info(f'Returned: {ret}')

# Futures 
def test_future(name): # This is what runs on the thread  
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')
    time.sleep(random.randrange(1,5))
    logging.info(f'Fninished: {threadname}')
    ret = 'Hello ' + name + ' Your random number is: ' + str(random.randrange(1,100))
    return ret 

def pooled(): # Better way than usung queues
    workers = 20
    ret = [] # Collect a list of future values that we wanna work with in the future 
    with ThreadPoolExecutor(max_workers =  workers) as ex:
        for x in range(workers):
            v = random.randrange(1,5)
            future = ex.submit(test_future, 'Ayoub' + str(x))
            ret.append(future)
    logging.info(f'Do something on the main thread')
    for r in ret:
        logging.info(f'Returned: {r.result()}')# Get the result of eachone of those futures 


# Main func
def main():
    logging.basicConfig(format = '%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt = '%H:%M:%S', level = logging.DEBUG)    
    logging.info('App Start')
    #queued()
    pooled()


if __name__ == "__main__":
    main()