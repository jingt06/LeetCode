#Runtime: O(n)

import sys;
arr =  input("give a list of sorted array\n").split(" ")
arr = list(filter(None, arr))
prev = None # keep track of the previous number
count = 0 # count how many times a number is duplicate
new_arr = []
for x in arr:
	if x != prev:
		prev = x
		new_arr.append(x)
		count = 0
	else:
		count = count + 1
		if(count <= 1):
			new_arr.append(x)
print(new_arr);