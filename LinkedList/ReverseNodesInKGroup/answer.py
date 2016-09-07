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

def ReverseKGroups(node, k):
	curr = node
	prev = None
	while curr is not None:
		breakLoop = False
		i = 0
		tail = None
		head = curr
		while i < k:
			if i == k - 1:
				tail = curr
			elif curr.next is None:
				breakLoop = True
				break
			curr = curr.next
			i = i + 1
		if breakLoop:
			if prev is None:
				break
			else:
				prev.next = head
				break
		# from head to tail is a k-size linked list
		# and curr is pointing to the next node after k-size list
		# now reverse it
		reversePrev = head
		reverseCurr = head.next
		for i in range(0, k-1):
			next = reverseCurr.next
			reverseCurr.next = reversePrev
			reversePrev = reverseCurr
			reverseCurr = next
		# get a reversed small list
		if prev is None:
			node = tail
		else:
			prev.next = tail
		prev = head
	return node

def main():
	n = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
	ReverseKGroups(n, 3).print()

if __name__ == "__main__":
	main()