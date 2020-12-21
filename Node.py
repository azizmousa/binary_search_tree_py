class Node:
	__parent = None
	__left_child = None
	__right_child = None
	__value = None

	def __init__(self, value):
		self.__parent = None
		self.__left_child = None
		self.__right_child = None
		self.value = value