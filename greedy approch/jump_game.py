# --------------------------
# input
# --------------------------
# 2
# 1 2 4 1 1 0 2 5
# 1 2 3 1 1 0 2 5
# --------------------------
# output 
# --------------------------
# Yes
# No


def jump_game(jumps):
    maxi_jump = 0
    for i in range(len(jumps)):
        if i>maxi_jump:
            break
        maxi_jump = max(maxi_jump, i+jumps[i])
    
    if maxi_jump >= len(jumps)-1:
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        jumps = list(map(int,input().split()))
        jump_game(jumps)