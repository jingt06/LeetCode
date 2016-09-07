class Node:
	def __init__(self, val=None, next=None):
		self.val = val
		self.next = next

	def __str__(self):
		return str(self.val)

	def print(self):
		print(self)
		if(self.next):
			self.next.print()

def reverse(node):
	if node.next is None:
		return node
	curr = node
	next = node.next
	end = None
	while curr is not None:
		next = curr.next
		curr.next = end
		end = curr
		curr = next
	return end

n = Node(1, Node(5, Node(3, Node(8))))
reverse(n).print()