
# ClimbingStairs(positive integer)
def ClimbingStairs(n):
	prev = 0
	curr = 1
	for i in range(0,n):
		tmp = curr
		curr = prev + curr
		prev = curr + tmp
	return curr