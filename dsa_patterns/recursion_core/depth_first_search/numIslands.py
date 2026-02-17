def numIslands(grid: list[list[str]])-> int : 
   if not grid:
      return 0
   
   rows = len(grid)
   cols = len(grid[0])
   count = 0 #Increments when we discover a new island root

   def dfs(row, col):
      if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
         return
      grid[row][col] = "0"
      dfs(row + 1, col)
      dfs(row - 1, col)
      dfs(row, col + 1)
      dfs(row, col - 1)
   

   for row in range(rows):
      for col in range(cols):
         if grid[row][col] == "1":
            count += 1 
            dfs(row, col)
   
   return count 
if __name__ == "__main__":
   grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
   ]
   print(numIslands(grid))

# CONCEPT 
# The goal is count how many connected components of '1' exist
# The job of DFS is to explore and mark all land connected to a starting land cell
# We increment our island count when we start a DFS from an unvisited land cell 
# We can ensure we prevent double counting by converting our visited land cells into water. 
# From any land cells DFS should explore Up, Down, Left, Right
# Inside the DFS function, recursion should stop if we the current cell is out of bounds or is water "0"


# TIME COMPLEXITY 
# The grid has m rows and n columns , the time complexity is => O(mn)

#SPACE COMPLEXITY
# if the entire grid is one giant island 
# DFS keeps expanding 
# Recursion depth can reach m x n