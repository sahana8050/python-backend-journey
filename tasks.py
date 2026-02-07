print("10-20:")
for i in range(10,21):
    print(i)

print("odd number from 1 to 15:")
for i in range(1,16):
    if i%2==1:                             ## if i replace 0 in 1 place i wiil get even numbers
        print(i)

print("odd number from 1 to 15:")
for i in range(1,16,2):                   ## we can print odd and even numbers by taking steps (start,stop,step)
    print(i)                              #in step it consider that value to take step
