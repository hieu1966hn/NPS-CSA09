Buổi 2: Kế thừa trong lập trình hướng đối tượng (OOP)

- Kế thừa (Inheritance): Là một trong bốn nguyên lý cơ bản của lập trình hướng đối tượng. Kế thừa cho phép chúng ta tạo ra một lớp mới (gọi là subclass) dựa trên một lớp hiện có (gọi là lớp cha hoặc superclass). Lớp con thừa hưởng tất vả các thuộc tính và phương thức của lớp cha nhưng cũng có thể thêm hoặc ghi đè các thuộc tính và phương thức của riêng lớp con.

- Cú pháp: 
class LớpCon(LớpCha):
    def __init__(self, thuoc_tinh_cha, thuoc_tinh_con):
        # Gọi hàm khởi tạo của lớp cha
        super().init(thuoc_tinh_cha)
        self.thuoc_tinh_con = thuoc_tinh_con

    def phuong_thuc_con(self):
        .... ví dụ cụ thể bên code.

- super(): Được sử dụng để gọi hàm khởi tạo/ phương thức của lớp cha. Điều này giúp chúng ta không cần phải viết lại toàn bộ đoạn mã liên quan đến việc khởi tạo các thuộc tính chung giữa các lớp con.



Đề bài luyện tập 1: Tạo lớp Rectangle với các thuộc tính chiều dài (length) và chiều rộng (width). Tạo lớp con Square kế thừa từ Rectangle và mặc định chiều dài bằng chiều rộng.
Yêu cầu:
- Lớp Rectangle cần có phương thức tính diện tích area() và chu vi perimeter().
- Lớp Square chỉ cần truyền vào 1 tham số là cạnh của hình vuông.

 
Đề bài luyện tập 2: Viết lớp Employee với thuộc tính name và salary. Viết lớp Manager kế thừa từ Employee, thêm thuộc tính department.

Yêu cầu:
- Thêm phương thức để hiển thị thông tin nhân viên và quản lý



Đề bài luyện tập 3: Tạo lớp BankAccount với các thuộc tính như account_number và balance. Viết các phương thức deposit(), withdraw() và check_balance().

Yêu cầu: 
- Tạo lớp con SavingsAccount kế thừa từ BankAccount, thêm thuộc tính lãi suất (interest_rate). 
- Viết phương thức tính lãi dựa trên số dư hiện tại.