
# CompleteCircuit(list, list)
def CompleteCircuit(gas, cost):
	total = 0
	j = -1
	i = 0
	current_sum = 0
	while i < len(gas):
		sum = sum + gas[i] - cost[i]
		total = total + gas[i] - cost[i]
		i = i + 1
		if(sum < 0):
			j = i
			sum = 0
	if total >= 0:
		return j+1
	else: 
		return -1