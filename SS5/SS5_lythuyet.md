Buổi 5: Giới thiệu về cơ sở dữ liệu 
1. Ôn tập kiến thức 
2. Hoàn thành dự án Snake
3. Tìm hiểu về Hệ quản trị cơ sở dữ liệu 

Dữ liệu: từ dữ liệu chúng ta có thể phân tích được các xu hướng, ..
- Dữ liệu có quan hệ: 
- Dữ liệu không quan hệ: JSON, graph, hash, 

Hệ thống quản trị dữ liệu (DBMS): Nơi tương tác giữa người dùng và dữ liệu.

==> Dữ liệu + Hệ thống quản trị dữ liệu = cơ sở dữ liệu

CSDL quan hệ: 
- Dữ liệu được biểu diễn thành các bảng gồm cột và dòng (hàng). Giống như bảng trong Excel.
- Mỗi dòng (một bộ/tuple) đại diện cho một đối tượng (mục thông tin). VD: Mỗi dòng có thể đại diện cho một học sinh trong lớp.
- Mỗi cột là một thuộc tính của đối tượng

- Tập hợp các bảng thì được gọi là: Một cơ sở dữ liệu quan hệ. Nhiều bảng kết nối với nhau qua các mối quan hệ => gọi nó là cơ sở dữ liệu quan hệ.

- Lược đồ quan hệ: Là cách mà các bảng trong CSDL được tổ chức và kết nối với nhau
- Khóa quan hệ: 
+ Khóa chính (Primary Key): Là cột hoặc nhóm cột giúp phân biẹt mỗi dòng trong bảng. VD: Trong bảng học sinh, "Mã học sinh" có thể là chìa khóa chính vì mỗi học sinh có một mã riêng.
+ Khóa ngoại (Foreign Key): Là cột kết nối 2 bảng lại với nhau. Nó thường là khóa chính từ bảng khác. VD: "Mã lớp" trong bảng học sinh có thể là khóa ngoại kết nối với bảng "Lớp học".

1. one - many relationship: Quan hệ một - nhiều
2. many - many relationship: Quan hệ nhiều - nhiều
3. one - one relationship: Quan hệ một - một

Hệ quản trị cơ sở dữ liệu SQL: 
- Cài đặt MySQL
- Cài đặt MySQL workbench: Giao diện để thao tác. 
- Nghiên cứu cách kết nối giữa: MySQL -> MySQL workbench

- Giới thiệu các kiểu dữ liệu trong SQL: INT, VARCHAR, BINARY, DATE, TIMESTAMP,...