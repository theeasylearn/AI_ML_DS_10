class Student:
    InstituteName = "THE EASYLEARN ACADEMY"
    def __init__(self,rollno,name):
        self.rollno = rollno 
        self.name = name 
    def display(self):
        print(f"Roll no {self.rollno} Name = {self.name}")

s1 = Student(100,"Kailash Prajapati")
s2 = Student(200,"Radha dave")
print(s1.InstituteName)
print(s2.InstituteName)
print(Student.InstituteName)

s1.display()
s2.display()
Student.InstituteName = "T.E.L"
print(Student.InstituteName)
