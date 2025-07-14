# Say that you are a traveler on a 2D grid. You begin
# in the top-left corner and your goal is to travel to 
# the bottom-right corner. You may only move down or right
# In how many ways can you travel to the goal on a grid with 
# dimension m * n
#Write a function `gridTraveler(m, n)` that calulates this.

# def gridTraveler(m, n ):
#    if m == 1 and n == 1:
#       return 1
#    if m == 0 or n == 0:
#       return 0
   
#    return gridTraveler(m - 1, n) + gridTraveler(m, n - 1)





def gridTraveler(m, n, memo = {}):
   if m == 1 and n == 1:
      return 1
   if m == 0 or n == 0:
      return 0
   
   key = tuple(sorted((m, n)))
   if key in memo:
      return memo[key]
   
   memo[key] = gridTraveler(m - 1, n, memo ) + gridTraveler(m , n-1, memo)
   return memo[key]
   # if the combination of m and n in memo return the result 
   # memo[m, n] = gridTraveler(m - 1, n, memo ) + gridTraveler(m , n-1, memo)
   # TIME complextiy for memoization is O(m * n)time -> O (m)time we are running it once 
   # SPACE complexity is O(m + n )

print(gridTraveler(18,18))