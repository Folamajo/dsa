

def sliding_window(int_list:list, window_size:int) -> int:
   if len(int_list) == 0 or window_size > len(int_list):
      raise ValueError("Window size must be less than length of integer list and integer list must not be empty")

   current_sum = sum(int_list[0:window_size])
   max_sum = current_sum

   for i in range(window_size, len(int_list)) :
      current_sum = current_sum - int_list[i - window_size] + int_list[i]
      if current_sum > max_sum:
         max_sum = current_sum
   
   return max_sum
print(sliding_window([2, 1, 5, 1, 3, 2], 3))