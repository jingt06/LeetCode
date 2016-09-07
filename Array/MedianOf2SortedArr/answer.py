def findMedianOf2SortedArr(A, B):
	total = len(A) + len(B)
	return k_th(A, B, total//2 + total % 2)


def k_th(A, B, k):
	# assume len(A) > len(B)
	if len(B) > len(A):
		return k_th(B, A, k)
	if len(B) == 0:
		return A[k]
	if k == 1:
		return min(A[0], B[0])

	if len(A) < k//2:
		return k_th(A, B[k//2:], k - k//2)
	elif len(B) < k//2:
		return k_th(A[k//2:], B, k - k//2)
	elif A[k//2] > B[k//2]:
		return k_th(A, B[k//2:], k - k//2)
	else:
		return k_th(A[k//2:], B, k - k//2)


a = [1,2,3,4,5,6,7] # 7
b = [3,4,6,8,9,10,12] # 7
print(findMedianOf2SortedArr(a, b))