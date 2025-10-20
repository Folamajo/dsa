class ListNode: 
   def __init__(self, val:int=0, next:"ListNode" = None):
      self.val = val
      self.next = next


def remove_nth_from_end(head:ListNode, n: int):




if __name__ == "__main__":
# QUESTION 
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# CONCEPT
# we want to return an altered list weith a specific node removed from it to do this we need to find a way to get to the node before the node to be removed. and then we link the node before the node to be removed to the node after the node to be removed. To do this we set up a dummy node that we place before the head we set a pointer to this node as the back pointer and we set the front pointer n nodes in ahead By the time the front pointer reaches None our back pointer will be one node before the node to be removed then we can remove our node2