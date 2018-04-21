#Linkedlist_insert.py
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None



class Linkedlist:

	def __init__(self,node):
		self.head = node

	def add_first(self,data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def add_last(self,data):
		new_node = Node(data)
		temp_node = self.head

		while temp_node.next!=None:
			temp_node = temp_node.next

		temp_node.next = new_node


if __name__ == '__main__':
	n = Node(100)
	h = Linkedlist(n)
	h.add_first(300)
	h.add_first(400)
	h.add_first(500)
	h.add_last(100)
	h.add_last(700)

	while(h.head!=None):
		print h.head.data
		h.head = h.head.next