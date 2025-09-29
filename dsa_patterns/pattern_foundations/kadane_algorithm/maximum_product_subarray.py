def max_product(nums: list) -> int:
   current_max = current_min = max_product = nums[0]

   for i in range(1, len(nums)):
      prev_max = current_max
      prev_min = current_min

      current_max = max (nums[i], prev_max * nums[i], prev_min * nums[i])
      current_min = min(nums[i], prev_max * nums[i], prev_min * nums[i])

      max_product = max(current_max, current_min)
   
   return max_product
     
   #We want to keep the max and minimimum 
   



if __name__ == "__main__":
   input = [2,3,-2,4]
   print(max_product(input))