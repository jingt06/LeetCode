# 3Sum(list of integers)
def Three_Sum(list):
	list.sort()
	i = 0
	j = len(list)-1
	while i <= len(list) - 3:
		j = len(list) - 1
		while j - i > 1:
			k = j - 1
			while k > i and list[k] + list[i] + list[j] >= 0:
				if list[k] + list[i] + list[j] == 0:
					print("%d %d %d" % (list[i], list[k], list[j]))
					break;
				k = k - 1
			j = j - 1
		i = i + 1

Three_Sum([-1, 0, 1, 2, -1, -4])