def maxAreaOfIslands(grid: list[list[int]])-> int:

   #  Edge case guard - We don't want to process an empty grid
   if not grid: 
      return 0
   
   # Store Dimensions – This gives us boundaries for DFS
   rows = len(grid)
   cols = len(grid[0])
   max_area = 0

   # Create dfs function 
   def dfs(row, col):
      # Base case to stop our recursion when we are out of bounds or in water
      if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
         return 0 
      
      # We sink the cell once we know it is valid land. 
      grid[row][col] = 0
      return 1 + dfs(row + 1, col) + dfs(row -1, col) + dfs(row, col + 1) + dfs(row, col - 1)
   # Grid traversal
   for row in range(rows):
      for col in range(cols):
         if grid[row][col] == 1:
            area = dfs(row, col)
            print(type(area), type(max_area))
            max_area = max(max_area, area)
   return max_area


if __name__ == "__main__":
   grid = [ [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0] ]
   
   print(maxAreaOfIslands(grid))
# CONCEPT
# The main difference between Number of Islands and Max Area of Island ? We must compute the size of each connected component and track the max
# In number if islands DFS did not return anything it just sank the islands that we checked. Here we actually want to return the number of cells in the current island so that we can track the max.
# We receive the area from DFS and we update the max_area
# The area of the island should be calculated by Returning 1+ sum of areas from all four recursive neighbours


# TIME COMPLEXITY 
# The grid has m rows and n columns so it is O(m x n)

# SPACE COMPLEXITY 
#