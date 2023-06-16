class Student:
    school = 'Gowtham'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        avg1=(self.m1 + self.m2 + self.m3)/3
        return avg1

s1 = Student(1,2,3)
s2 = Student(3,4,5)

print(s1.avg())
print(s2.avg())