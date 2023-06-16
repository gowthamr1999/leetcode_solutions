v = ["dog","eoe","fows"]
ans=""
v=sorted(v)
first=v[0]
last=v[-1]
for i in range(min(len(first),len(last))):
    if(first[i]!=last[i]):
        break
    ans+=first[i]
print(ans)