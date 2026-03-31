from collections import deque
def alienOrder(words : list[str]) -> str: 
   graph = { char : [] for word in words for char in word}
   in_degree = { char : 0 for word in words for char in word }

   for i in range(len(words) - 1):
      word1, word2 = words[i], words[i + 1]
      for j in range(min(len(word1), len(word2))):
         if word1[j] != word2[j]:
            graph[word1[j]].append(graph[word2[j]])
            in_degree[word2[j]] += 1
            break

      if len(word1) > len(word2) and word1.startswith(word2):
         return ""
   
   queue = deque([char for char in in_degree if in_degree[char] == 0 ])
   order = []
   while queue: 
      char = queue.popleft()
      order.append(char)

      for neighbour in graph[char]:
         in_degree[neighbour] -= 1
         if in_degree[neighbour] == 0:
            queue.append(neighbour)

   return "".join(order) if len(order) == len(in_degree) else ""

# You are given a list of words sorted according to an unknown alien language.

# Example:

# ["wrt", "wrf", "er", "ett", "rftt"]

# Your task:

# Figure out the order of characters in the alien alphabet.
# Return a string representing one valid character ordering.
# If no valid ordering exists → return "".

# CONCEPT
# We're not translating anything, we're not re-sorting the words yourself
# We're using the fact that the words are already sorted to infer rules about the letters
# The sorted words are the clues, each time you compare two neighboring words, the first place they differ tells you which character must come earlier in the alien alphabet
# Nodes represent characters 
# Edges represent ordering constraints
# We use only the first differing character because once the first differing character is found, that is enough to determine the ordering rule between the two words
# An invalid scenario would be a longer word ("abc") appearing before its prefix ("ab")
# ordering is impossible so in this case we must return ""
# Even if a character has no dependencies it still belongs in the alphabet so it must appear in the final ordering. 


# We break in the loop because once you find the difference, we have already determined the order between the two words
# In lexicographic comparison, the first difference decides everything
# We should return "" for invalid prefix case where word2 starts with word1 and word1 is longer


# TIME COMPLEXITY 
# The time complexity of initialising graph and in_degree
# O(n x k)
# To build edges we compare adjacent words
# Up to n-1 comparisons
# Each comparison scans up to k characters
# The time complexity of building edges becomes O(n x k)
# BFS Topological Sort
# We process each character once –> O(u)
# Each edge once –> O(edges)
# edges <= u^2 but practically bounded by constraints from words
# BFS => O (u + edges)
# Final Time Complxity => O (n x k + u + edges)

# SPACE COMPLEXITY
# We store: 
# graph -> edges -> all unique characters and their edges
# in-degree –> u -> one entry per unique character
# queue –> up to u -> up to u characters
# order/result -> u -> up to u characters

# Final Space Complexity => O(u + edges)