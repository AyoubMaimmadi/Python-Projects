# Tree structure
class BinaryTree (object):
	# Starts the Node
	def __init__ (self, node):
		self.node = node
		self.left = None
		self.right = None

	def addChild (self, childNode):
		if childNode == self.node:
			return

		# Left = less than current node
		elif childNode < self.node:
			# If node already has a child on the left
			if self.left:
				self.left.addChild (childNode)			
			else:
				self.left = BinaryTree (childNode)

		# Right = more than current node
		else:
			# If node already has a child on the right
			if self.right:
				self.right.addChild (childNode)
			else:
				self.right = BinaryTree (childNode)

	# Returns a sorted array
	def sortTree (self):
		array = []

		# if there is a left node
		if self.left:
			# builds array with recursion
			array += self.left.sortTree ()
	
		# appends the "root" of left subtree 
		array.append (self.node)

		# if there is a right node
		if self.right:
			# builds array with recursion
			array += self.right.sortTree ()

		return array		

# Returns the beginning of the Tree
def buildTree (array):
	# Beginning of the tree
	root = BinaryTree (array[0])

	# Adds all the childs from the array
	for idx in range (1, len(array)):
		root.addChild(array[idx])
	
	return root
