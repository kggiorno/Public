## Collatz sequence function checks for even, if so it prints number // 2
## If odd, multiplies num by 3 and adds 1
## This program will take a user input integer, and modify it through the collatz sequence until it equals 1

def collatz(number):
	if number % 2 == 0:
		collatzNum = int(number / 2)
		return collatzNum
	else:
		wonkyNum = int(3 * number + 1)
		return wonkyNum

def getUserInteger():
	userInputNum = input('Please enter an integer:')
	while True:
		try:
			userInt = int(userInputNum)
			return userInt
		except:
			print("You tryin to break me? That wasn't an integer punk, try again.")
			userInputNum = input("Please enter an integer:")
			continue

userInteger = getUserInteger()
while True:
	if userInteger == 1:
		print(userInteger)
		break
	else:
		print(userInteger)
		userInteger = collatz(userInteger)
		continue