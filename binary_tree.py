class newNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None



def findMax(root):

	if (root == None):
		return float('-inf')

	
	res = root.data
	lres = findMax(root.left)
	rres = findMax(root.right)
	if (lres > res):
		res = lres
	if (rres > res):
		res = rres
	return res


if __name__ == '__main__':
	root = newNode(5)
	root.left = newNode(6)
	root.right = newNode(33)
	root.left.right = newNode(21)
	root.left.right.left = newNode(11)
	root.left.right.right = newNode(17)
	root.right.right = newNode(4)
	root.right.right.left = newNode(26)

	print("Maximum element is",
		findMax(root))

