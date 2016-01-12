
# water(list of integers)
def water(List):
	LeftMax = [0]
	x = 1
	# find the left max value
	while x < len(List):
		LeftMax.append(max(List[x - 1], LeftMax[x - 1]))
		x = x + 1
	RightMax = [0]
	x = len(List) - 2
	# find the right max value
	while x >= 0:
		RightMax.insert(0, (max(List[x + 1], RightMax[0])))
		x = x - 1
	# find out the number of water can be stored, which is min(RightMax, LeftMax)  - height
	total = 0
	for n in range(0, len(List) - 1):
		water = min(LeftMax[n], RightMax[n]) - List[n]
		if water < 0:
			water = 0
		total = total + water 
	return total

print(water([0,1,0,2,1,0,1,3,2,1,2,1]))  # = 6