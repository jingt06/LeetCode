
#TwoSumSorted(list of sorted integers, target sum)
def TwoSumSorted(List, sum):
	i = 0
	j = len(list) - 1
	while i != j:
		if List[i] + List[j] == sum:
			print("%d %d" % List[i], List[j])
			return
		elif List[i] + List[j] > sum:
			j = j - 1
		else:
			i = i + 1 
	print("None")