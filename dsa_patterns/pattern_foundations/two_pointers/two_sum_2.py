def two_sum(nums: list, target: int):
   left = 0 
   right = len(nums) - 1

   while left < right:
      if (nums[left] + nums[right]) == target:

         return [left + 1, right + 1]
      elif (nums[left] + nums[right]) > target:
         right -= 1
      elif (nums[left] + nums[right]) < target:
         left += 1 
         


input = [2,3,4]
print(two_sum(input, 6))

# TIME COMPLEXITY

# The maximum number of times the left and right move can execute in terms of n 
# is n  in the worst case scenario 
# time complexity is O(n)

# SPACE COMPLEXITY 

# WHat additional data structures are you creating
# We only created a constant number of variables (left and right)
# so our space complexity is O(1)