import random
import time


def multi(number1, number2):
	time_0 = time.time()
	answer = int(input(f"{number1} X {number2} = "))
	if answer == number1*number2:
		print("Correct")
		print(round(time.time()-time_0, 2))
	else:
		print("Incorrect")
		print(f"{number1} X {number2} = {number1*number2}")

while True
	multi(random.randint(1, 10), random.randint(1, 10))