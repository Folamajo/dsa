class ListNode: 
   def __init__(self, data:int=0, next:"ListNode" = None):
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


def remove_nth_from_end(head:ListNode, n: int)->ListNode:
   dummy = ListNode(0)
   dummy.next = head
   front = back = dummy
   counter = 0
   while front :
      if counter < n + 1:
         front = front.next
         counter += 1

      else:
         front = front.next
         back = back.next

   back.next = back.next.next
   return dummy.next


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

   print(remove_nth_from_end(first, n=2).print_node())


# QUESTION 
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# CONCEPT
# we want to return an altered list weith a specific node removed from it to do this we need to find a way to get to the node before the node to be removed. and then we link the node before the node to be removed to the node after the node to be removed. To do this we set up a dummy node that we place before the head we set a pointer to this node as the back pointer and we set the front pointer n nodes in ahead By the time the front pointer reaches None our back pointer will be one node before the node to be removed then we can remove our node2