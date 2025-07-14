

def fib(n):
   result = [0] * (n + 1)
   result[0] = 0
   result[1] = 1

   for i in range(2, n+1):
      result[i] = result[i-1] + result[i-2]
   return result[n]


#Time and space complextity

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))