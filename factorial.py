def factorial(num):
	answer = 1
	for i in range(num, 0, -1):
		answer *= i
	
	return answer

print(factorial(4))