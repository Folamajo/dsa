def letter_combinations(digits: str ) -> list[str]: 
   # Add guard
   if len(digits) == 0:
      return []
   
   result = []


if __name__ == "__main__":

# CONCEPT
#  In letter cmbinations, each level of the recursion tree corresponds to one digit in the input string
#  The index of the current digit and the partially buil string represent the state at each recursion node
#  We stop and record a result when the length of the built string equals the numbder of digits 
#  The number of letters mapped to the current digit will determine how many branches the nodes will have
#  No prunning is needed because every partial string can become valid.