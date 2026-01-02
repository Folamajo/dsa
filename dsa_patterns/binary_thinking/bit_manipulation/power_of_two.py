def power_of_two(n: int):
   if n > 0 and n & (n -1 ) == 0:
      return True
   return False

if __name__ == "__main__":
   n = 1
   print(power_of_two(3))
# CONCEPT
# Binary representations of numbers that are powers of two have exactly one bit. 
# For us to even check the bits n must be greater than 0 
# When we remove the right most set bit of a binary value ( -1 ) the right most set bit becomes 0 and all bits after become 1
# we can do an an AND bitwaise operation that n AND (n - 1 ) 
# if the result is 0 we know it had only one set bit 