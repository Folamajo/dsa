def move_zeroes(nums:list)-> list:
   non_zero = 0

   for i in range(len(nums)):
      if not nums[i] == 0:
         nums[non_zero] = nums[i]
         non_zero += 1 
  
   for i in range(non_zero, len(nums)):
      nums[i] = 0 
   
   return nums
   


if __name__ == "__main__":
   nums = [-1,0,0,1,0]
   print(move_zeroes(nums))


# QUESTION
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# CONCEPT
# we set a two pointers to our first value i moves through the array nz tracks where we will place our non zero value. 
# when if the value in index is not equal to 0 we take the value in index i  and 
# replace it with the value in index nz and move both forward if the value at index i = 0 we simply leave nz where it is and move index i forward
# when the first loop is done replace the remaining values starting from index non-zero to the end of nums as the are the values that need to be replaced



#  PSEUDOCODE:
#  Create variable that acts as a pointer to where the next value will go
#  we set up our loop using a normal for loop
#  if i is on a value greater than zero 
#     we put that value in position nz
#     move nz by 1
#  loop over new list from the position of nz
#     replace remaining values with zero