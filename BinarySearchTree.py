from Node import Node

class BinarySearchTree:

	__root = None

	def __init__(self):
		self.__root = None


	def add(self, value):
		node = Node(value)
		if 	self.__root == None:
			self.__root = node 
		else:
			self.__addNode(node, self.__root)

	def __addNode(self, inp_node, current):
		if inp_node.value < current.value:
			if current.left_child == None:
				current.left_child = inp_node
				inp_node.parent = current
			else:
				self.__addNode(inp_node, current.left_child)
		else:
			if current.right_child == None:
				current.right_child = inp_node
				inp_node.parent = current
			else:
				self.__addNode(inp_node, current.right_child)