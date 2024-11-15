Buổi 10: Tìm hiểu về thư viện Pandas
- Cài đặt thư viện Pandas với cú pháp: pip install pandas
- Sử dụng thư viện với import 
- Giới thiệu: dataframe và series
- Giới thiệu các hàm đọc file của pandas();
- Các phương thức cơ bản của Pandas


Trong đó: 
- Series: Một cột (1 chiều): List
- Dataframe: Nhiều cột (2 chiều), tương tự như một dictionary vói key là tên cột và value là: Series

Giới thiệu các hàm đọc file của Pandas
1. read_csv(): đọc dữ liệu từ file CSV
Cú pháp: 
df = pd.read_csv('<ten_file>.csv')
print(df.head()) /// chỉ in 5 hàng đầu

2. read_excel(): đọc dữ liệu từ file Excel.
Cú pháp: 
df = pd.read_excel('<ten_file>.xlsx')
print(df.info()) /// chỉ in 5 hàng đầu

Chú thích:
- head(): Xem 5  dòng đầu của DF => df.head()
- info(): Xem thông tin chung về DF, bao gồm lượng dòng/cột và kiểu dữ liệu
- dtypes: Xem kiểu dữ liệu của từng cột trong DF

Xuất file CSV với hàm to_csv()
- Cú pháp:
df.to_csv('<ten_file_xuat>.csv', index=False)
- Mô tả: index=False loại bỏ cột chỉ mục khi xuất ra file


Đề bài: 
1. Tạo 1 DF chứa thông tin về tên, tuổi và điểm số của học sinh lớp "CSA09"
2. Đọc dữ liệu từ file CSV có sẵn (lát nữa làm)
3. Thực hiện thao tác xem trước dữ liệu với head(), xem kiểu dữ liệu dtypes và kiểm tra thông tin chung với info()
4. Xuất dữ liệu ra file CSV


Đề bài thực hành 2: 
1. Lấy dữ liệu từ bài 1, bổ sung thêm cột "Point2" CHỨA điểm CP2 của lớp
2. Tính điểm trung bình của mỗi học sinh và thêm cột mới vào DF
3. Hiển thị thông tin của học sinh có điểm trung bình cao nhất (nghiên cứu)

Đề bài số 3: Tính điểm TB của từng học sinh Dựa trên thang điểm
- Xuất dữ liệu file CSV có chứa DS học sinh và điểm CP1, CP2
- Đọc dữ liệu từ file CSV vừa xuất và xếp loại học sinh như điều kiện dưới đây:
- Giỏi: ĐTB >= 8
- Khá: 6.5 <= ĐTB < 8
- Trung bình: 5 <= ĐTB < 6.5
- Yếu: ĐTB < 5
- Xuất dữ liệu ra file CSV với cột xếp loại mới.

Đề bài số 4: Đọc dữ liệu từ 1 file CSV chứa thông tin bán hàng bao gồm các cột: Tên sản phẩm,
Số lượng bán, Đơn giá
- Loại bỏ các dòng dữ liệu có giá trị null (thiếu thông tin)
- Thêm một cột mới tên là "Tổng tiền" với công thưc:
Tổng tiền = Số lượng bán * Đơn giá.
- Xuất DF mới ra file CSV sau khi làm sạch
