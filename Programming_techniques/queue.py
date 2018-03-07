#queue.py

class ArrayQueue:

	DefaultSize = 10

	def __init__(self):

		self._data = [None]*ArrayQueue.DefaultSize
		self._size = 0
		self._front = 0


	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size==0

	def first(self):

		if self.is_empty():
			raise Empty('Queue is Empty')

		return self._data[self._front]


	def dequeue(self):

		if self.is_empty():
			raise Empty('Queue is Empty')

		answer = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front+1)%len(self._data)
		self._size = 1
		return answer
	def enqueue(self,p):
		if self._size==len(self._data):
			self._resize = (2*self._data)
		avail = (self._front + self._size)%len(self._data)
		self._data[avail] = p
		self._size+=1
	def resize(self,ope):

		old = self._data
		self._data = [None]*ope

		walk = self._front

		for k in range(len(self._data)):
			self._data[k] = old[walk]
			walk = (walk+1)%len(old)

		self._front = 0



