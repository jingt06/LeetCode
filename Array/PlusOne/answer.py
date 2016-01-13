
# PlusOne(List of number of single digits)
# runtime O(n), space O(1)
def PlusOne(List):
	print("%s + 1" %List)
	n = len(List) - 1
	c = 1 # carry
	while n >= 0 and c == 1:
		List[n] = List[n] + 1
		if List[n] == 10:
			List[n] = 0
			c = 1
		else:
			c = 0
		n = n - 1
	if c == 1:
		List = [1] + List
	print(List)

PlusOne([9,9,9])