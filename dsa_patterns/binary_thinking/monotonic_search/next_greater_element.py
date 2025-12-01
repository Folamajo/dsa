
def nextGreaterElement(nums1:list[int], nums2: list[int]) -> list[int]:
   stack = []
   dict = {}
   result = []
   
   for i in range( len(nums2)):
      if len(stack) == 0 :
         stack.append(nums2[i])
      else: 
         if nums2[i] > stack[-1]:
            remove = stack.pop()
            dict[remove] = nums2[i]
            stack.append(nums2[i])
         elif nums2[i] < stack[-1] :
             dict[stack[-1]] = -1
             stack.append(nums2[i])

      dict[nums2[-1]] = -1

   for i in range(len(nums1)):
      if nums1[i] in dict:
         result.append(dict[nums1[i]])

   return result

if __name__ == "__main__":
   nums1 = [4,1,2]
   nums2 = [1,3,4,2]
   print(nextGreaterElement(nums1, nums2))

# Brute force 
# For each number in nums1:
# Find where that number appears in nums2
# From that index, scan to the right
# Look for the first number that is greater
# If you find one → that’s the next greater
# If not → return -1
# This is 100% correct for the brute force way.

#Stack is LIFO