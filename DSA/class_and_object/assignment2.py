# 1) define person class with instant object name and age set object veriable age and name display name and age

# class Person:
#     def __init__(self,name=None,age=None):
#         self.name = name
#         self.age = age

#     def setname(self,name):
#         self.name = name

#     def setage(self,age):
#         self.age = age

#     def show(self):
#         print("name:",self.name)
#         print("age :",self.age)


# Jhon = Person("Jhon",24)
# p1 = Person()
# p1.setage(26)
# p1.setname("Rebal")
# p1.show()
# Jhon.show()


# 2) 

class Cricle:
    def __init__(self,radius=None):
        self.radius = radius
    
    def set_radius(self,radius=None):
        self.radius = radius
    
    def get_radius(self):
        print(self.radius)

    def get_area(self):
        return (3.14 * (self.radius ** 2))
    
    def get_cricle_area(self):
        return(2 * 3.14 * self.radius)
    
area1 = Cricle(25)
area2 = Cricle()
area2.set_radius(45)


print("area 1 :",area1.get_area())
print("area 1 cricle area",area1.get_cricle_area())
print(area2.get_area)
print(area2.get_cricle_area())