Buổi 8: Truy vấn dữ liệu từ nhiều bảng
- Chữa BTVN
- join
- with, Union:

1. INNER JOIN: 
- Mô tả: Dùng để lấy dữ liệu từ hai bảng, chỉ trả về các hàng có giá trị khớp trong cả 2 bảng
- Cú pháp:
SELECT table1.col1, table2.col2
FROM table1
INNER JOIN table2
ON table1.sharedCol = table2.sharedCol;

- Ví dụ: Lấy danh sách học sinh và các khóa học mà họ đang tham gia
SELECT Students.name, Courses.course_name
FROM Students
INNER JOIN Courses
ON Students.course_id = Courses.course_id;


2. LEFT JOIN (LEFT OUTER JOIN):
- Mô tả: Trả về tất cả dữ liệu từ bảng bên trái và các bản ghi khớp từ bảng bên phải, nếu không có bản ghi nào khớp sẽ trả về NULL.
- Cú pháp: 
SELECT table1.col1, table2.col2
FROM table1
LEFT JOIN table2
ON table1.sharedCol = table2.sharedCol;

- Ví dụ: Lấy danh sách tất cả học sinh và các khóa học, kể cả những học sinh không tham gia khóa học nào.
SELECT Students.name, Courses.course_name
FROM Students
LEFT JOIN Courses
ON Students.course_id = Courses.course_id;


3. RIGHT JOIN (RIGHT OUTER JOIN):
- Mô tả: Trả về tất cả dữ liệu từ bảng bên phải và các bản ghi khớp từ bảng bên trái, nếu không có bản ghi nào khớp sẽ trả về NULL.
- Cú pháp: 
SELECT table1.col1, table2.col2
FROM table1
RIGHT JOIN table2
ON table1.sharedCol = table2.sharedCol;

- Ví dụ: Lấy danh sách tất cả khóa học và những học sinh tham gia, kể cả những khóa học không có học sinh tham gia.
SELECT Students.name, Courses.course_name
FROM Students
RIGHT JOIN Courses
ON Students.course_id = Courses.course_id;


4. FULL JOIN (FULL OUTER JOIN):
- Mô tả: Kết hợp của cả LEFT/ RIGHT JOIN. Trả về tất cả dữ liệu từ cả hai bảng, với các bản ghi không khớp sẽ được trả về NULL.
- Cú pháp:
SELECT table1.col1, table2.col2
FROM table1
FULL JOIN table2
ON table1.sharedCol = table2.sharedCol;

Ví dụ: Lấy danh sách tất cả học sinh và tất cả khóa học, dù học sinh không tham gia hay khóa học không có học sinh.



///////////////
5. WITH (Common Table Expression - CTE):
- Mô tả: Dùng để định nghĩa một truy vấn phụ (subquery) tạm thời, giúp cải thiện sự rõ ràng và tối ưu hiệu năng khi làm việc với truy vấn phức tạp.
- Cú pháp: 
WITH Ten_alias AS (
    SELECT col FROM table WHERE condition
)
SELECT * FROM Ten_alias;

- Ví dụ: Lấy tất cả học sinh có điểm >  8;
WITH HighGrades AS (
    SELECT Name, Grade
    FROM Students
    WHERE Grade > 8
)

SELECT * FROM HighGrades;