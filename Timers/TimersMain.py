# Timers 
# Excute code at timed intervals 
# This is the first step in learning threading

import time 
from threading import Timer

def display(msg):
    print(msg + ' ' + time.strftime('%H:%M:%S'))


# Basic timer 
def run_once():
    display('Run Once: ')
    t = Timer(2, display, ['Timeout: ']) # Waits 2 seconds 
    t.start()

run_once()
print('Waiting...')

