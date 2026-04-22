strs=['bat','cat','rat','mat']
res=""
strs.sort()
first=strs[0]
last=strs[-1]
for i in  range(len(first)):
    if i< (len(first)) and first[i]==last[i]:
     res=res+first[i]
else:
    print(res)
    
