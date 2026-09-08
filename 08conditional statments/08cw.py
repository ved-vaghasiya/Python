# #########################################CONITIONAL STATEMNTS#####################################################################################
# result=float(input("enter your result :"))
# if(result>=33):
#     print("pass")
# else:
#     print("fail")    


# number=int(input("Enter a number:"))

# if number%2==0:
#     print("number is even!!! ")

# if number%2==1 :
#     print("number is odd !!!!")

# age=int(input("enter your age:").split()[0])
# gender=input("enter your gender")
# gender=gender.lower().strip()
# print(age,gender)

# if age >= 18 :
#     if gender=="male":
#         print("Seat is available for you!!!!")

# if gender != "male":
#     print("seat is unavilable for you !!!!!!")


# if gender=="male":
#         print("Seat is available for you!!!!")

# else:
#     print("seat is unavilable for you!!!1")    


# username=input("enter your name:")
# password=input("enter your password")

# if username  == "Ved Vaghasiya":
#       if password == "123456789":
#             print("you are login")

# if password != password:
#       print("password is wrong")            

       

# else:
#       print("wrong credintials"


#example.......
# marks = int(input("Enter Your Marks:"))

# if marks > 90 :
#     print("your grade is A")

# elif marks > 80 and  marks< 90 :
#     print("your grade is B")

# elif marks > 70 and marks <80 :
#     print("your grade is C")

# else:
#     print("you are fail , better lucj next time")


a=int(input("enter your number a :"))
b=int(input("enter your number b :"))

print("You have following ;\n 1.Addtion\n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Floor division ")

y=int(input("select your operaton"))
if y==1:
    print(a+b)
elif y==2:
    print(a-b)

elif y ==3:
    print(a*b)

elif y==4:
    print(a/b)

elif y==5 :
    print(a//b)

else:
    print("please enter valid number")

       