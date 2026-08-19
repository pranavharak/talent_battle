st = "luffy is still joyboy"
result = []
# i = 0
# while i < len(st):
#     if st[i]==' ':
#         i+=1
#         continue
    
#     j = i
#     st2 = ""
#     while j<len(st) and st[j]!=" ":        
#         st2 = st2 + st[j]
#         j+=1

#     result.append(st2)
#     i = j
cnt = 0
last = 0
for i in range(len(st)):
    if st[i] == " ":
        if cnt > 0:
            last = cnt
            result.append(cnt)
        cnt = 0
        continue
    else:
        cnt+=1

if cnt > 0:
    last = cnt
 

print(last)