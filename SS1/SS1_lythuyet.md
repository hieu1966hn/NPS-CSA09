Khóa học CSA: 
- Lập trình hướng đối tượng?
- Xử lý, hệ thống dữ liệu với SQL, Pandas


Buổi 1: Giới thiệu về lập trình hướng đối tượng
- Lập trình hướng đối tượng OOP (Object - Oriented Programming): Tạo ra các đối tượng và trừu tượng hóa chúng.
- Ý bổ sung: Cách tiếp cận lập trình dựa trên việc sử dụng "đối tượng" và "lớp" để tổ chức và quản lý mã nguồn => Giúp dễ dàng quản lý các chương trình phức tạp bằng cách chia thành các đối tượng có thuộc tính và hành vi riêng.

- Lớp (class): Là bản thiết kế đối tượng, định nghĩa các thuộc tính (dữ liệu) và phương thức (hành vi) của đối tượng.
- Đối tượng (Object):  là một thực thể cụ thể của lớp. Đối tượng được tạo ra từ lớp và có thể có dữ liệu và hành vi riêng.
- Thuộc tính (Attributes): Là các biến được lưu trữ trong đối tượng. Mỗi đối tượng có các thuộc tính riêng được định nghĩa trong class.
- Phương thức (Methods): Là các hàm được định nghĩa bên trong lớp(class), mô tả các hành vi của đối tượng.



*Tính đóng gói (Encapsulation): Đảm bảo rằng các thuộc tính của đối tượng không thể bị truy cập trực tiếp từ bên ngoài, thường được thực hiện bằng cách sử dụng các thuộc tính "private".

Exp:
### Khởi tạo một bản thiết kế con người
class Person:
    ## Khởi tạo thuộc tính cho bản thiết kế này (class)
    def __init__(self, name, age):
        ## Gán giá trị cho kiểu dữ liệu
        self._name = name
        self._age = age




Bài luyện tập 2: Tạo 1 Car với các thuộc tính như model, color, year và phương thức display_info() để in ra thông tin của xe. Sau đó tạo một vài đối tượng của lớp Car và gọi phương thức display_info().



Bài luyện tập số 3: Tạo lớp BackAccount với các thuộc tính như: account_number và balance. Đảm bảo rằng chỉ có thể truy cập balance thông qua các phương thức deposit() và withdraw().



Bài luyện tập số 4: Quản lý học viên
Yêu cầu: Tạo lớp Student với các thuộc tính như: name, student_id, grades (danh sách các điểm số). Thêm phương thức calculate_average() để tính trung bình điểm và add_grade() để thêm điểm mới vào danh sách điểm số.