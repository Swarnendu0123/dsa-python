# -----------------------------------------
# Flood fill algorithm
# -----------------------------------------
# https://www.youtube.com/watch?v=C-2_uSRli8o&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=9
# -----------------------------------------
# input
# -----------------------------------------
# 1
# 5 4
# 1 1 (starting position)
# 0 1 1 0
# 0 1 1 0
# 0 0 1 0
# 0 0 0 0
# 1 1 0 1
# 4 4
# 1 2 (starting position)
# 0 1 0 1
# 0 0 1 0
# 0 1 0 0
# 1 0 0 1
# -----------------------------------------
# output
# -----------------------------------------
# 0 2 2 0
# 0 2 2 0
# 0 0 2 0
# 0 0 0 0
# 1 1 0 1

# 0 2 0 1
# 0 0 1 0
# 0 1 0 0
# 1 0 0 1
# -----------------------------------------


def main():
    n, m = map(int, input().split())
    r, c = map(int, input().split())

    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    def dfs(i, j):
        if (i<0 or i>n-1) or (j<0 or j>m-1) or (visited[i][j]) or (graph[i][j] == 0):
            return 
        visited[i][j] = True
        graph[i][j] = 2
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
    
    visited = [[False]*m for _ in range(n)]
    dfs(r, c)

    for i in range(n):
        for j in range(m):
            print(graph[i][j], end=" ")
        
        print()
        


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        main()
