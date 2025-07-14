from pprint import pprint

def grid_traveler(m, n):
   #Create table
   grid = [[0 for i in range(n + 1)] for i in range(m + 1)]

   #Base case
   grid[1][1] = 1

   #Fill the table 
   for i in range(m + 1):
      for j in range(n + 1):
         if i < m:
            grid[i + 1][j] += grid[i][j]
         if j < n:
            grid[i][j + 1] += grid[i][j]

   return grid[m][n]
print(grid_traveler(3,3))