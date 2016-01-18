
# SetMatrixZero(Matrix), Matrix is a list of list of number
# runtime O(nm), space O(1)
def SetMatrixZero(Matrix):
	col_has_zero = False # if first column contains 0
	row_has_zero = False # if first row contains 0

	for row in Matrix:
		if row[0] == 0:
			col_has_zero = True
			break

	for num in Matrix[0]:
		if num == 0:
			row_has_zero = True
			break

	for i in range(0, Matrix):
		for j in range(0, len(Matrix[0])):
			if Matrix[i][j] == 0:
				Matrix[i][0] = 0
				Matrix[0][j] = 0

	for i in range(1,Matrix):
		if Matrix[i][0] == 0:
			for j in range(0, Matrix[i]):
				Matrix[i][j] = 0
		if col_has_zero:
			Matrix[i][0] = 0

	for j in range(1,Matrix[0]):
		if Matrix[0][j] == 0:
			for i in range(0, Matrix):
				Matrix[i][j] = 0
		if row_has_zero:
			Matrix[0][j] = 0