
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def __str__(self) -> str:
        return f"{self.name} : {self.marks}"
        
obj1 = student("Gaurav",90)
obj2 = student("Vison",70)

l = [27,2,4,67,5,2]
print(l)
l.sort()
print(l)