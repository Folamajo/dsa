def is_happy(input:int)->bool:
   
   def get_next(num):
      sum = 0 
      for digit in str(num):
         sum += (int(digit) ** 2)
      return sum

   fast = slow = input

   while True:
      slow = get_next(slow)
      fast = get_next(get_next(fast))

      if slow == fast:
         return False
      elif fast == 1 or slow == 1:
         return True


if __name__ == "__main__":
   input = 1
   print(is_happy(input))


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
   # # Brute force would mean we store everything in a set and check if we've seen it before. 

   # We have our input we create a function that calculates the squares of our number we set our slow and fast pointers to the input we run our function for slow and fast if either is equal to 1 we know we have a happy number we return true if fast === slow we know we have a cycle we return false

# PSEUDOCODE
   # 1. We define a function that takes a value and returns the sum of the square digits 
   # 2. We set two variables fast and slow to equal our input 
   # 3. We run a while loop that chacks if fast and slow are not equal to 1 
   # 4. Inside the loop we run out function on slow and set the value to slow i.e slow = f(slow) 
   # 5. We do the same for fast but we want two steps so we say f(f(fast) 
   # 6. we check if fast and slow are equal we return false 7. We return true