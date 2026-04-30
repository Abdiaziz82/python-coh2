a = 4
b = 2
print(a + b)
print(a -b)
print ( a * b)
print( a / b)
# floor division
print( a // b)
print( a % b)

#comparison operators
print( a == b)
print (a != b)
print (a > b)
print (a < b)

# assignment operators
c = 55
c += 10
number = 10
number -= 4
print(number)
print(c)

#logical operators
print(a and b )
print( a or b)
print(not a)

user = "mohamed"
password = "hhhh"

if user or password:
    print("you are  allowed to log in")
else:
    print("you are not allowed to log in")


age = 18

if age >= 18:
    print("you are an adult")
else:
    print("you are not an adult")

def calculator():

    try:
        number1 = int(input("Enter the first number "))
        number2 = int(input("Enter the second number "))
        operation = input("Enter the operation  + , - , //, *  ")

        if operation == "+":
            print(number1 + number2)
        elif operation == "-":
            print(number1 - number2)
        elif operation == "*":
            print(number1 * number2)
        elif operation == "//":
            try:
                print(number1 // number2)
            except ZeroDivisionError:
                print("you cannot divide by zero")
        else:
            print("the operation is invalid")

    except ValueError:
        print("the input is not valid ensure you put valid input")

calculator()
