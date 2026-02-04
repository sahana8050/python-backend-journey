# printing 0-4 integers numbers
print("0 to 4:")
for i in range(5):
    print(i)


    ## printig 1-5 integers numbers
print("1 to 5:")
for i in range(1,6):
    print(i)


#printing even numbers
print("Event numbers:")
for i in range(2,11,  2):
    print(i)

 
 ## squaring  numbers
    print("squaring numbers:")
for i in range(5):
    print(i*i)

    
## if inside for loop
print("if insise for loop:")
for i in range(10):
    if i%2==0:
        print(i)

# break and continue in for loop
print("break in for loop")
for i in range(5):
    if i==6:
        break;
print(i)

print("continue in for loop")
for i in range(10):
    if i%2==0:
        continue
    print(i)
