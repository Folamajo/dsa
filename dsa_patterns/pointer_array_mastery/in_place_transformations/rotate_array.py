

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
   
   reverse_array = rotate_helper(nums, 0, (len(nums) - 1))
   reverse_first_k = rotate_helper(reverse_array, 0, k -1 )
   reverse_last_n = rotate_helper(reverse_first_k, k, (len(nums) - 1))

   return reverse_last_n

if __name__ == "__main__":
   input = [1,2,3,4,5,6,7]
   print(rotate_array(input, 3))   


#  SPACE COMPLEXITY -> amount of memory an algorithm uses as a function of the input size
#  In this algorithm our Space complexity remains O(1) because the number of variables we use are constant #  and do not increase as a function of the input size
#  
#  TIME COMPLEXITY -> amount of time an algorithm takes to complete as a function of the input size
#  our time complexity in this scenario is O(n) because our helper function initially has 
#  to iterate through our list at least once to reverse it 
#  so each time we traverse our list we are performing a linear time operation which is O(1)
#  since we do it 3 times the total work is still a constant multiple of n so it is O(3n) which is O(n)