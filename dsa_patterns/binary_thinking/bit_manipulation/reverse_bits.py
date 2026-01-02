def reverse_bits(n:int)-> int:
   result = 0

   for _ in range(32):
      result = result << 1
      right_bit = n & 1
      result = result | right_bit
      n = n >> 1
   return result

if __name__ == "__main__":
   n = 43261596
   print(reverse_bits(n))
# # CONCEPT
# Reversing bits means flipping the arrangment of our bits going from left to right to right to left.
# We must fix the bits to 32 because reversing the bits is undefined unless you say how many bits exist
# Bits don't come with natural boundaries, we have to choose the width or the operations has no stable meaning
# e.g 5 is 101
# 4 bit -> 0101
# 8 bit -> 00000101
# 16 bit -> 0000000000000101 

# When we reverse these they will all have different values 
# so we need to have a standard that allows us to include the leading zeros in the reversal
# Read the bits from right to left
# move the current bit in the result to the left so that it leaves space for a new bit .



