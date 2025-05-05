class Solution(object):
   def missingNumber(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      print(nums)
      sorted_list = sorted(nums)
      print(sorted_list)

      for i in range(len(sorted_list)):
         if i != sorted_list[i]:
            return i



solution = Solution()
input = [9,6,4,2,3,5,7,0,1]
print(solution.missingNumber(input))