# Move a func to multiple threads 
# Wait for all thread to complete

import logging
from threading import Thread
import threading
import time
import random 

# Func to perform work
def longtask(name):
    max = random.randrange(1,10)
    logging.info(f'Task: {name} performing {str(max)} times')
    for x in range(max):
        logging.info(f'Task: {name}: {x}')
        time.sleep(random.randrange(1,3))
    logging.info(f'Task: {name}: Complete')

# Main function
def main():
    logging.basicConfig(format = '%(levelname)s - %(asctime)s: %(message)s', datefmt = '%H:%M:%S', level = logging.DEBUG)
    logging.info('Starting')
    # longtask('main') very slow 
    
    # Run it on a threads multiple times 
    threads = []
    for x in range(10):
        t = Thread(target = longtask, args = ['thread' + str(x)])
        threads.append(t)
        t.start()

    # Wait for all thread to finish
    for t in threads:
        t.join()
    logging.info('Finished all threads')

if __name__ == "__main__":
    main()


