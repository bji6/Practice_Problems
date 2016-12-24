def recursivePathRun(grid, cur_x, cur_y, num_rows, num_cols, path_size, min_path):
    #print("current Path size %d" % path_size)
   # print ("y = %d" % cur_y)
    #print ("x = %d" %  cur_x)
    #print(num_rows)
   # print(num_cols)
    
    # if we went too far in one direction return empty
    if (cur_x == num_cols or cur_y == num_rows):
        return 999999999
    # we reached end of path, add pathsize to list and return
    elif ((cur_x == (num_cols - 1)) and (cur_y == (num_rows - 1))):
        #print("found path, returning!")
        #print(path_size)
        return path_size

    # move right
    if (cur_x + 1 < num_cols):
        path_size_x = path_size
        path_size_x += grid[cur_y][cur_x + 1]
        if (min_path > path_size_x):
            path_size_x = recursivePathRun(grid, cur_x + 1, cur_y, num_rows, num_cols, path_size_x, min_path)
            min_path = min(min_path, path_size_x)
    # move down
    if (cur_y + 1 < num_rows):
        path_size_y = path_size
        path_size_y += grid[cur_y + 1][cur_x]
        if (min_path > path_size_y):
            path_size_y = recursivePathRun(grid, cur_x, cur_y + 1, num_rows, num_cols, path_size_y, min_path)
            min_path = min(min_path, path_size_y)

    return min_path


class Solution(object):
    
    
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
       # print(grid)
        num_rows = len(grid)
        
        if (num_rows < 1):
            return 0
        
        num_cols = len(grid[0])
        #print("num rows %d" % num_rows)
        #print("num cols %d" % num_cols)
        
        min_size = recursivePathRun(grid, 0, 0, num_rows, num_cols, grid[0][0], 999999999)

        print("done recursion, %d" % min_size)
        return min_size

def main():
    test = Solution()

    grid = [[5,0,1,1,2,1,0,1,3,6,3,0,7,3,3,3,1],[1,4,1,8,5,5,5,6,8,7,0,4,3,9,9,6,0],[2,8,3,3,1,6,1,4,9,0,9,2,3,3,3,8,4],[3,5,1,9,3,0,8,3,4,3,4,6,9,6,8,9,9],[3,0,7,4,6,6,4,6,8,8,9,3,8,3,9,3,4],[8,8,6,8,3,3,1,7,9,3,3,9,2,4,3,5,1],[7,1,0,4,7,8,4,6,4,2,1,3,7,8,3,5,4],[3,0,9,6,7,8,9,2,0,4,6,3,9,7,2,0,7],[8,0,8,2,6,4,4,0,9,3,8,4,0,4,7,0,4],[3,7,4,5,9,4,9,7,9,8,7,4,0,4,2,0,4],[5,9,0,1,9,1,5,9,5,5,3,4,6,9,8,5,6],[5,7,2,4,4,4,2,1,8,4,8,0,5,4,7,4,7],[9,5,8,6,4,4,3,9,8,1,1,8,7,7,3,6,9],[7,2,3,1,6,3,6,6,6,3,2,3,9,9,4,4,8]]

    test.minPathSum(grid)

main()