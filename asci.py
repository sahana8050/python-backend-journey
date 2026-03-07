#prove strings are true in incase sensitive in asci values 

string1="car"
string2="CAR"
index=0

for index in range(len(string1)):
    char1=string1[index]
    char2=string2[index]
    if len(string1)!=len(string2):
       print("false")
    else:
      print("True")
    exit()

    if 'a'<=char1<='z':
        char1=ord(char1)-ord('a')
    elif 'A'<=char1<='Z':
        char1=ord(char1)-ord('A')
    else:
     print("false")

    if 'a'<=char2<='z':
        char2=ord(char2)-ord('a')

    elif 'A'<=char2<='Z':
        char2=ord(char2)-ord('A')

    else:
     print("False")

    if char1!=char2:
     print("False")
     break
     
    else:
     print("True")




