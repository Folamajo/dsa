def remove_duplicates(nums: list):

   left = 0
   right = 1

   for right in range(1, len(nums)):
      if nums[left] != nums[right]:
         nums[left + 1] = nums[right]
         left += 1 
   

   return left + 1


      
   
   
#Get time complexity

input = [1,1,2]
print(remove_duplicates(input))