def trap(input:list)->int:
   if len(input) < 3:
      return 0 
   
   left = 0
   right = (len(input) -1 )
   max_left = left
   max_right = right
   trapped_water = 0 

   while left < right:
      if input[max_left] < input[max_right]:
         left += 1