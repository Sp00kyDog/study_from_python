num = 0
num2 =100
while num < num2:
	num = num + 1
	if num%3==0 and num%5==0:
		print("FIzzBuzz")
	elif num%3==0:
		print ("Fizz")	
	elif num%5==0:
		print ("Buzz")	
	else:
		print (num)