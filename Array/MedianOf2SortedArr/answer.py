def findMedianOf2SortedArr(A, size_A, B, size_B):
	total = size_A + size_B
	if total % 2:
		return k_th(A, size_A, B, size_B, total//2 + 1)
	else:
		return k_th(A, size_A, B, size_B, total//2)


def k_th(A, size_A, B, size_B, k):
	if m > n:
		return k_th(B, size_B, A, size_A, k)
	if m == 0:
		return B[k - 1]
	if k == 1:
		return min(A[0], B[0])
	a = min(k//2, size_A)
	b = k - a
	if A[a - 1] < B[b -1]:
		return k_th(A[a:], size_A - a, B, size_B, k - a)
	elif A[a - 1] > B[b -1]:
		return k_th(A, size_A, B[b:], size_B - b, k - b)
	else :
		return A[a - 1]