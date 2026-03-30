
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


# We break in the loop because once you find the difference, you have already determined the order between the two words
# In lexicographic comparison, the first difference decides everything
# We should return "" for invalid prefix case where word2 starts with word1 and word1 is longer