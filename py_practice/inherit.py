class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initializing SchoolMember : {0})'.format(self.name))
        
    def tell(self):
        print('Name:"{0}" Age:"{1}"'.format(self.name,self.age), end=" ")
        
class Teacher(SchoolMember):
    '''Represents a Teacher'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('(Initialized Teacher : {0})'.format(self.name))
        
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{0:d}"'. format(self.salary))
        
class Student(SchoolMember):
    '''Represents a Student'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student : {0})'.format(self.name))
        
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{0:d}"'.format(self.marks))
        
t = Teacher("Shiv",26,50000)
s = Student("Sam",18,80)

print()

members = [t,s]

for member in members:
    member.tell()