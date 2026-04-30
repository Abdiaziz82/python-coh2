def my_function():
    return "this is function"

message = my_function()
print(message)

student1_name = "abdiaziz"
student2_name = "AHMED"
student3_name = "halima"
#f-string
message = f"hello {student1_name}  welcome to the clASS"
message = f"hello {student2_name}  welcome to the clASS"
message = f"hello {student3_name}  welcome to the clASS"
print(message)

def greet_student(name ,email="user@gmail.com"):
    message = f"hello {name}  welcome to the clASS and your email is {email}"

    print(message)

greet_student("mohamed" )
greet_student("zamzam" , "zamzam@gmail.com")
greet_student("ali")

email = "student@gau.ac.ke"

def list_students(*args, **kwargs):
    print(kwargs)
    global email
    email = "halima@gmail.com"
    print(email)
    return f"the first student is {args[0]} and the second is  {args[1]} "
    

students = list_students("john" ,"doe" ,"musa" ,"fdghdh" , age = 23 , gender = "male")
print(students) 


