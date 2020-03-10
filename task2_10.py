a = (input("Pls enter the string "))
print(a[2])
print(a[-2])
print(a[0:5])
print(a[:-2])

for i in range(0,len(a), 2):
    print(a[i], end = "")

print("")

for c in range(1,len(a), 2):
    print(a[c], end = "")
    
print("")

l = []
for b in a:
    l.append(b)
l.reverse()
j  = "".join(l)
print(j)

new_list = []
for z in range(0, len(l), 2):
    k = new_list.append(l[z])
p = "".join(new_list)
print(p)
print(len(a))

# Chudo code ))) Vse prosto
s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

    
