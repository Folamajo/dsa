Node = {"data" : 1, "next" : None}

def Node(data:int, next = None):
   return {"data": data, "next": next}

def traverseLinkedList(node):
   current_node = node
   while current_node['next'] is not None:
      print(current_node)
      current_node['data'] = current_node['next']
      current_node['next'] = None
      
      
head = Node(1)
second_node = Node(2)
third_node = Node(3)
head["next"] = second_node["data"]
second_node["next"] = third_node["data"]

print(traverseLinkedList(head))



# print(head.)
# tail = None
# size = 0

# curr = head