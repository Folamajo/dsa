class Solution(object):
   def missingNumber(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      #BRUTE FORCE
      # sorted_list = sorted(nums)
      # print(sorted_list)

      # for i in range(len(sorted_list)):
      #    if i != sorted_list[i]:
      #       return i

      #O(N)

      size = len(nums)
      expected_sum = int(size * (size + 1 ) / 2) #O(1)
      sum_nums = sum(nums) #O(N)
      
      return expected_sum - sum_nums #O(1)


solution = Solution()
input = [3, 0, 1]
print(solution.missingNumber(input))