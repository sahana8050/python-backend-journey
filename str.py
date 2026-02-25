##in python strings are immutable means non changeble if we want to change they will allocated in another memory not replace current path
#example for immutable str in python
             #str="sahana"
             #str[0]= "R"
             #print(str)

print("length of string is :")
str="sahana R"
str=len(str)
print(str)

print("get length of array:")
arr=[]
arr=len(arr)
print(arr)


print("length of char array:")
char_array=['s','a','h','a','n','a']
length=len(char_array)
print(length)


print("length of string:") #here allocation array is like |s | a| h| a| |n | a| inside one one byte index  will allocates
str="sahana"
Length=len(str)
print(Length)

print("count the index using for loop:")
s="sahana"
index=0
for numbers in s:
 print(index,numbers)
 index+=1


print("using while loop")
n="sahana"
index=0
while index<len(n):
 print(index,n[index])
 index+=1






 
 
 

















        
        
    



