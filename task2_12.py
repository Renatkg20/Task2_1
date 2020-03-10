# Read an integer:
a = input("Pls enter the string ")

try:
  result = a.index('f')
  result1 = a.rindex('f')
  if result == result1:
    print(result)
  elif result != result1:
    print(result, result1) 
except ValueError:
  print("") 



#   chudo code

#  s = input()
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') >= 2:
#     print(s.find('f'), s.rfind('f'))