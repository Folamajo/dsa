def hamming_weight(n:int)-> int:
   num_set_bits = 0
   temp_n = n 

   while not temp_n == 0:
      
#CONCEPT
# We are calculating the number of 1's in the binary representation of a value
# The rightmost is called the Least Significant Bit(LSB)
# It has has the smallest value: 1 
#  It changes most often: 
   # if it is 1 the number is odd 
   # if it is 0, the number is even 

# We are working with pure integers and bit operations
# We start with a number n
# Remove one set bit 
# count how many times we do that
# Stop when there are no set bits left
# while our n is not equal to zero we know there are set bits left to remove