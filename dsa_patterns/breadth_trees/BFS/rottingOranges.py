from collections import deque

def rottingOranges(grid:list[list[int]]) -> int:
   if not grid: 
      return 0
   
   rows = len(grid)
   cols = len(grid[0])

   queue = deque()
   fresh = 0
   minutes = 0

   for row in range(rows):
      for col in range(cols):
         curr_orange = grid[row][col]
         if curr_orange == 2:
            queue.append([row, col])
         
         elif curr_orange == 1: 
            fresh += 1 


   while queue:
      level_size = len(queue)

      for _ in range(level_size):
         rotten_orange = queue.popleft()
         row, col = rotten_orange

         

# PATTERN RECOGNITION
# Rotting oranges is best classified as Multi source BFS
# Because rotting spreads simultaneously from all rotten oranges
# We must also track the number of fresh oranges
# One full level of BFS represents One minute
# One rotten orange can spread rot 4 directions (up, down, left, right)
# We increment the minutes counter after processing one full BFS level
# If some oranges remain we should return -1
