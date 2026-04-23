nums=[1,1,2,3,4]
val=1
k=0
for i in range(len(nums)):
    if nums[i]!=val:
        nums[k]=nums[i]
        k=k+1
        print(nums[:k])