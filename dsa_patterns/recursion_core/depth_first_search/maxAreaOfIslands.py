def maxAreaOfIslands(grid: list[list[int]]):
   

# CONCEPT
# The main difference between Number of Islands and Max Area of Island ? We must compute the size of each connected component and track the max
# In number if islands DFS did not return anything it just sank the islands that we checked. Here we actually want to return the number of cells in the current island so that we can track the max.
# We receive the area from DFS and we update the max_area