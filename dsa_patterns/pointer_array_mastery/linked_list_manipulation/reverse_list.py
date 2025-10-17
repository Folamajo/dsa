class ListNode:
   def __init__(self, data: int, next : "ListNode" = None):
      self.data = data
      self.next = next


   def print_node(self):
      node = self 
      while node:
         print(node.data, end = " --> ")
         if node.next:
            node = node.next
         else:
            print("null")
            return



def reverse_list(head) -> ListNode:
   prev = None
   current = head

   while not current is None:
      next = current.next
      current.next = prev
      prev = current
      current = next
   return prev



if __name__ == "__main__":
   first =  ListNode(1)
   second = ListNode(2)
   third = ListNode(3)
   fourth = ListNode(4)
   fifth = ListNode(5)

   first.next = second
   second.next = third
   third.next = fourth
   fourth.next = fifth

   print(reverse_list(first).print_node())

#QUESTION
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# CONCEPT 
# reversing a linked list means take the next pointer of each node and pointing it to the prevous node 
# if there is no previous like the head we point it to a null or None variable or value
# The head's next becomes None, Each subsequent node points backwards to the one before it and the tail becomes the new head
# We will need a 3 pointers, one on the current node, one on the previous node and one on the next node. 

# PSEUDOCODE 
# Set prev = None
# Set current = head
# While the current is not None:
   # next = curr.next
   # current.next = prev
   # prev = current 
   # current = next
# return prev # this will be the new head


#TIME COMPLEXITY
   # You traverse the list once, touch each node exactly one time
   # TIME -> O(n)

#SPACE COMPLEXITY 
   # SPACE -> O(1)
   # We only used three pointers (prev, current, next)