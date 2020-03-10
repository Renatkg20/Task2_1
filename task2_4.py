import math

def difference(hour, minutes, seconds):
	return (hour * 60 * 60) + (minutes * 60) + seconds

def difference1(hour, minutes, seconds):
	return (hour * 60 * 60) + (minutes * 60) + seconds

result1 = difference(14,50,23) 
result2 = difference(14,32,33)
total = result2 - result1
print(math.fabs(total))
