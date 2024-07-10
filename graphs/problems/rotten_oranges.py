# -----------------------------------------
# number of connected components in a graph
# -----------------------------------------
# https://www.youtube.com/watch?v=yf3oUhkvqA0&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=10
# -----------------------------------------
# input
# -----------------------------------------

# 3 3
# 2 1 1
# 1 1 0
# 0 1 1 

# 4 4
# 0 1 0 1
# 0 0 2 0
# 0 1 0 0
# 1 0 0 1
# -----------------------------------------
# output
# -----------------------------------------
# 4

# 0
# -----------------------------------------


def main():
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    

    def dfs(i, j, depth):
        nonlocal maxi_depth

        if (i<0 or i>n-1) or (j<0 or j>m-1) or visited[i][j] or graph[i][j] == 0:
            return
        
        visited[i][j] = True
        
        if graph[i][j] == 1:
            graph[i][j] = 2 
            maxi_depth = max(maxi_depth, depth)

        if graph[i][j] == 2:
            print(graph)
            dfs(i+1, j, depth+1)
            dfs(i-1, j, depth+1)
            dfs(i, j-1, depth+1)
            dfs(i, j+1, depth+1)

    visited = [[False]*m for _ in range(n)]
    maxi_depth = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                dfs(i, j, 0)
    
    print(maxi_depth)



if __name__ == "__main__":
    main()



