# Better than printing 
'''
Logging levels from small to critical: 
    debug
    info
    warning
    error
    critical
'''


import logging 
# from logging import root
# Basic logging 
# They do not all get displayed by default 

def test():
    print('~'*20)
    level = logging.getLevelName(logging.getLogger().getEffectiveLevel())
    print(f'Log level: {level}')
    logging.debug('debug message here')
    logging.info('info message here')
    logging.warning('warning message here')
    logging.error('error message here')
    logging.critical('critical message here')
    print('~'*20)

test()
     
# Logging levels 
# Getting and setting the logging levels 
# Allows for filtering 

# Get the root logger
rootlog = logging.getLogger()
print('Level: ' + logging.getLevelName(rootlog.getEffectiveLevel()))

# Set it to debug
rootlog.setLevel(logging.DEBUG)
test()

# Set it to critical
rootlog.setLevel(logging.CRITICAL)
test()

# Set it to warning
rootlog.setLevel(logging.WARNING)
test()

# Log to file
handler = logging.FileHandler('file.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
rootlog.addHandler(handler)
rootlog.setLevel(logging.DEBUG)
rootlog.debug('test')
test()