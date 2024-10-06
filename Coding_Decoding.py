# Secret_code
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
# else:
#   simply reverse the string
#   append three random characters at the starting and the end in both cases

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode


st= input("Enter the message ")
words= st.split(" ")
neword=[]
choice=input("Wanna Code or decode ")
if (choice =="code" ):
    for word in words:
     if(len(st)>=3):
        s1="hgg"
        s2="huf"
        newst=s1 + word[1:] + word[0] + s1
        neword.append(newst)
     else:
        newst=word[::-1]
        neword.append( newst)
elif(choice=="decode"):
    for word in words:
        if(len(st)<=3):
            newst=word[::-1]
            neword.append(newst)
        else:
           newst=word[3:-3]  
           newst= newst[-1]+newst[:-1] 
           neword.append(newst)
           
print(" ".join(neword))           

              

