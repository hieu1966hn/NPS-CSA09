Buổi 6: Truy vấn và hàm trong SQL
1. Cài đặt mySQL 
2. Cài đặt SQL Workbench 


SELECT
- Công dụng: Dùng để chọn và truy xuất dữ liệu từ bảng.
- Cú pháp: SELECT ten_cot1, ten_cot2 

FROM
- Công dụng: Chỉ định bảng chứa dữ liệu cần truy vấn
- Cú pháp: FROM ten_bang

WHERE 
- Công dụng: Dùng để lọc dữ liệu theo điều kiện cụ thể.
- Cú pháp: WHERE ten_cot "=, >, <, ..." value

DISTINCT
- Công dụng: Loại bỏ các giá trị trùng lặp trong kết quả truy vấn
- Cú pháp: SELECT DISTINCT ten_cot FROM ten_bang;

AS
- Công dụng: Đặt tên mới (bí danh) cho cột hoặc bảng để dễ hiểu hơn.
- Cú pháp: Đặt tên cột Name là StudentName
SELECT Name AS StudentName, Age FROM Students;

LIKE
- Công dụng: Tìm kiếm dữ liệu khớp với mẫu ký tự
- Ví dụ: Tìm loại hoa có tên bắt đầu bằng chữ "R"
SELECT * FROM Flowers_table
WHERE Name LIKE 'R%';

BETWEEN
- Công dụng: Lọc dữ liệu trong một khoảng giá trị nhất định.
- Ví dụ: Lấy tất cả hoa có giá từ 20 - 25$
SELECT * FROM Flowers_table
WHERE Price BETWEEN 20 AND 25;

ORDER BY
- Công dụng: Sắp xếp kết quả truy vấn theo cột cụ thể.
- Ví dụ: Sắp xếp danh sách các loại hoa có giá tiền tăng dần.
SELECT * FROM Flowers_table
ORDER BY Price ASC;

- Ví dụ với giảm dần
SELECT * FROM Flowers_table
ORDER BY Price DESC;

LIMIT
- Công dụng: Giới hạn số lượng kết quả trả về.
- Ví dụ: Lấy ra 3 hoa đầu tiên trong bảng Flowers_table
SELECT * FROM Flowers_table
LIMIT 3;


Đề bài thực hành: 
1. Sử dụng câu lệnh SELECT, liệt kê tất cả tên học sinh và thành phố của họ.
2. Sử dụng WHERE để lọc danh sách học sinh có điểm Grade là "A".
3. Sử dụng DISTINCT để liệt kê các giá trị khác nhau trong cột Grade.
4. Sử dụng LIKE để tìm học sinh có tên chứa từ khóa "Lee".