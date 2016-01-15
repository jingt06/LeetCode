
# CountingInversions(List of intergers, List of integers)
# Return [number of inversion, merged sorted list]
def Merge(List1, List2):
	count = 0
	newList = []
	while List1 or List2:
		if List1 and List2:
			if List1[0] >= List2[0]:
				newList = newList + [List2[0]]
				count = count + len(List1)
				List2.pop(0)
			else:
				newList = newList + [List1[0]]
				List1.pop(0)
		elif List1:
			newList = newList + [List1[0]]
			List1.pop(0)
		elif List2:
			newList = newList + [List2[0]]
			List2.pop(0)
	return [count, newList]

# CountingInversions(List of intergers)
# Return [number of inversion, sorted list]
def CountingInversions(List):
	l = len(List)
	if l <= 1:
		return [0, List]
	else: 
		s1 = CountingInversions(List[0:l//2])
		s2 = CountingInversions(List[l//2:l])
		s3 = Merge(s1[1], s2[1])
	return [s1[0]+s2[0]+s3[0], s3[1]]


print(CountingInversions([1,3,6,8,4,5]))