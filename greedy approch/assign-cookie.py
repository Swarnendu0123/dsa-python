# https://www.youtube.com/watch?v=DIX2p7vb9co&list=PLgUwDviBIf0rF1w2Koyh78zafB0cz7tea&index=1
greed = [1,5,3,3,4]
cookie = [4,2,1,2,1,3]

# greed 1 3 3 4 5
# cookie 1 1 2 2 3 4


def asign_cookie(greed, cookie):
    r = 0; l = 0
    m = len(greed); n = len(cookie)
    greed.sort()
    cookie.sort()
    while (r<m and l<n):
        if greed[r]<=cookie[l]:
            r+=1
        l+=1
    
    return r


print(asign_cookie(greed, cookie))

