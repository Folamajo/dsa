from collections import deque

class TreeNode:
   def __init__(self, val=0, left = None, right = None):
      self.val = val
      self.left = left
      self.right = right


def minDepth(root: TreeNode) -> int:
   if not root:
      return 0
   
   queue = deque([(root, 1)])

   while queue:
      node, depth = queue.popleft()

      if not node.left and not node.right:
         return depth
      
      if node.left:
         queue.append((node.left, depth + 1))
      
      if node.right:
         queue.append((node.right, depth + 1))

   return 0


if __name__ == "__main__":
   root = TreeNode(3)
   root.left = TreeNode(9)
   root.right = TreeNode(20)
   root.right.left = TreeNode(15)
   root.right.right = TreeNode(7)

   print(minDepth(root))



# TIME COMPLEXITY: If there are n nodes and each node is visited at most once => O(n)
# SPACE COMPLEXITY: Queue can hold up to the max width of the tree => O(n)