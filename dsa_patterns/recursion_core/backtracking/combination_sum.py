def combination_sum(candidates: list[int], target:int) -> list[list[int]]:
   output = []
   path = []
   start = 0
   current_total = 0
   def helper(path: list[int], start : int, target: int, current_total: int):
      if current_total == target:
         output.append(list(path))
         return 
      if current_total > target: 
         return
      
      for i in range(start, len(candidates)):
         path.append(candidates[i])
         current_total += candidates[i]
         helper(path, i, target, current_total)
         remove = path.pop()
         current_total -= remove
   
   helper(path, start, target, current_total)
   return output



if __name__ == "__main__": 
   nums = [2,3,6,7]
   target = 7 
   print(combination_sum(nums, target))

# TIME COMPLEXITY
# Time complexity is determined by the size of the recursion tree (number of explored paths)
# The number of candidates from start to end determines how many branches each node in the recursion tree can have
# max depth = target / min(candidates)
# Rough upper bound -> (O (n ^ target/min))
# Output cost factor -> 

# SPACE COMPLEXITY
# What dominates the auxillary space
# The recursion stack and the current path
# O (target / min (candidates))