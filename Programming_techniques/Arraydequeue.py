#dequeue.py

class Queue:

	defaultsize = 10

	def __init__(self):

		self._data = [None]*Queue.defaultsize
		self._front = 0
		self._back = 0
		self._size = 0


	def __len__(self):
		return self._size
	def is_empty(self):
		return self._size==0
	def add_first(self,e):

		if self._size==len(self._data):
			self._size = self.resize(2*len(self._data))

		

		if self._front-1>0:
			self._front = (self._front - 1)%(len(self._data))
		else:
			self._front = len(self._data)
		
		self._data[self._front] = e
		self._size+=1
		

	def add_back(self,e):

		if self._size == len(self._data):
			self._size = self.resize(2*len(self._data))

		
		self._back = (self._back+self._size)%len(self._data)
		self._data[self._back]=e


		self._size+=1

	def delete_first(self):

		if self.is_empty:
			raise Empty('Empty')
		else:
			self._data[self._front]=None
			self._front = (self._front + 1)%(len(self._data))
			self._size-=1
	def delete_back(self):
		if self.is_empty:
			raise Empty('Empty')
		else:
			self._data[self._back]=None
			if self._back-1>0:
				self._back = self._back-1
			else:
				self._back = len(self._data)
			self._size-=1




		
