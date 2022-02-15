# Simple producer and consumer 
# Demonstarates queue and event with locks 

import random
import threading
import multiprocessing
import logging
import time 
from threading import Thread
from queue import Queue
logging.basicConfig(format = '%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt = '%H:%M:%S', level = logging.DEBUG)    

# Functions
def display(msg):
    threadname = threading.current_thread().name
    processname = multiprocessing.current_process().name
    logging.info(f'{processname}\{threadname}: {msg}')

# Producer 
def creat_work(queue, finished, max):
    finished.put(False)
    for x in range(max):
        v = random.randint(1,100)
        queue.put(v)
        display(f'Producing: {x}: {v}')
    finished.put(True)
    display('finished')

# Consumer
def perform_work(work, finished):
    counter = 0
    while True:
        if not work.empty():
            v = work.get()
            display(f'Consuming {counter}: {v}')
        else:
            q = finished.get()
            if q == True:
                break
        display('finished')

# Main function
def main():
    max = 50
    work = Queue()
    finished = Queue()

    producer = Thread(target=creat_work, args=[work, finished, max], daemon=True)
    consumer = Thread(target=perform_work, args=[work, finished], daemon=True)

    producer.start()
    consumer.start()

    producer.join()
    display('Producer has finished')

    consumer.join()
    display('Consumer has finished')

    display('Finished')

if __name__ == "__main__":
    main()
