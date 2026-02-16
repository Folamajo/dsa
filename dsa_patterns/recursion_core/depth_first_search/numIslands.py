def numIslands(grid: list[list[str]])-> int : 
   if not grid:
      return 0
   
   rows = len(grid)
   cols = len(grid[0])
   count = 0 #Increments when we discover a new island root

   for row in range(rows):
      for col in range(cols):


         
if __name__ == "__main__":
   grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
         ]


# CONCEPT 
# The goal is count how many connected components of '1' exist
# The job of DFS is to explore and mark all land connected to a starting land cell
# We increment our island count when we start a DFS from an unvisited land cell 
# We can ensure we prevent double counting by converting our visited land cells into water. 
# From any land cells DFS should explore Up, Down, Left, Right
# Inside the DFS function, recursion should stop if we the current cell is out of bounds or is water "0"