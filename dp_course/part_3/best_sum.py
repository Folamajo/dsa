# Write a function 'bestSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments
# The function should return an array containing the shortest combination of numbers that add up to 
# exactly the targetSum
# If there is a tie for the shortest combination, you may return one of the shortest

def best_sum(target, numbers, memo = {}):
   if target == 0:
      return []
   if target < 0:
      return None 
   
   if target in memo:
      return memo[target]
   
   shortest_combo = None
   for num in numbers:
      remainder_result = best_sum(target - num, numbers, memo)

      if not remainder_result == None:
         combination = remainder_result + [num]
         if shortest_combo == None or (len(combination) < len(shortest_combo)):
            shortest_combo = combination
   
   memo[target] = shortest_combo
   # print(memo)
   return shortest_combo



print(best_sum(8, [2,3,5]))

# TIME COMPLEXITY:
# how many distinct values can our target become => m to 0 => m + 1 => m
# for each unique target how many recursive calls can be made in the worst case scenario => => O(n)
# So our time complexity is O(m x n)  

# SPACE COMPLEXITY
# There are two key contributors: 
   # Call Stack Depth 
   # Stored Values  
# Maximum depth of the recursive call stack => in the worst case scenaro O(m)
# Memo dict => Up to m entries => O(m)
# Since we are storiong a full list of entries it would be O(m^2) in the worst case scenario