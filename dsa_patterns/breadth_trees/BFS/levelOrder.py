from collections import deque

class TreeNode :
   def __init__(self, val = 0, left= None, right = None):
      self.val = val
      self.left = left
      self.right = right


def levelOrder(root: [TreeNode]) -> list[list[int]]:
   if not root:
      return []
   
   result = []
   queue = deque([root])

   while queue: 
      level_size = len(queue)
      level = []

      for _ in range(level_size):
         node = queue.popleft()
         level.append(node.val)

         if node.left:
            queue.append(node.left)
         if node.right:
            queue.append(node.right)
      
      result.append(level)
   
   return result

if __name__ == "__main__":
   # root = [3, 9, 20, None, None, 15, 7]
   root = TreeNode(3)
   root.left = TreeNode(9)
   root.right = TreeNode(20)
   root.right.left = TreeNode(15)
   root.right.right = TreeNode(7)
   print(levelOrder(root))




# TIME COMPLEXITY: There are N nodes, time complexity = O(n)
# SPACE COMPLEXITY: Consider the max number of nodes in the queue at once at the worst case this would be a full level = O(n)