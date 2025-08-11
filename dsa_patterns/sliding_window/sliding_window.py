

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

# TIME COMPLEXITY
#    - Identify inputs => 
#       int_list = i 
#       window_size = k 
#    - Check time complexity of first edge case:
#       current_sum = sum(int_list[0:window_size]) = O(k) we are only touch k elements
#    - max_sum = current_sum is = O(1) it is a simple assignment - we can include it but it wont change final result
#    -  Check loop:
#       for i in range(window_size, len(int_list)) :
#       How long is the loop = O (n - k) lenght of list and length of window.
#       -  We assign and compare current_sum to max_sum
#          This is O(1)
#       -  What is then the totak complexity of whole loop if the loop runs (n-k) and each iteration is O(1)
#          How many times does it run?
#          We already figured out the loop runs (n - k) times.
#          How much work happens each time? 
#          Inside the loop, each step is O(1) — a fixed amount of work.
#          O(n -k ) * O(1) => O(n - k ) => O(n)
#    - Total time complexity => O(k) + o(1) + O(n) => O(n + k) => O(n)

#  SPACE COMPLEXITY: Amount of memory the algorithm needs to run in addition to the input size
#     -  We are storing a fixed number of variables (current_sum and max_sum, loop index)
#        So our space complexity os O(1)





# Time Complexity:
#    “The algorithm first computes the sum of the first k elements in O(k) time, then slides the window across 
#     the remaining (n - k) elements, updating the sum in O(1) time per step, which totals O(n - k) ≈ O(n). 
#     Since k is much smaller than n in most cases, the overall time complexity is O(n).”
# Space Complexity:
#    “We only use a fixed number of variables — current_sum, max_sum, and a loop index — 
#     regardless of input size, so      the space complexity is O(1).”

