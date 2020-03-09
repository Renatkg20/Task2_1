apples = int(input("Pls enter the number of apples "))
students = int(input("Pls enter the number of students "))
if apples % students == 0:
	apple_for_students = apples // students
	print(f"Apple for each student {apple_for_students}, there is no apples in the busket")
elif apples % students != 0:
	busket = apples % students
	apples = apples - busket
	apple_for_students = apples // students
	print(f"Apple for each student {apple_for_students}, there is {busket} apples in the busket")
elif apples == 0:
	print("Do not divid on zero")
else:
	print("Something went wrong")