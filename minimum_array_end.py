x = 1
result = [x]
j = x+1
while len(result)!=4:
    if x &  j == x:
        result.append(j)
        j+=1
    else:
        j+=1

print(result)