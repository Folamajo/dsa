
def single_number(nums: list[int]) -> int:
   ans = 0 
   for i in range(len(nums)):
      ans = ans ^ nums[i]
   return ans



if __name__ == "__main__":
   nums = [2,2,1]
   print(single_number(nums))

#CONCEPT 
# This questions relies on using bitwise operations to compare values. 
# we use XOR bit operation because it allows us to to compare two values if they are the same we get 0 if they are not we get that value back 

