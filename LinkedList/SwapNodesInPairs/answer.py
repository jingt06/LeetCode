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

def SwapPair(node):
	curr = node
	prev = None
	while curr is not None:
		if curr.next is None:
			break
		# else
		nextPair = curr.next.next
		next = curr.next
		if prev is None:
			curr.next = next.next
			next.next = curr
			node = next
			prev = curr
		else:
			curr.next = next.next
			next.next = curr
			prev.next = next
			prev = curr
		curr = nextPair
	return node

def main():
	n = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	SwapPair(n).print()

if __name__ == "__main__":
	main()