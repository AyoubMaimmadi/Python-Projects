import random
import string

chars = string.ascii_letters + string.digits + '!@#$%^&*()'

for i in range(10): # 10 passwords
	password = ''.join(random.choice(chars) for i in range(10))
	# print('--->password '+ str(int(i)+1)  + ' ==> '+ password)
	print(f'--->password {i}  ==>  {password}')
