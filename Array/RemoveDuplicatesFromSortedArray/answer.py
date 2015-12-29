import sys;
arr =  input("give a list of sorted array\n").split(" ")
arr = list(filter(None, arr))
prev = None
new_arr = []
for x in arr:
	if x != prev:
		prev = x;
		new_arr.append(x)
print(new_arr);