def trap(input:list)->int:
   if len(input) < 3:
      return 0 
   
   left = 0
   right = (len(input) -1 )
   max_left = left
   max_right = right
   result = 0 

   while left < right:
      if input[left] < input[right]:
         if input[left] > input[max_left]:
            max_left = left