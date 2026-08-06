def smallestNumber(n, t):
        
    flag = 1
    while flag:
        digits = digit(n)
        prod = 1
        for i in range(len(digits)):
            prod *= digits[i]
        
        if prod % t == 0:
            flag = 0
            return n
        else:
            n+=1



def digit(x):
    temp = []
    while x!=0:
        rem = x % 10
        temp.append(rem)
        x = x // 10
    return temp

print(smallestNumber(1,1))