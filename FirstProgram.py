#Basics:-

print("Hellow World")
print("Hi my Name is Aniket","and I'm 19 years old undergraguate student.")
print("My dateof Birth is :-","25/08/2005")
print("My Favourite number is",2255) #in this condition 0005 /(or) 02255 is not valid,means front 0 is not vallid 
print("My Favourite number is 0005")
print("My Favourite number is 2255")
print(9927)
print("Bhagyank:-",2+5+8+2+5,"and",2+2)
print("Mulank:-",2+5)
print(7*23)
print(23/4)
print(77-44)
print(44%2,"And",45%2)
print(7*23,23/4,77-44,44%2,"And",45%2)

#Note:- Python is Inplicit Typed Language
name = "Aniket" #string
age = 19 #int
Price = 25.990 #float
Birth = "25-08-2005"
old = False #Always F and T type in capital letter
Year = None
print(age,name,Price,Birth)
print(age,"and",name,"and",Price,"and",Birth)
print("My Birth Date is :-",Birth) 
age2 = Birth #2age is not vallid 
print(age2)
print(type(name))
print(type(age))
print(type(Price))
print(type(old))
print(type(Year))

#Extra
a = 5
b = 10
sum = a+b
print(sum)
print((b > a and "b>a") or (a > b and "a>b"))

#Extra
my_string = "Hellow, World!"
result = my_string[1:1:-1]
print(result)

#Extra
x = {}
y = [1,2]
z = [3,4]
print(x.fromkeys(y,z))

#Extra
"""from getpass import getpass
Username = input('Enter Username :')
password = input('Enter password :')"""

#Expression Execution Rules:-
#1.
A,B = 2,3
Txt = "@"
print(2*Txt*3)

#Conditional Statment Example
"""light = input("light :" )
if(light == "Red"):
    print("Stop")
elif(light == "Green"):
    print("Go")
elif(light == "Yellow"):
    print("Look")    
else:
    print("Light is Broken") """

marks = input("marks :") 
if(marks <= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")   
elif(marks >= 70 and marks < 80):
    print("C")  
else:
    print("D")      




    



