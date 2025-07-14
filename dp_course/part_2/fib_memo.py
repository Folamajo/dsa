#Fib sequence has O(2^n)
# How can we be faster
# Time complexity is a bottle neck
# Since there are sub trees we can just calculate the values of these sub trees 
# We store these subtree results in in a memo so we dont have to calulate them again 
# This pattern of overlapping subproblems is known as dynamic programming

#Fib with memoization
# gives us O(n) because we grow lineary.

def fib(n, memo = {}):
   # create base case
   # check if our value is in out memo  
   # memo function
   if n <= 2:
      return 1 
   
   if n in memo:
      return memo[n]
   

   memo[n] = fib(n-1, memo) + fib(n-2, memo)
   return memo[n]

print(fib(6))