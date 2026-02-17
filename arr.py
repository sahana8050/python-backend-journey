arr=[1,5,7,9,24]
max_value=arr[0]
for x in arr:
    if x>=max_value:
        max_value=x
print(max_value)

print("second largest number:")
arr=[2,4,5,7,9,8]
largest=arr[0]
second_largest=arr[0]
for s in arr:
    if(s>largest):
        second_largest=largest
        largest=s
    elif(s>second_largest and s!=largest):
        second_largest=s
        print(second_largest)
