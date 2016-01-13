
# RotateImage( List of (List of Integers of length n))
def RotateImage(Matrix):
	# reflect by diagonal and then reflect by horizontal mid line
	n = len(Matrix)
	i = 0
	while i < n:
		j = 0
		while j < n - i:
			Matrix[i][j], Matrix[n - 1 - j][n - 1 - i] = Matrix[n - 1 - j][n - 1 - i], Matrix[i][j]
			j = j + 1
		i = i + 1
	i = 0 
	while i < n/2:
		Matrix[i], Matrix[n - 1 - i] = Matrix[n - 1 - i], Matrix[i]
		i = i + 1
	print(Matrix)

RotateImage([[1,2], [3,4]])