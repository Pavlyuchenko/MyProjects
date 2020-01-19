def addition(number):
	for i in range(0, len(number)):
		if number[-(1+i)] == 9 or number[-(1+i)] == 10:
			number[-(1+i)] = 0
			try:
				number[-(2+i)] += 1
			except:
				number.insert(0, 1)
	return number

print(addition([9, 9, 9]))