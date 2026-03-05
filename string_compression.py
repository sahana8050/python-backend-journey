#string compession 
print("string compression:")
input_string="aaaabbc"
result=""
current_character=input_string[0]
count=1
index=1


while index < len(input_string):
   
   if input_string[index]==current_character:
      count = count+1

   else:
       result = result+current_character

       if count>1:
          result = result + str(count)

       current_character = input_string[index]
       count = 1

   index = index+1

result = result+current_character

if count>1:
   result = result + str(count)

print(result)
  



 
