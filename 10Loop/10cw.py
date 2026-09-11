
# for i in range(888):
#     print("ved vaghasiya 💀",end="")
# num=int(input("enter your number::"))
# for i in range (0,num+1):
#     if i%2==0:
#         print(f"{i} is even")
#     elif i%2 !=0:
#         print(f"{i} is odd")


# for i in range(10,0,-1):
#     print(i)


str=input("Enter a string :").strip().lower()
str2=""
length=len(str)
for i in range(length-1,-1,-1):
    print(str[i])
    str2=str2+str[i]  

if str2==str :
    print("palandrom")

elif str2!=str:
    print("not a palandrom")

# else:
#     print("invalid credentials or special characteer used")

   