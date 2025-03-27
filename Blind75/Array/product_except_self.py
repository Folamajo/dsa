class Solution(object):
   def productExceptSelf(self, nums):
      """
      :type nums: List[int]
      :rtype: List[int]
      """
      answer = [1] * len(nums)

      left_previous = 1
      for i in range(len(nums)):
         answer[i] = left_previous
         left_previous *= nums[i]

      right_previous = 1
      for i in reversed(range(len(nums))):
         answer[i] *= right_previous
         right_previous *= nums[i]

      return answer

# O(2n) => O(n) Time complexity
#O(1) space complexity

array = [1,2,3,4]

solution = Solution()
print(solution.productExceptSelf(array))