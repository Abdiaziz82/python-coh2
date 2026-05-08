class Student:
    #class attribute
    name = "abdiaziz"
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade 

    def display_self(self):
        return self.name

student_1 = Student("abdi" ,"22" ,"B")
student_2  = Student("MOhamed" ,"50" ,"F")
print(student_1.name)
print(Student.name)
print(student_1.grade)
print(student_2.age)
print(student_1.display_self())

# print(student_1.name)
# print(dir(Student))

my_name = "Ali"
print(type(my_name))
print(dir(my_name))

print(dir(str))
print(type(student_1))
print(dir(student_1))
print(my_name.isnumeric())