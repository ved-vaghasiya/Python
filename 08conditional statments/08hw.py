#1.....
num=int(input("enter your number :"))

if num >10:
    print("number is greater than 10")

else:
    print("number is not greateer than 10")

age=int(input("enter your age !!!!!!!!!"))

#2......
if age >18 :
    print("you are adult")

#3...
number = int(input("enter your number first !!"))

if number >0 :
    print("number is positive ")

#4....
marks=int(input("enter your marks pls..."))

if marks >= 40 :
    print("crrongulations you are pass !!!")

#5.....
number = int(input("Enter a number: "))

if number == 0:
    print("Zero")


# 6. Positive or Not Positive

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
else:
    print("Not positive")


# 7. Adult or Minor

age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")


# 8. Even or Odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 9. Pass or Fail

marks = float(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# 10. Greater Number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
else:
    print(b, "is greater")



#C..
#11
marks=int(input("Enter your marks"))
if marks >= 90:
    print("your grade is A")

elif marks > 75 and marks < 89 :
    print("Your grade is B")    

elif marks > 40 and marks <59 :
    print("Your grades is C")

elif marks <40 :
    print("Your grade is D")

#13...
day=int(input("Enter your number that indicates days"))



if day == 1:
    print("Monday")

elif day ==2:
    print("Tuesday")

elif day ==3 :
    print("Wednesday")

elif day ==4 :
    print("Thursday")

elif day ==5 :
    print("Friday")

else:
    print("Invalid credintials")


#14....
marks=int(input("Enter your marks"))
if marks >= 90:
    print("your grade is A ,Excellent")

elif marks > 75 and marks < 89 :
    print("Your grade is B , Good")    

elif marks > 40 and marks <59 :
    print("Your grades is C , Pass")

elif marks <40 :
    print("Your grade is D , Fail")

#15.....
num = int(input("Enter a number: "))

if num == 1:
    print("1")
elif num == 2:
    print("2")
elif num == 3:
    print("3")
else:
    print("Other")


#D......
#16
age= int(input("enter your age :"))

if age >18 :
    if age <60 :
        print("you are adult")
else:
    print("you are kid!!")


#17..
marks=int(input("Enter your marks"))
if marks >= 90:
    print("your grade is A ,Excellent")

elif marks > 75 and marks < 89 :
    print("Your grade is B , Good")    

elif marks > 40 and marks <59 :
    print("Your grades is C , Pass")

elif marks <40 :
    print("Your grade is D , Fail")


#19.....
num=int(input("enter any number:"))

if num >0 :
    if num  > 100 :
        print("the num is greater than 100 and its positive")

else:
    print("the num is negative also less than 100")



#20.......

age= int(input("enter your age :"))

if age >18 :
    if age <60 :
        print("you are adult")
else:
    print("you are kid!!")

#21.....
num = int(input("Enter a number: "))

if num != 0:
    if num > 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")


#E......
#22...
age=int(input("Enter your age ::"))
marks=int(input("Marks your Marls:"))

if age >18 and marks>40 :
    print("you are eligible ")
else:
    print("you are not")    
   
#23.....
first_num= int (input("enter your first number :"))
second_num = int (input("enter your second number :"))

if first_num >10 and second_num >10:
    print("Both numbers are greater than 10")

else :
    print("Nope the are not both greater than 10") 

#24......
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

if first > 10 and second > 10:
    print("Both are greater than 10")

#25....

number = int(input("Enter a number: "))

if number < 0 or number > 100:
    print("Number is either less than 0 or greater than 100") 

           
#26.....
is_closed = False

if not is_closed:
    print("Open")


#27.....
number = int(input("Enter a number: "))

if number >= 10 and number <= 50:
    print("Number is between 10 and 50")


#28......
number = int(input("Enter a number: "))

if number < 10 or number > 50:
    print("Number is outside the range 10 to 50")

#29.....
is_student = True
has_id = True
has_ticket = True

if is_student and has_id and has_ticket:
    print("Allowed")

#30....
age=int(input("Enter your age :"))

if age >= 18 and marks >= 40 and has_id is True:
    print("Eligible")

else:
    print("not eligible")

    







    