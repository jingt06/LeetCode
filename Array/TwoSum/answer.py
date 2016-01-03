
# comsume a list of numbers and a integer
# Runtime: O(n)
def TwoSum(list, target):
	hashmap = {}
	count = 1
	for key in list:
		find = hashmap.get(target - key) 
		if find is not None:
			print("%d %d" % (find, count))
			return
		else:
			hashmap[key] = count
			count = count + 1
	print(-1)

TwoSum([1,2,7,3,10], 9)