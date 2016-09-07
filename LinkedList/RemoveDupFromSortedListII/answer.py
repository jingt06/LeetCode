class Node:
	def __init__(self, val=None, next=None):
		self.next = next
		self.val = val

	def __str__(self):
		return str(self.val)

	def print(self):
		print(self)
		if(self.next):
			self.next.print()

def RmDup (node):
	head = None
	tail = None
	curr = node
	prev = None
	while curr is not None:
		if (prev is None or prev != curr.val) and (curr.next is None or curr.next.val != curr.val):
			if head is None:
				head = curr
				tail = curr
			else:
				tail.next = curr
				tail = curr
			prev = curr.val
			curr = curr.next
			tail.next = None
		else:
			prev = curr.val
			curr = curr.next
	return head

def main():
	n = Node(1, Node(2, Node(3, Node(3, Node(4, Node(4, Node(5)))))))
	n = RmDup(n).print()

if __name__ == "__main__":
	main()