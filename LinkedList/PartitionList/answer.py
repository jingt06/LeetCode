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

def Partition(node, k):
	left_head = None;
	left_tail = None;
	right_head = None;
	right_tail = None;
	curr = node;
	while curr is not None:
		if curr.val < k:
			if left_head is None:
				left_head = curr
				left_tail = curr
			else:
				left_tail.next = curr
				left_tail = curr
			curr = curr.next
			left_tail.next = None
		else:
			if right_head is None:
				right_head = curr
				right_tail = curr
			else:
				right_tail.next = curr
				right_tail = curr
			curr = curr.next
			right_tail.next = None
	if left_head is None:
		return right_head
	else:
		left_tail.next = right_head
		return left_head

def main():
    n = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
    Partition(n, 3).print()


if __name__ == "__main__":
    main()