


# QUESTION : 202. Happy Number
   # Write an algorithm to determine if a number n is happy.
   # A happy number is a number defined by the following process:
   # Starting with any positive integer, replace the number by the sum of the squares of its digits.
   # Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
   # Those numbers for which this process ends in 1 are happy.
   # Return true if n is a happy number, and false if not.

# CONCEPT
   # We take a number we replace it with the sum of its squared digits continuously we loop over these digits 
   # If we eventurally get to 1 we return true 
   # else we return false 
   # We can detect the repitition using Floyd's cycle detection 
   # Create a function that accepts a number and get the sum of the squares of its digits 
   # Brute force would mean we store everything in a set and check if we've seen it before. 

