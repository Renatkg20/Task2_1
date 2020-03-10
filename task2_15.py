g = int(input("Enter your age "))
if g % 2 == 0:
	for age in range(0, g+2, 2):
		print(age)
elif g % 2 != 0:
	for age in range(1, g+2, 2):
		print(age)
else:
	print("Something is getting wrong")