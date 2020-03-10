def fact1(a):
	if a == 0:
		return 1
	else:
		return a*fact1(a -1)

t  = int(input("insert numb "))

print(fact1(t))
