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
         directions = [(-1, 0), (1,0), (0, -1), (0, 1)]
         for (dr, dc) in directions:
            new_row = row + dr
            new_col = col + dc
            if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols:
               if grid[new_row][new_col] == 1:
                  grid[new_row][new_col] = 2
                  queue.append([new_row, new_col])
                  fresh -= 1
      if queue:
         minutes += 1

      
   return minutes if fresh == 0 else -1

if __name__ == "__main__":
   grid = [[2,1,1], [1,1,0], [0,1,1]]
   print(rottingOranges(grid))
# PATTERN RECOGNITION
# Rotting oranges is best classified as Multi source BFS
# Because rotting spreads simultaneously from all rotten oranges
# We must also track the number of fresh oranges
# One full level of BFS represents One minute
# One rotten orange can spread rot 4 directions (up, down, left, right)
# We increment the minutes counter after processing one full BFS level
# If some oranges remain we should return -1


# TIME COMPLEXITY
# During BFS how many times can a single orange enter the queue -> A single orange can enter the queue once 
# THe grid has m rows and n columns 
# The total time complexity is -> O(mn)
# The grid scan is -> O(mn)
# BFS -> each cell processed once -> O(mn)
# Total O(mn) + O(mn) = O(mn)

# SPACE COMPLEXITY
# Two things use space : the queue and the direction list
# In the worst case, the queue can hold almost al cells 
# The rot spreads and many cells maybe in the queue across levels
# Final space complexity O(mn)