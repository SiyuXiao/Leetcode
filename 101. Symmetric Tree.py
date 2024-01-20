class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
'''
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
'''
a = [1,2,2,3,4,4,3]
root = TreeNode(a[0])
def tree(x):
	if not root.left and not root.right:


