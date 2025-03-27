class Solution(object):
   def maxProduct(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      current_product_left = 1
      current_product_right = 1
      max_product = float('-inf')

      for i in range(len(nums)):
         if nums[i] == 0:
            current_product_left = 1
            max_product = max(max_product, 0)
         else:
            current_product_left *= nums[i]
            max_product = max(max_product, current_product_left)
   
      for i in reversed(range(len(nums))):
         if nums[i] == 0:
            current_product_right = 1
            max_product = max(max_product, 0)
         else:
            current_product_right *= nums[i]
            max_product = max(max_product, current_product_right)
      return max_product
   




      # for i in range(len(nums)):
      #    current_product *= nums[i]

      #    if current_product > max_product:
      #       max_product = current_product
      #    else:
      #       current_product = 1  
      # return max_product

      


input = [-2, 3, -4, 5, -6]
solution = Solution()
print(solution.maxProduct(input))