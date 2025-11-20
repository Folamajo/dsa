def binary_search(input:list, target:int):
   # initialise varibales 
   left = 0
   right = len(input) - 1

   while left <= right:
      middle = left + int((right - left ) / 2)
      if input[middle] == target : 
         return middle
      elif target > input[middle]:
         left = middle + 1
      else:
         right = middle - 1
   return -1 

if __name__ == "__main__":
   input = [-1,0,3,5,9,12]
   target = 9 
   print(binary_search(input, target))