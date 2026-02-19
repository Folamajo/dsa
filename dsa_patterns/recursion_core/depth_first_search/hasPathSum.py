

class TreeNode: 
   def __init__(self, val = 0, left = None, right = None):
      self.val = val
      self.left = left
      self.right = right

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
   # Root null guard 
   if not root : 
      return False
   
   if not root.left and not root.right and targetSum - root.val == 0:
      return True
   
   return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val )

if __name__ == "__main__":
   root = TreeNode(5)
   root.left = TreeNode(4)
   root.right = TreeNode(8)
   print(hasPathSum(root, targetSum=22))

# CONCEPT 
# We are trying to check if any root to leaf path sums to target
# We know a node is  leaf when it has no children
# We handle the running sum by passing the remaining target down recursively
# When we reach a leaf node we return True if the RemainingSum - node.val === 0 
# When branching recursively we need to check either side by return dfs(left) and dfs(right)