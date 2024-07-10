# -----------------------------
# input
# -----------------------------
# [4,3,7,1,2]
# -----------------------------
# -----------------------------
# output
# -----------------------------
# 4
# -----------------------------


# time complexity: O(nlogn) + O(n) = O(nlogn)
# space complexity: O(1)

def shortest_jobs(jobs):
    jobs.sort() # time: O(nlogn)
    total_time = 0

    local_sum = 0
    for i in range(len(jobs)-1): # time: O(n)
        local_sum += jobs[i]
        total_time += local_sum
    
    print(total_time// len(jobs))


if __name__ == "__main__":
    jobs = list(map(int,input().split()))
    shortest_jobs(jobs)
    