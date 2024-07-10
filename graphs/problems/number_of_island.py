# -----------------------------------------
# number of connected components in a graph
# -----------------------------------------
# https://www.youtube.com/watch?v=muncqlKJrH0&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=8
# -----------------------------------------
# input
# -----------------------------------------
# 1
# 5 4
# 0 1 1 0
# 0 1 1 0
# 0 0 1 0
# 0 0 0 0
# 1 1 0 1
# 4 4
# 0 1 0 1
# 0 0 1 0
# 0 1 0 0
# 1 0 0 1
# -----------------------------------------
# output
# -----------------------------------------
# 3
# 2
# -----------------------------------------





def main():
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    

    def dfs(i, j):
        if (i<0 or i>n-1) or (j<0 or j>m-1) or (visited[i][j]) or (graph[i][j]==0):
            return
        else:
            visited[i][j] = True
            # corner cases
            dfs(i+1,j+1)
            dfs(i-1,j-1)
            dfs(i+1,j-1)
            dfs(i-1,j+1)
            # side cases
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

    visited = [[False]*m for _ in range(n)]
    island_count = 0
    for i in range(n):
        for j in range(m):
            if (graph[i][j]==1) and (not visited[i][j]):
                dfs(i,j)
                island_count+=1
    
    print(island_count)



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        main()