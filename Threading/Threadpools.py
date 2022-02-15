# Threadpools
# Reusing existing threads, because creating threads is expensive
# If you have a large body of work do not creat a thread for each item
# Instead use the thread pool executor

import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time 
import random

# Test Func 
def test(item):
    s = random.randrange(1,10)
    logging.info(f'Thread {item}: id = {threading.get_ident()}')
    logging.info(f'Thread {item}: name = {threading.current_thread().name}')
    logging.info(f'Thread {item}: sleep for = {s}')
    time.sleep(s)
    logging.info(f'Thread {item}: finished')

# Main func
def main():
    logging.basicConfig(format = '%(levelname)s - %(asctime)s: %(message)s', datefmt = '%H:%M:%S', level = logging.DEBUG)
    logging.info('App Start')

    workers = 5
    items = 5
    # ThreadPoolExecutor: to use a max number of workers
    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(test,range(items))

    logging.info('App Finished')

if __name__ == "__main__":
    main()