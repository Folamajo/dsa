class Solution(object):
   def maxSubArray(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """

      current_sum = 0
      max_sum = float('-inf')
    
      for i in range(len(nums)):
         current_sum += nums[i]
         
         if current_sum > max_sum:
            max_sum = current_sum 

         if current_sum < 0:
            current_sum = 0

      return max_sum
      # output = float('-inf')
      
      # for i in range(len(nums)):
      #    for j in range(i, len(nums)):
      #       sum = nums[i] + nums[j]

      # if sum > output:
      #    output = sum 

      # return output

array=[-3, -2, -5]
solution = Solution()
print(solution.maxSubArray(array))