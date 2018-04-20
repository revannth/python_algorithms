class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


class Linkedlist:

	def __init__(self,node):
		self.head = node



if __name__ == '__main__':
	n = Node(100)
	h = Linkedlist(n)
	second = Node(200)
	n.next = second
	third = Node(500)
	second.next = third


	while(h.head!=None):
		print h.head.data
		h.head = h.head.next