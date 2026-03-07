#

string1="car"
string2="CAR"

if len(string1)!=len(string2):
       print("false")
else:

 for i in range(len(string1)):
    char1=string1[i]
    char2=string2[i]
    if 'a'<=char1<='z':
        char1=ord(char1)-ord('a')
    elif 'A'<=char1<='Z':
        char1=ord(char1)-ord('A')
    

    if 'a'<=char2<='z':
        char2=ord(char2)-ord('a')

    elif 'A'<=char2<='Z':
        char2=ord(char2)-ord('A')

    

    if char1!=char2:
     print("False")
     
     
    else:
     print("True")
     break




