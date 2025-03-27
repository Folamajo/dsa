# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

class Solution(object):
   def threeSum(self, nums):
      """
      :type nums: List[int]
      :rtype: List[List[int]]
      """
   #Sort the array first 
      nums.sort()
   # Initialise output
      result = []
      for i in range(len(nums)):
         left = i + 1
         right = len(nums) - 1

         while left < right : 
            if nums[i] == nums[left] :
               left += 1

            if nums[i] + nums[left] + nums[right] == 0:
               result.append([nums[i], nums[left], nums[right]])
            else:
               left += 1
      
      return result

input = [-1, 0, 1, 2, -1, -4]
solution = Solution()
print(solution.threeSum(input))