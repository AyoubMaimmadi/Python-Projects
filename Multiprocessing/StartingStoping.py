# Starting and Stoping
# The full process life cycle 

import logging
import multiprocessing
from multiprocessing.context import Process
import time 

def work(msg, max):
    name = multiprocessing.current_process().name
    logging.info(f'{name} Started')
    for x in range(max):
        logging.info(f'{name} {msg}')
        time.sleep(1)
    logging.info(f'{name} Finished')

# Main process

def main():
    logging.info(f'Started')

    max = 2
    worker = Process(target = work, args = ['Working', max], daemon = True, name = 'Worker')
    worker.start()

    time.sleep(5)

    # if process is running, stop it 
    if worker.is_alive:
        worker.terminate() # Sends back a signal of termination
    worker.join()
    
    # exitcode == 0 is good
    # Anything else is an error

    logging.info(f'Finished: {worker.exitcode }')

logging.basicConfig(format = '%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt = '%H:%M:%S', level = logging.DEBUG)    
if __name__ == "__main__":
    main()