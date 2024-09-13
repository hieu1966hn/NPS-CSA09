### Tạo class Point.
# class Point:
#     ## Khai báo hàm khởi tạo
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     ## Viết phương thức
#     ### Cộng điểm hiện tại với một điểm khác
#     def add(self, point):
#         return Point(self.x + point.x, self.y + point.y)
    
#     ### Cộng điểm hiện tại với một điểm khác
#     def sub(self, point):
#         return Point(self.x - point.x, self.y - point.y)

#     ## Hiển thị tọa độ của điểm
#     def __str__(self): ## Phương thức này giúp định dạng đầu ra khi in một đối tượng Point.
#         ### Khi gọi hàm print(point1), phương thức này sẽ được tự động gọi ra để hiển thị theo định dạng
#         return f"({self.x}, {self.y})"

##### VÍ dụ
# point1 = Point(2, 3)
# point2 = Point(4, 5)

### Cộng 2 điểm trên
# print("Cộng 2 điểm point1 và point2", point1.add(point2))






#### Thực hành với kế thừa
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def make_sound(self):
#         return f"{self.name} makes a sound. "

### Tạo một loài động vật
# class Dog(Animal):
#     def __init__(self, name, species, breed):
#         ## Gọi lại hàm khởi tạo của lớp cha
#         super().__init__(name, species)
#         self.breed = breed
    
#     def make_sound(self):
#         return super().make_sound() + f"{self.name} barks"

# ### Tạo một loài động vật
# class Cat(Animal):
#     def __init__(self, name, species, breed):
#         ## Gọi lại hàm khởi tạo của lớp cha
#         super().__init__(name, species)
#         self.breed = breed
    
#     def make_sound(self):
#         return super().make_sound() + f"{self.name} meow"
    
# ### Sử dụng các lớp kế thừa đó
# max = Dog("Max", "Dog", "Chihuahua")
# min = Cat("Min", "Cat", "Tam thể")

# print(max.make_sound())
    


##### Kế thừa nhiều lớp
# class Bird:
#     def __init__(self, name):
#         self.name = name
    
#     def eat(self):
#         return f"{self.name} is eating"

# class Flyer:
#     def __init__(self, wing_span):
#         self.wing_span = wing_span
    
#     def fly(self):
#         return f"Flying with a wingspan of {self.wing_span} meters"


# class FlyingBird(Bird, Flyer):
#     def __init__(self, name, wing_span):
#         ## Gọi hàm khởi tạo của cả 2 lớp
#         Bird.__init__(self, name)
#         Flyer.__init__(self, wing_span)
    
#     def show_info(self):
#         return f"{self.name} can fly with a wingspan of {self.wing_span} meters"


# ### Sử dụng lớp FlyingBird
# eagle  = FlyingBird("Eagle", 2.5)

# print(eagle.eat())
# print(eagle.fly())
# print(eagle.show_info())



### Chữa bài luyện tập 1
# class Rectangle:
#     def __init__(self, lenght, width):
#         self.length = lenght
#         self.width = width
    
#     def area(self):
#         return self.length * self.width
    
#     def perimeter(self):
#         return (self.length + self.width) * 2

# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
    


## test HCN
# r = Rectangle(4, 5)
# print(r.area())

# s = Square(5)
# print(s.area())
# print(s.perimeter())


### Chữa bài luyện tập 2:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show_info(self):
        return f"Employe Name: {self.name}, Salary: {self.salary}"
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_info(self):
        return super().show_info() + f", Department: {self.department}"
    


m = Manager("Alan Walker", 8000, "HR")
print(m.show_info())