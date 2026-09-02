#part 3..........
#task1.........
name="ved vaghasiya"
city="surat"
favourite_programing_language="python"
message="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis nat"
print(name)
print(city)
print(favourite_programing_language)
print(message)

#task2....
empty=""
print(type(empty))
print(len(empty))

#task3...
text = "Python Programming"

print("Complete string:", text)
print("Length:", len(text))
print("First character:", text[0])
print("Last character:", text[-1])
print("Third character:", text[2])
print("Second-last character:", text[-2])

#part 4 ...........
#task4....
text1="Programming"
print(text[0])
print(text[2])
print(text[5])
print(text[10])

#task5...
text1="Programming"
print(text[-1])
print(text[-2])
print(text[-3])
print(text[-10])

#task6......
name = "Ved Vaghasiya"

print( name[0])
print( name[-1])
print( name[4])


#Part5........
#task7.......
text = "Python Programming"

print("Python:", text[0:6])
print("Programming:", text[7:18])
print("Complete string:", text[:])
print("First 5 characters:", text[:5])
print("Last 5 characters:", text[-5:])


text1="ABCDEFGHIJKL"
print(text1[0:12:2])
print(text1[0:12:3])
print(text1[1:8:2])
print(text1[::-1])

#task9.....
string = "Python Programming"

print("Last 5 characters:", string[-5:])
print("Last 10 characters:", string[-10:])
print("Reverse string:", string[::-1])

#task 10.......
a = "Programming"

print(a[:3])
print(a[-3:])
print(a[::2])
print(a[::-1])
print(a[1:-1])

#Part 6.......
#task 11.......

print(len(text1))
print(len(message))
print(len(message))


#task12
print(len(text))

#Part7......
#task13........
first_name = "Ved"
last_name = "Vaghasiya"

print(first_name + " " + last_name)

#task14.........
name = "Ved"
age = 18
city = "Ahmedabad"
language = "Python"

print("My name is " + name + ". I am " + str(age) + " years old and I live in " + city + ". I am learning " + language + ".")


#task15.......
a = "Age: "
b = 18

# print(a + b)

print(a + str(b))

#part8
#task16....
a = "#"

print(a * 3)
print(a * 5)
print(a * 10)

#task17
print(a*10)

#part9
#Task18
#task18

a = "python programming language"

print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.swapcase())

#task19

a = "Python"
b = "python"

print(a == b)

print(a.lower() == b.lower())

#part10....

#task20

a = "Python is a programming language"

print("Python" in a)
print("programming" in a)
print("Java" in a)
print("language" in a)


#task21

b = "Python is a programming language"

print(b.find("Python"))
print(b.find("programming"))
print(b.find("language"))
print(b.find("Java"))


#task22

c = "Python is a programming language"

print(c.index("Python"))
print(c.index("programming"))
print(c.index("language"))



#task23

d = "banana"

print(d.count("a"))
print(d.count("n"))
print(d.count("b"))


#task24

e = "student_notes.pdf"

print(e.startswith("student"))
print(e.endswith(".pdf"))
print(e.endswith(".txt"))


#part 11
#task 25 ......

text2 ="I am learning Java"
print(text2.replace("Java","Python"))

#task 26
text3 = "apple apple apple"
print(text3.replace("apple", "mango"))

#task28

text = "Python"

text.upper()
print(text)

text = text.upper()
print(text)


#task29

text = "   Python Programming   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())


#task30

a = input()
a = a.strip()

print(a)


#task31

a = "Python is easy to learn"

print(a.split())


#task32

a = "apple,banana,mango,orange"

print(a.split(","))


#task33

words = ["Python", "is", "easy"]

print(" ".join(words))


#task34

words = ["Python", "is", "easy"]

print("-".join(words))
print("/".join(words))


#task35

name = "Ved"
age = 18
city = "Ahmedabad"

print(f"My name is {name}. I am {age} years old and I live in {city}.")


#task36

a = 10
b = 20

print(f"The sum is {a + b}")


#task37 A

text = "Python"

# print(text[20])
# IndexError: string index out of range

print(text[0])


#task37 B

text = "Python"

# text[0] = "J"
# TypeError: 'str' object does not support item assignment

text = "J" + text[1:]
print(text)


#task37 C

age = 20

# print("Age: " + age)
# TypeError: can only concatenate str (not "int") to str

print("Age: " + str(age))


#task37 D

text = "Python"

# print(text.index("Java"))
# ValueError: substring not found

print(text.find("Java"))









