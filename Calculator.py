# Program make a simple calculator that can add, subtract, multiply and divide using functions
# William Quintero
# Sistemas distribuidos 2022
# define functions
def sum(x, y):
   """This function adds two numbers"""

   return x + y

def rest(x, y):
   """This function subtracts two numbers"""

   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""

   return x * y

def divide(x, y):
   """This function divides two numbers"""

   return x / y

# take input from the user
print("Seleccione su opcion.")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", sum(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", rest(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")