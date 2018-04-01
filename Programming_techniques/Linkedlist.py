class Node:
	def __init__(self,data):
		self.data = data
		self.next =  None

	def set_next(self,node):
		self.next=node


class Linkedlist:
	def __init__(self):
		self.head = None
		self.tail = None


	def insert_front(self,data):
		new_node = Node(data)
		if self.head!=None:
			new_node.set_next(self.head)
		else if self.head==None:
			self.tail=new_node
		self.head=new_node
		

	def insert_behind(self,data):
		new_node = Node(data)
		if self.tail!=None:
			self.tail.set_next(new_node)
		self.tail = new_node


	def __str__(self):
		s = ""

		p = self.head

		if p!=None:
			while p.next!=None:
				s+=p.data+'\n'
				p=p.next
			s+=p.data+'\n'

		else:
			s="Empty"

		return s

if __name__ == '__main__':
	l = Linkedlist()
	l.insert_front('5')
	l.insert_front('10')
	l.insert_behind('20')
	l.insert_front('3000')
	print l
	