def max_subarray(nums:list):
   if len(nums) == 0:
      return 
   current_sum = 0
   max_sum = float('-inf')

   for i in range(len(nums)):
      current_sum = max(nums[i], (current_sum + nums[i]))
      max_sum = max(current_sum, max_sum)

   return max_sum


if __name__ == "__main__":
   input = [-5, -2, -8]
   print(max_subarray(input))