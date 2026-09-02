a="we are in swaminarayan \n university kalol \n ahmedabad"
print(a)

b= "python"
print(b[3])
print(b[-6])
print(b[:])
print(b[1:4])
print(b[0:])
print(b[-6:-2])
print(b[:4])
c=b[:]
print(c)
print(b[::-1])
print(b[0:6:2])
print(len(b))
print(len("ved"))

c= "j" +b[1:] #logic building
print(c) #STRINGS ARE INMUTABLE WE CAN NOT MODIFY LATER

#STRING METHODS ....
#1.UPPER
print(b.upper())
c="ved vaghasiya"
d=c[:3].upper()
e=c[3:].lower()
print(d+e)
#LOGIC BUILDING...........

#2.LOWER
print(b.lower())
#3.CAPITALIZE....
text="pYTHON pROGRAMING"
print(text.capitalize())

#4 TITLE.......
print(c.title())
#5 SWAP CASE.....
x="VeD VAgHASIYYA"
print(x.swapcase())

#6CASEFOLD .......
#example
y="Pyhton Programing "
print(y.casefold())

#SEARCHING IN STRINGS
#in....
print("v" in x)

#not in ...
print("v" not in x)

#index.....
text = "Hello Python"

print(text.index("Python"))

#find....
text = "Hello Python"

print(text.find("js"))

#startswith.......
text = "Python Programming"

print(text.startswith("Python"))


#endswith........

text = "Python Programming"
print(text.endswith("Programming"))

#Replacing Text'

text = "my name is dev"

new_text = text.replace("dev", "ved")

print(new_text)

d="hello Python"
e="pytHon"
f=e.lower() in d.lower()
print(f)


#WHITESPACE.....
#it is unessary space given to the left or right side of the string ,,,example:- " python programing " 
# :: the space given before the letter p and after the letter  g in programming is

# STRIP......
#strip() removes whitespace from both ends.

text= "  hello  "
print(text.strip())

#lstrip & rstrrip

#1.lstrip
#lstrip() removes whitespace from the left side.
text1="  hello"
print(text.strip())

#2.rstrip
#rstrip() removes whitespace from the right side.
text2="hello  "
print(text2.rstrip())

#. Escape Characters.......:-Escape characters are used to represent special characters inside strings.
#New Line
print("Hello\nWorld")

#tab...
print("hello\tworld")

#Double quote......
print("He said \"Hello\"")

#Single Quote
print('It\'s Python')