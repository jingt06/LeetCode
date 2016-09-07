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

def RmDup(node): # node is a sortedt linked list
	curr = node
	prev = None
	head = None
	tail = None
	while curr is not None:
		if head is None:
			head = curr
			tail = curr
			prev = curr.val
		elif curr.val == prev:
			curr = curr.next
			continue
		else:
			tail.next = curr
			prev = curr.val
			tail = curr
		curr = curr.next
	tail.next = None
	return head



def main():
    n = Node(1, Node(1, Node(2, Node(3, Node(3, Node(3))))))
    RmDup(n).print()


if __name__ == "__main__":
    main()