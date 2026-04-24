nums=[1,2,2,3,3,3,3,3]
count={}
res=0
maxCount=0
for i in nums:
    count[i]=count.get(i,0)+1
    if count[i]>maxCount:
        maxCount=count[i]
        res=i
print(res) 
