def candy(rating):
	n = len(rating)
	inc = 1
	increment = [0] * n
	for i in range(1,n-1):
		if rating[i] > rating[i - 1]:
			if inc + 1 > increment[i]:
				inc = inc + 1
				increment[i] = inc
		else:
			inc = 1
	i = n - 2
	inc = 1
	while i >= 1:
		if(rating[i] > rating[i+1]):
			if inc + 1 > increment[i]:
				inc = inc + 1
				increment[i] = inc
		i = i - 1
	total = n
	for i in range(0,n-1):
		total = total + increment[i]
