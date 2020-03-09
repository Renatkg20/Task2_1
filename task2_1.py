name_user = (input("Please input name: ")).replace(" ", "")
	
def greeting_user(name):
	return ("Hello " + name + " !!!")

output_name = greeting_user(name_user)
print(output_name)