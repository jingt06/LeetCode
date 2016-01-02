
import sys;



def search(list, size, num):
	first = 0;
	last = size;
	while first != last:
		mid = first + (last - first) // 2
		if list[mid] == num :
		 	return mid
		if list[first] <= list[mid]:
			if list[first] <= num and num < list[mid]:
				last = mid
			else:
				first = mid + 1
		else:
			if list[mid] < num and num <= list[last - 1]:
				first = mid + 1
			else:
				last = mid
	return -1


arr =  input("give a list of rotated sorted array\n").split(" ")
num = int(input("give the number you want to search\n"))
arr = list(map(int,filter(None, arr)))
size = len(arr)
print(search(arr,size,num))

