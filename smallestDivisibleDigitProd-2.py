def digit(num):
    temp = []
    while num!=0:
        rem = num % 10
        num = num // 10
        temp.append(rem)
    return temp

num = "11111"
num = int(num)
flag = 1
while flag:
    result = digit(num)
    len_num = len(str(num))
    prod = 1
    print(f"{num}= {len_num}")
    for i in range(len(result)):
        prod *= result[i]   
    if prod != 0 and prod % 1968750 == 0:
        flag = 0
        print(num)
    else:
        num+=1

