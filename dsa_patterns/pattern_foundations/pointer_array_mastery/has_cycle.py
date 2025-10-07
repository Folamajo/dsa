class ListNode: 
   def __init__(self, data: int, next: "ListNode" = None):
      self.data = data
      self.next = next
      




def hasCycle(head) -> bool:
   slow = fast = head

   while fast and fast.next: 
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
         return True
   return False



if __name__ == "__main__" :

   head = ListNode(3)
   second_node = ListNode(2)
   third_node = ListNode(0)
   fourth_node = ListNode(-4)

   head.next = second_node
   second_node.next = third_node
   third_node.next = fourth_node
   fourth_node.next = second_node


   # input = [3, 2, 0, -4]
   print(hasCycle(head))
# WHAT IS A LINKED LIST CYCLE
# A linked list has a cycle if there is a node in the list that we continuously reach when we keep following the next pointer
# so usually in a linked list if we keep following the pointer we would reach null.  In this case we would just end up back at one of the nodes

# BRUTE FORCE
# This involves using a hash map that stores each node we see and if we come across a code we have already seen we know its a cycle
# or if we reach null we know theres no cycle

# FASTER SOLUTION
# Floyd's cycle detection
# Move one pointer slowly (one step at a time) and another pointer faster(two steps at a time)
#The idea is that as we move each poiinter there will eventually be a point where both pointers meet if there is a cycle
# If there is no cycle the fast pointer will eventually keep going till it reaches null then there is no loop and we return false 
# if both our pointers eventually collide at a point we one of our values back to the head and move both by one step the point where they both collide again is our start pointer of the cycle

# IMPLEMENTATION
# We set both our slow and fast to the head
# We set our while loop to track if fast and fast.next is true 
# We then check if our slow and fasst ever reach this means we have a cycle we simply return True
# else we return at the end of our loop False