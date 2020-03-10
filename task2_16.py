# def weihgt(wgt, year):
# 	your_weihgt = wgt +(wgt *0.165)
# 	g = int(your_weihgt)
# 	for i in range(g, year+1, 1):
# 		result = int(your_weihgt) + int(i)
# 		return result

# print(weihgt(80, 15))

wgt = int(input())
year = int(input())

your_weihgt = round(wgt *0.165)
for i in range(year+1):
 	result = int(your_weihgt) + i
 	print(result)