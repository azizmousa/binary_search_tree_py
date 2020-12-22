from Node import Node

class BinarySearchTree:

	__root = None

	def __init__(self):
		self.__root = None

	# add method that kick off the adding methodology
	def add(self, value):
		node = Node(value)
		if 	self.__root == None:
			self.__root = node 
		else:
			self.__addNode(node, self.__root)


	# the recursive add method
	# performe the add algorithm
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


	# method to kick off the tree visiting methodology (in order travers)
	def in_order_travers(self):
		self.__visit_inorder(self.__root)


	# method to perform  the process functionality to the travers operation
	def __process(self, node):
		print(node.value)


	# the recursive visiting method
	# perform in order travers
	def __visit_inorder(self, current):
		if current == None:
			return
		self.__visit_inorder(current.left_child)
		self.__process(current)
		self.__visit_inorder(current.right_child)


	def find(self, value):
		node = self.__find_node(value)
		if node == None:
			return False
		return True 


	# method to find the node of the specified value
	def __find_node(self, value):
		current = self.__root
		if current == value:
			return current
		else:
			while current != None:
				if value < current.value:
					current = current.left_child
				elif value > current.value:
					current = current.right_child
				else:
					break

			return current

	# method to remove value from the tree without change the tree structure
	def remove(self, value):
		node = self.__find_node(value)
		parent = node.parent
		# case 1: the node not exist
		if node == None:
			return False
		# case 2: the node is leaf node
		elif node.left_child == None and node.right_child == None:
			if parent.left_child == node:
				parent.left_child = None
			else:
				parent.right_child = None
		# case 3:   the node not leaf node
		# case 3.1: the node has no right child
		elif node.right_child == None:
			if parent.left_child == node:
				parent.left_child = node.left_child
			else:
				parent.right_child = node.left_child
		# case 3.2: the node has right child, 
		# 			and that right child has no left child
		elif node.right_child != None and node.right_child.left_child == None:
			node.right_child.left_child = node.left_child
			if parent.left_child == node:
				parent.left_child = node.right_child
			else:
				parent.right_child = node.right_child
		# case 3.3: the node has right child,
		# 			and that right child has left child
		elif node.right_child != None and node.right_child.left_child != None:
			current = node
			# find the most left child
			while current.left_child != None:
				current = current.left_child
			# change the parent to the current parent
			parent = current.parent
			if parent.left_child == node:
				parent.left_child = None
			else:
				parent.right_child = None
			# just repleace the node value with the current value
			node.value = current.value

		return True










