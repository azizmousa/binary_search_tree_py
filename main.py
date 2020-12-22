from BinarySearchTree import BinarySearchTree

tree = BinarySearchTree()

tree.add(4)
tree.add(2)
tree.add(1)
tree.add(3)
tree.add(8)
tree.add(6)
tree.add(5)
tree.add(7)

tree.in_order_travers()

print("search result = ", tree.find(6))

print("remove result = ", tree.remove(6))

tree.in_order_travers()