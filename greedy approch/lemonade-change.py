coins = [5, 5, 10, 10, 20]


def lemonade_check(coins):
    five = 0
    ten = 0
    for coin in coins:
        if coin == 5:
            five+=1
        elif coin == 10:
            ten+=1
            five-=1
            if five<0:
                return False
        else:
            if ten>0 and five>0:
                ten -= 1
                five -= 1
            elif five>2:
                five-=3
            else:
                return False
    
    return True

print(lemonade_check(coins))
