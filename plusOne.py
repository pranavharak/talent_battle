digit = [9]
n = digit[0]
if len(digit)>=1:
    for i in range(1,len(digit)):
        n = n * 10
        n = n+digit[i]
n = n+1
result = []
while n !=0:
    rem = n %10
    result.append(rem)
    n = n //10
result.reverse()
print(result)