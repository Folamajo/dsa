

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
   root.left.left = TreeNode(11)
   root.left.left.left = TreeNode(7)
   root.left.left.right = TreeNode(2)
   root.right.left = TreeNode(13)
   root.right.right = TreeNode(4)
   root.right.right.right = TreeNode(1)


   print(hasPathSum(root, targetSum=22))

# CONCEPT 
# We are trying to check if any root to leaf path sums to target
# We know a node is  leaf when it has no children
# We handle the running sum by passing the remaining target down recursively
# When we reach a leaf node we return True if the RemainingSum - node.val === 0 
# When branching recursively we need to check either side by return dfs(left) and dfs(right)

# TIME COMPLEXITY
# If the binary tree had n nodes the time complexity is 
# Worst case we might visit every node once
# We do constant work per node 
# So TIME = O(n)

# SPACE COMPLEXITY 
# The space complexity in terms of tree height h 
# O(h)