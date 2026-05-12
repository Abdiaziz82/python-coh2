
# parent/superclass
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f" hello {self.name}"
    
    def __str__(self):
        return f"this person is {self.name}"
    
#child /subclass
class Student(Person):
    
    def __init__(self, name, age ,marks,grade):
        super().__init__(name,age)
        self.marks = marks
        self.grade = grade
        
    def study(self):
        return f"{self.name} is studying"
    
    
#grandchilld
class ScholarshipStudent(Student):
    def __init__(self,name,age,marks,grade,scholarship_amount):
        super().__init__(name,age,marks,grade)
        self.scholarship_amount = scholarship_amount
    
    def claim_scholar(self):
        return f"{self.name} is claiming {self.scholarship_amount}"
    



person_1 = Person("Abdi" ,33)
print(person_1)
print(person_1.greet())
student_1 = Student("halima " ,22 ,60 ,"B")
print(student_1)
print(student_1.greet())
print(student_1.study())

scholar_1 = ScholarshipStudent("Mohamed",22 ,90 ,"A" , 80000)
print(scholar_1.greet())
print(scholar_1.claim_scholar())
print(scholar_1.study())
    