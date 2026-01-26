def letter_combinations(digits: str ) -> list[str]: 
   # Add guard
   if len(digits) == 0:
      return []
   
   
   result = []
   mapping = {"2": "abc", "3":"def", "4":"ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
   
   def backtrack(index: int, path:str):
      if len(path) == len(digits):
         result.append(path)
         return 
      
      for letter in mapping[digits[index]]:
         backtrack(index + 1, path + letter)

   backtrack(0, "")
   return result


if __name__ == "__main__":
   digits = '23'
   print(letter_combinations(digits))
# CONCEPT
#  In letter cmbinations, each level of the recursion tree corresponds to one digit in the input string
#  The index of the current digit and the partially buil string represent the state at each recursion node
#  We stop and record a result when the length of the built string equals the numbder of digits 
#  The number of letters mapped to the current digit will determine how many branches the nodes will have
#  No prunning is needed because every partial string can become valid. 


#  TIME COMPLEXITY
#  The input has n digits each digit maps to most 4 letters so in the wort case scenario we can map to O(4 ^ n) leaf nodes
#  So time complexity is O(n * 4 ^ n)

#  SPACE COMPLEXITY
#  For the stack only the space complexity dure to the reursion stack and current path in terms of n digits is B
#  The space nneded to store all combinations is O(n * 4n)