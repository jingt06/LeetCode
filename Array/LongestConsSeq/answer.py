
# comsume a list of numbers
def LongestConsecutiveSequence(list):
	hashmap = {}
	for num in list:
		hashmap[num] = 0
	longest = 0
	for key, val in hashmap.items():
		if val == 1:
			continue;
		length = 1
		down = key - 1
		while hashmap.get(down) is not None:
			hashmap[down] = 1
			down = down - 1
			length = length + 1
		up = key + 1
		while hashmap.get(up) is not None:
			hashmap[up] = 1
			up = up + 1
			length = length + 1
		longest = max(longest, length)
	return  longest

print(LongestConsecutiveSequence([3,100,4,5,66]))
