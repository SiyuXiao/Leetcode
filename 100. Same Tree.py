class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
#答案的算法，这个算法的时间复杂度是n，因为相当于遍历了所有节点
#如果是二叉搜索的话，时间复杂度就是logn
def isSameTree(p, q):
    if not q and not p:
        return True
    elif not p or not q:
        return False
    elif p.val!=q.val:
        return False
    else:
        return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
print(isSameTree(p, q))




