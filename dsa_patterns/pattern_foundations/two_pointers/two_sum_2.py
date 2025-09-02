def two_sum(nums: list, target: int):
   left = 0 
   right = len(nums) - 1

   # for right in range(len(nums)):
   while left < right:
      if (nums[left] + nums[right]) == target:

         return [left + 1, right + 1]
      elif (nums[left] + nums[right]) > target:
         right -= 1
      elif (nums[left] + nums[right]) > target:
         left += 1 
         


input = [2,3,4]
print(two_sum(input, 6))