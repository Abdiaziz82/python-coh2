class Student:
    """  this is a class student it has name, age and grade attributr """
    #class attribute
    university = "Garissa university"
    all_students = []
    total_students = 0


    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self._grade = grade 
        Student.register_student(self)

    def display_self(self):
        return self.name
    
    @classmethod
    def register_student(cls,student):
        cls.all_students.append(student)
        cls.total_students += 1

    @classmethod
    def count_students(cls):
        return cls.total_students

    @classmethod
    def list_all_students(cls):
        for student in cls.all_students:
            print(f"{student.name}")



    @classmethod
    def update_university(cls,new_university):
        cls.university = new_university
        print(f"class is {cls}")

        return f"university updated to {new_university}"

    
    def __eq__(self,other):
        return self.name == other.name \
            and self.age == other.age and self.grade == other.grade
    
    def __str__(self):
        return f"the student name is {self.name} and the age is {self.age} and has grade {self.grade}"
    def get_grade(self):
        print("getting the grade")
        return self._grade
    
    def set_grade(self,grade):
        print("setting the grade")
        if grade not in ["A","B","C","D"]:
            print("this is invalid grade")
        else:
            self._grade = grade
    


student_1 = Student("abdi" ,"22" ,"B")
student_2  = Student("halima" ,"42" ,"C")
student_3  = Student("samatar" ,"22" ,"A")

print(Student.update_university("Meru University"))

print(Student.university)
print(Student.count_students())

Student.list_all_students()




# print(student_1)
# student_2.university = "MKU"
# student_2.grade = "F"
# print(student_2.grade)
# del student_2.grade
# print(Student.__doc__)







# print(student_2.university)

# is_equal = student_1 == student_2
# print(is_equal)

# print(student_1.name)
# print(Student.name)
# print(student_1.grade)
# print(student_2.age)
# print(student_1.display_self())

# # print(student_1.name)
# # print(dir(Student))

# my_name = "Ali"
# print(type(my_name))
# print(dir(my_name))

# print(dir(str))
# print(type(student_1))
# print(dir(student_1))
# print(my_name.isnumeric())