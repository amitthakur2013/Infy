class Node:
	def __init__(self,data):
		self.__data=data
		self.__ndext=None

	def get_data(self):
		return self.__data
	
	def get_next(self):
		return self.__next
		
	def set_data(self,data):
		self.__data=data

	def set_next(self,next):
		self.__next=next

class LinkedList:
	def __init__(self):
		self.__head=None
		self.__tail=None

	def get_head(self):
		return self.__head

	def get_tail(self):
		return self.__tail

	def add(self,data):
		new_node=Node(data)
		if self.__head is  None:
			self.__head=self.__tail=new_node
		else:
			self.__tail.set_next(new_node)
			self.__tail=new_node
	
	def display(self):
		temp=self.__head
		while temp is not None:
			print(temp.get_data())
			temp=temp.get_next()
		
	def find_node(self,data):
		temp=self.__head
		while temp is not None:
			if temp.get_data()==data:
				return temp
			temp=temp.get_next()
		return None
	def insert(self,data,data_before):
		new_node=Node(data)
		temp=self.__head
		if data_before is None:
			new_node.set_next(self.__head)
			self.__head=new_node
			if new_node.get_next() is None:
				self.__tail=new_node
		else:
			while temp is not None:
				if temp.get_data()==data_before:
					break
				temp=temp.get_next()
			new_node.set_next(temp.get_next())
			if new_node.get_next() is None:
				self.__tail=new_node
	
	def delete(self,data):
		node=self.find_node(data)
		if node is not None:
			if node==self.__head:
				if self.__tail==self.__head:
					self.__tail=None
				self.__head=node.get_next()
			else:
				temp=self.__head
				while temp is not None:
					if temp.get_next()==node:
						temp.set_next(node.get_next())
						if node==self.__tail:
							self.__tail=temp
						node.set_next(None)
						break
					temp=temp.get_next()
		else:
			print("The element to be deleted does not exists!!")

	def __str__(self):
		temp=self.__head
		msg=[]
		while temp is not None:
			msg.append(str(temp.get_data()))
			temp=temp.get_next()
		msg=" ".join(msg)
		return msg

list1=LinkedList()
list1.add("Sugar")
list1.add("Tea Bags")
list1.add("Milk")

list1.display()
			

