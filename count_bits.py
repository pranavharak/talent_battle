def binary(num):

    if num == 0:
        return 0

    cnt = 0
    
    while num>0:
        rem = num % 2
        if rem == 1:
            cnt +=1
        num = num // 2
    return cnt

print(binary(5))