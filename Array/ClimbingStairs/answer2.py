from math import sqrt, floor, pow
# ClimbingStairs(positive integer)
def ClimbingStairs(n):
	return floor(((pow((1+sqrt(5))/2, n - 1)) - pow((1-sqrt(5))/2, n - 1))/sqrt(5)) 