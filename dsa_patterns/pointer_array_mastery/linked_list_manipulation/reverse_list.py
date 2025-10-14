def reverse_list(head):


if __name__ == "__main__":


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