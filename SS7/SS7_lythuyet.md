Buổi 7: Các hàm có sẵn trong SQL
- C, U, D

C: Create
CREATE DATABASE ten_database: Tạo cơ sở dữ liệu (DB)

USE ten_database: Chọn csdl để sử dụng

CREATE TABLE ten_bang (...): Tạo bảng mới trong cơ sở dữ liệu

INSERT INTO ten_bang (cot1, cot2, ...) VALUES (gia_tri1, gia_tri2, ...); Thêm dữ liệu vào bảng

R: Read
SELECT cot1, cot2, ... FROM ten_bang; Để lấy dữ liệu từ bảng

U: Update
UPDATE ten_bang SET cot1 = gia_tri_moi WHERE dieu_kien; Cập nhật dữ liệu trong bảng

D: Delete
DELETE FROM ten_bang WHERE dieu_kien;

//////
ALTER TABEL ten_bảng ADD cot_moi kieu_du_lieu ; Thêm cột vào bảng

ALTER TABEL ten_bảng DROP COLUMN ten_cot; Xóa cột khỏi bảng

DROP TABLE ten_bang; Xóa bảng

DROP DATABASE ten_database; Xóa cơ sở dữ liệu





Lệnh SQL 

CREATE DATABASE CSA09;

USE CSA09;

CREATE TABLE Students (
	StudentID INT PRIMARY KEY,
	Name VARCHAR(50),
    Age INT, 
    Grade VARCHAR(10),
    City VARCHAR(50)
);

INSERT INTO Students (StudentID, Name, Age, Grade, City)
VALUES
(1, 'Tùng Lâm', 16, "B", "Hà Nội"),
(2, 'Đông Du', 17, "B", "Hà Nội"),
(3, 'Thế Vũ', 15, "A", "Hà Nội"),
(4, 'Phong', 17, "C", "Hà Nội"),
(5, 'Khánh', 15, "F", "Hà Nội");