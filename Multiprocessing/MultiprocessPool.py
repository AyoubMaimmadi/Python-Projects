# Multiprocess pool
# Pools are processes and their results

import logging
import multiprocessing
from multiprocessing.context import process
import time 
import random

# Worker Process
def work(item, count):
    name = multiprocessing.current_process().name
    logging.info(f'{name} Started')
    for x in range(count):
        logging.info(f'{name} {item}')
        time.sleep(1)
    logging.info(f'{name} Finished')
    return item + ' is finished'

# Main process
def proc_result(result):
    logging.info(f'Result: {result}')



def main():
    logging.info(f'Started')

    max = 5
    pool = multiprocessing.Pool(max)
    results = []
    for x in range(max):
        item = 'Item' + str(x)
        count = random.randrange(1,5)
        r = pool.apply_async(work, [item, count], callback = proc_result)
        results.append(r)

    # Wait for the results 
    for r in results:
        r.wait()

    # pool.close or pool.terminate
    pool.close()
    pool.join()
    logging.info(f'Finished') 


logging.basicConfig(format = '%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt = '%H:%M:%S', level = logging.DEBUG)    
if __name__ == "__main__":
    main()