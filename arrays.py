arr=[1,2,3,4,5] #printing list of numbers in parralel
print(arr)

print(arr[0]) #here arrays are counting from 0 not 1

arr.append(6) #adding new number to array using .aooend
print(arr)

arr.pop(4) #deleting item from array using .pop
print(arr)

for x in arr:
    print(x)
    
for x in arr:
    print(x, end=",") # \n is a new line


print("\n maximum value:") #printing maximum value
arr=[1,5,7,9,24]
max_value=arr[0]
for x in arr:
    if x>=max_value:
        max_value=x
print(max_value)


print("\n minimum value")
arr=[1,3,6,7,8]
min_value=arr[0]
for x in arr:
    if x<=min_value:
     mini_value=x
print(mini_value)


print("second largest number:")
arr=[5,1,9,3,97,8]
largest=arr[0]
second_largest=[-1]
for x in arr:
    if x>=largest:
        second_largest=largest
        largest=x
    elif x>=second_largest and x!=largest:
        second_largest=x
print(second_largest)



print(":")






