def trap(input:list)->int:
   if len(input) < 3:
      return 0 
   
   left = 0
   right = (len(input) -1 )
   max_left = input[left]
   max_right = input[right]
   result = 0 

   while left < right:
      if max_left <= max_right:
         left += 1
         if input[left] > max_left:
            max_left = input[left]
         else:
            result += max_left - input[left]
      elif max_left > max_right:
         right -= 1 
         if input[right] > max_right:
            max_right = input[right]
         else:
            result += max_right - input[right]

     

   return result


#Time complexity : Because our left and right pointer only move just one at a time so it is linear time O(n)
#Space complexity : Storing five variables 

if __name__ == "__main__":
   input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
   print(trap(input))
