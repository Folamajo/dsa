# https://www.youtube.com/watch?v=oBt53YbR9Kk

# Write a funcion fib(n) that takes in a number as an argumnet.
# The function should return the n-th number of the Fibonacci sequence.

def fib(n):
   if n <= 2:
      return 1
   
   return fib(n-1) + fib(n -2)



#TIME COMPLEXITY: O(2^n) we are calling our function n different function calls recursively
#SPACE COMPLEXITY: O(n) we add any stack space our function makes we call our function n times so we track those calls 

def bar(n):
   if n <= 1:
      return 1
   return bar(n - 2)

#Even though we are going down n - 2 times it O(n/2) we call it as O(n) this sis the same for its time complexity
# we can remove any multiplicative constants

def dib (n):
   if n <= 1:
      return
   dib(n - 1)
   dib(n - 1)

print(dib(6))

# dib is an example of recursive function that highlights tree recusion and exponential growth (Similar to fin(n) but no computation ).
# Tree recursion: each call branches into two more calls.
# Exponential growth: It grows like a bineary tree with 2 ^ n calls.
# height of this recursive tree is (n)
# We take the total no. of calls we take the number 2 and multiply it by n so we are 
# so TIME COMPLEXITY = O(2^n)
# SPACE COMPLEXITY: when we make a function call we add it to the stack we cakeep adding the following functions calls # to the stack till we hit our base case. when we hit the base case we make a return and that function call is removed # from the stack. and only when we return from the left one we add the right one. so the most number of stack frames # # we use is the height of our tree  O(n)

def lib(n):
   if n <= 1:
      return
   lib(n - 2)
   lib(n - 2)

#In this scenario our heigh is n/2 
# TIME COMPLEXITY (2 ^ n/2 ) -> (2^n)
# SPACE COMPLEXITY: O (n)
