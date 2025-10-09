class ListNode : 
   def __init__(self, data: int, next : "ListNode" = None):
      self.data = data
      self.next = next

   
   def printNode(node:"ListNode"):
      while node.next:
         print(node.data)
      return


def middle_node(head:ListNode) -> ListNode:
   slow = fast = head

   while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
   
   return slow

if __name__ == "__main__" :
   head = ListNode(1)
   second = ListNode(2)
   third = ListNode(3)
   fourth = ListNode(4)
   fifth = ListNode(5)

   head.next = second
   second.next = third
   third.next = fourth
   fourth.next = fifth

   print(middle_node(head))

# QUESTION 
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# CONCEPT
# How do we find the middle node before knowing the list's length in advance.
# We can use two pointer again
# We set our pointers at the start and create a while loop 
# The slow pointer moves one at a time and the fast pointer moves in twice at a time
# At the end of our loop our slow pointer should be in the middle of our Linked list

# TIME COMPLEXITY 
#  O(n) -> Because we traverse our array once 

# SPACE COMPLEXITY
# O(1) Because we dont create any new data structures