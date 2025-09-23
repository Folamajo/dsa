def max_product(nums: list):

   
   curr_max = nums[0]
   curr_min = nums[0]
   max_product = nums[0]

   for i in range(len(nums)):
      curr_max = max(nums[i], (nums[i] * curr_max))
      curr_min = min (nums[i], (nums[i] * curr_min) )
      max_product = max(curr_max, max_product)

   return 


if __name__ == "__main__":
   input = [-2]
   print(max_product(input))