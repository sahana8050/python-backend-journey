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
