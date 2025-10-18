class ListNode:
   def __init__ (self, data: int, next:"ListNode" = None):
      self.data = data
      self.next = next
   

def merge_two_lists(list1, list2)->ListNode : 
   dummy = ListNode(0)
   tail = dummy

   while list1 and list2:
      if (list1.data <= list2.data):
         tail.next = list1
         list1 = list1.next
      else:
         tail.next = list2
         list2 = list2.next

      tail = tail.next
   if list1 == None:
      tail.next = list2
   elif list2 == None:
      tail.next = list1
   return dummy.next
      
# QUESTION
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.


# CONCEPT
# We start by creating a dummy node
# we attach a pointer this node that allows us to determine the tail of the merged list
# We then attach pointers to our two lists 
# We compare the value at each pointer and attach to our dummy node
# We move the pointer from whereever we attached 
# We then attach the left over nodes

#PSEUDOCODE
# Create function title that accepts two lists:
#     Create dummy Node 
#     Create variable tail that points to dummy node 
#     Define while loop while both lists hae nodes:
#        Compare their current values
#        Attach the smaller one to the merged list(tail.next)
#        Move the pointer forward in that list
#        Move tail forward
#     Attach rest of the list to the tail
#     return Merged list head


#TIME COMPLEXITY 
# O(n) we visit each node once
# SPACE COMPLEXITY
# O(1) we reused existing nodes only constant pointers