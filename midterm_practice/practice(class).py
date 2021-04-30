class Person:           #parent class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):  #child class
    def __init__(self, fname, lname, year):  #add property
        super().__init__(fname, lname)
        self.graduationYear = year
    
    def welcome(self):
        print("welcome", self.firstname, self.lastname, 'to the class of',self.graduationYear)

x = Person("Yehyun", "Suh")
x.printname()
y = Student('andy','ng',2021)
y.welcome()

#############################################################

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Object method in a class. Use def within a class.
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Jiyoung", 24)
p1.myfunc()
