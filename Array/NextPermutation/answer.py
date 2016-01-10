def NextPermutation(List):
	postion = 0
	iterator = len(List) - 1
	acc = List[iterator]
	while iterator > 0:
		iterator = iterator - 1
		if List[iterator] < acc:
			break
		acc = List[iterator]
	iterator2 = len(List) - 1
	while iterator2 > iterator:
		if List[iterator2] >= acc:
			break
		else:
			iterator2 = iterator2 - 1
	tmp = List[iterator2]
	List[iterator2] = List[iterator]
	List[iterator] = tmp
	new_List = List[0:iterator+1]
	for i in reversed(List[iterator+1:]):
		new_List = new_List + [i]
	print(new_List)


arr =  input("give a list of integers\n").split(" ")
arr = list(map(int,filter(None, arr)))
NextPermutation(arr)
