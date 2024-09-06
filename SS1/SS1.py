# ### Khởi tạo một bản thiết kế con người
# class Person:
#     ## Khởi tạo thuộc tính cho bản thiết kế này (class)
#     def __init__(self, name, age):
#         ## Gán giá trị cho kiểu dữ liệu
#         self.name = name
#         self.age = age
    
#     ### Khởi tạo hành vi (phương thức)
#     def move(self):
#         print(f"{self.name} can move with 2 leg on the ground")

#     def greet(self):
#         print(f'Hello, my name is {self.name} and I am {self.age} years old')


# ### Khai báo 1 biến (đối tượng) là thực thể của lớp Person
# Hieu = Person("Nguyễn Trung Hiếu", 30)
# print(Hieu.name)      

# ### Gọi phương thức move & greet
# Hieu.move()
# Hieu.greet()



#### Chữa bài luyện tập 1
# class Counter:
#     def __init__(self):
#         self.count = 0
    
#     def tick(self):
#         self.count += 1
    
#     def reset(self):
#         self.count = 0


# counter1 = Counter()
# counter1.tick()
# counter1.tick()
# counter1.tick()
# counter1.reset()
# print(counter1.count)


#### Thực hành bài luyện tập số 2
# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year

#     def display_info(self):
#         print(f"Model: {self.model}, Color: {self.color}, Year: {self.year}")

# car1 = Car("Toyota Camry", "White", 2020)
# car2 = Car("Honda Civic", "Black", 2019)

# ## Gọi hàm hiển thị thông tin xe
# car1.display_info()
# car2.display_info()


#### Chữa bài luyện tập số 3: 

# class BackAccount:
#     ## Hàm khởi tạo thuộc tính
#     def __init__(self, account_number, balance = 0):
#         self.account_number = account_number
#         self._balance = balance ### Thuộc tính private

#     ### Phương thức truy cập
#     def deposit(self, amount):
#         self._balance += amount

#     def withdraw(self, amount):
#         if amount > self._balance: 
#             print("Insufficient funds")
#         else:
#             self._balance -= amount


# ### Tạo tài khoản và thực hiện giao dịch
# account = BackAccount("123456")
# # account.__balance = 1000 ### Về lý thuyết sẽ không hoạt động.
# account.deposit(500)
# account.withdraw(200)
# print(account._balance) ## Dự đoán kết quả: 300$



### Bài luyện tập số 4
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
    
    ## Thêm điểm và môn học để lưu trữ
    def add_grade(self, gade, subject):
        self.grades[subject] = gade
    
    ### Trung bình điểm số
    def calculate_average(self):
        ## Có bao nhiêu môn học có điểm?
        soMonHoc =  len(self.grades) ## number: 3
        diem = 0
        #### Xem kỹ vòng lặp này xem đúng chưa để mỗi lần lặp lấy ra được điểm của môn học tương ứng.
        # for i in self.grades.keys():
        #     diem =+ self.grades[i]
        return diem/soMonHoc


### Tạo một đối tượng học viên và thêm điểm
TrungHieu = Student("Nguyễn Trung Hiếu", "$12345")
TrungHieu.add_grade(8,"math")
TrungHieu.add_grade(8,"physics")
TrungHieu.add_grade(8,"chemistry")

print(TrungHieu.calculate_average())


    
