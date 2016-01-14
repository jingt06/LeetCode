def GrayCode_occ(n, List):
	if n == 0:
		return List
	else:
		new_list = list(map(lambda str: "1"+str, List)) + list(map(lambda str: "0"+str, List[::-1])) 
	return GrayCode_occ(n-1,new_list)

#GrayCode(positive integer)
def GrayCode(n):
	return GrayCode_occ(n - 1,["0", "1"])

print("GrayCode(4)")
print(GrayCode(4))