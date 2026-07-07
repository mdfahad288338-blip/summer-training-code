class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


class teacher(person):
    def __init(self,name,age,subject):
     super().__init__(name,age)
     self.subject = subject

class principal(teacher):
    def __init__(self,name,age,subject,school):
        super().__init(name,age,subject)
        self.schoolname=school

    def display(self):
      print("Name:",self.name)
      print("Age:",self.age)
      print("Subject:",self.subject)
      print("School:",self.schoolname)

p1 = principal("fahad",20,"Math","SBBP")
p1.display()

