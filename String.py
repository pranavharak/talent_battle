s = "bb"
t = "ahbgdc"
st = ""
i =0
j = 0

while j <len(s):
    if s[j] == t[i]:
        st += t[i]
        j+=1
    i+=1
    if i == len(t):
        i = 0 
    
print(st)
if st == s:
    print("true")
else:
    print("false")