def generateParenthesis(n: int) -> list[str]:
   result = []
   def backtrack(path, open, close):
      if len(path) == 2 * n :
         result.append(path)
         return
      if open < n:
         backtrack(path + "(", open + 1, close)
      if close < open:
         backtrack(path + ")", open, close + 1)

   backtrack("", 0, 0)
   return result


if __name__ == "__main__":
   n = 3
   print(generateParenthesis(n))
# The fundamental goal of the recursion is to build only strings where every prefic has more '(' than ')'
# So when building our string the number of ')' used so far must never exceed the number of '(' used so far
# Each node in the three represents a partially build string with cound of '(' and ')' used so far
# We close the branch by add ')' when the number of '(' used so far is greater thna the number of ')'
# Our base case that tells when a branch has profuced a finished solution is when the current string length is 2n
# This is considered a pruned recursion tree because invalid partial strings are never allowed to be created
# Generate parenthesis takes a two stage approach, We define the constraints clearly, then let the recursion explore ony valid branches
# We create a helper function that builds the string incrementally while tracking counts


#  Time complexity
#  The number of valid parentheses strings that exist for a given n is the ->  nth Catalan number
#  Since the algorithm generartes all valid strings and each valid string has length 2n the time complexity is then -> O(n . Catalan(n))
#  The extra n factor come from the algorithm producing / storing each completed string costs O(n)

# SPACE COMPLEXITY
# The maximum recursion stack -> O(n)
# WHen we include the space needed to store all valid parenthesis strings, the total space complexity is O(n . Catalan(n))