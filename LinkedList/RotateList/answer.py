class Node:
	def __init__(self, val=None, next=None):
		self.val = val
		self.next = next

	def print(self):
		print(self.val)
		if self.next is not None:
			self.next.print()

	def len(self, n=None):
		if n is None:
			n = 1
		else:
			n = n + 1
		if self.next is None:
			return n
		else:
			return self.next.len(n)

def RotateList(node, k):
	len = node.len()
	k = k % len
	# now k < len must be true
	curr = node
	prev = None
	tail = None
	kth = None
	i = 0
	while i < len:
		if i == k-1:
			prev = curr
			kth = curr.next
		if i == len - 1:
			tail = curr
		curr = curr.next
		i = i + 1
	tail.next = node
	prev.next = None
	return kth

def main():
	n = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	RotateList(n, 2).print()

if __name__ == "__main__":
	main()