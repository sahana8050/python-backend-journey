print("second maximum value")
arr = [2, 3, 4, 55, 22]

max_value=arr[0]
second_max=arr[0]

for x in arr:
    if x>max_value:
        second_max=max_value
        max_value=x
    elif x > second_max and  x != max_value :
         second_max=x
print(second_max)

