class TreeNode:
	def __init__(self, val):
		self.left = None 
		self.right = None 
		self.val = val



class Solution:
	def solution(self, root):
		if not root or (not root.left and not root.right):
			return 0 

		self.tilt = 0

		self.traversal(root)

		return self.tilt


	def traversal(self, root):
		if not root:
			return 0 

		if root.left:
			left = self.traversal(root.left)

		if root.right:
			right = self.traversal(root.right)

		self.tilt += abs(left - right)

		return left + right + root.val