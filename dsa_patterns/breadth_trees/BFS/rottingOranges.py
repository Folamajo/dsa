

# PATTERN RECOGNITION
# Rotting oranges is best classified as Multi source BFS
# Because rotting spreads simultaneously from all rotten oranges
# We must also track the number of fresh oranges
# One full level of BFS represents One minute
# One rotten orange can spread rot 4 directions (up, down, left, right)
# We increment the minutes counter after processing one full BFS level
# If some oranges remain we should return -1
