class Node:
	def __init__(self, val=None, next=None):
		self.next = next
		self.val = val

	def __str__(self):
		return str(self.val)

	def print(self):
		print(self)
		if self.next is not None:
			self.next.print()

def RmKthFromEnd(node, k):
	node, num = RmKthRec(node, k)
	return node

def RmKthRec(node, k):
	if node.next is None:
		num = 1
		if k == num:
			return None, num
		else:
			return node, num
	else:
		result, num = RmKthRec(node.next, k)
		num = num + 1
		if num == k:
			return result, num
		else:
			node.next = result
			return node, num

def main():
	n = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	RmKthFromEnd(n, 2).print()

if __name__ == "__main__":
	main()