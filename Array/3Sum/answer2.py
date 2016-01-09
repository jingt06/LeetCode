def TwoSumSorted(List, sum):
	i = 0
	j = len(list) - 1
	while i != j:
		if List[i] + List[j] == sum:
			return [List[i], List[j]]
		elif List[i] + List[j] > sum:
			j = j - 1
		else:
			i = i + 1 
	return []

def ThreeSum(List, sum):
	for num in range(0, len(List)):
		new_list = List[:num] + List[num + 1:]
		result = TwoSumSorted(new_list.sort(), sum - List[num]) 
		if result != []:
			print("%d %d %d" % (result[0], result[1], List[num]))
			return
	print("None")