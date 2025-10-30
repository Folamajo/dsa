
def rotate_array(nums, k):
   k = k % len(nums)
   if len(nums) <= 1 or k == 0 :
      return nums