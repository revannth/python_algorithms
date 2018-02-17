#Stack.py

class ArrayStack:

	def __init__(self):
		self.stack = []

	def push(self,number):

		self.stack.append(number)

	def pop(self):

		return self.stack.pop()

	def top(self):

		return self.stack[-1]

	def is_empty(self):

		if len(self.stack)==0:
			return True
		return False
	def __len__(self):

		return len(self.stack)





if __name__ == '__main__':
	stck = Stack()
	stck.push(20)
	stck.push(40)
	stck.push(100)
	print(len(stck))
	stck.pop()
	print(len(stck))
	stck.push(120)
	print(stck.top())

