

def rotate_helper(nums:list, start: int, end: int):
   while  start < end : 
      temp = nums[start]
      nums[start] = nums[end]
      nums[end] = temp
      start += 1
      end -= 1
   return nums

def rotate_array(nums, k):
   k = k % len(nums)
   if len(nums) <= 1 or k == 0 :
      return nums
   
   reverse_array = rotate_helper(input, 0, (len(nums) - 1))
   reverse_first_k = rotate_helper(reverse_array, 0, k -1 )
   reverse_last_n = rotate_helper(reverse_first_k, k, (len(nums) - 1))

   return reverse_last_n

if __name__ == "__main__":
   input = [1,2,3,4,5,6,7]
   print(rotate_array(input, 3))   