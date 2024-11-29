Buổi 11: Truy xuất và xử lý dữ liệu với thư viện Pandas
- Ôn tập kiến thức
+ KDL: Series, DataFrame
+ to_csv(): Xuất dữ liệu ra file csv
+ read_csv() : Đọc dữ liệu từ file CSV
+ .dataFrame(): chuyển về kdl DF
+ info(): Tổng hợp thông tin về DF và các cột
+ dtypes: Kiểu dữ liệu từng cột
+ head()/tail(): Trả về 5 hàng đầu tiên/cuối cùng
+ dropna(): /...


- Truy xuất dữ liệu: 
+ Truy xuất dòng và cột từ DF (cách thông thường)
+ Truy xuất 1 cột: df['Name'] || df.Name
+ Truy xuất nhiều cột: df[['Name', 'Age']]
+ Truy xuất 1 hàng: df[1:2]
+ Truy xuất nhiều hàng: df[1:4] || df[1:]

Chú ý: 
- Nếu truy vấn là một dòng/ một cột thì kết quả trả về là một: Series
- Nếu truy vấn bao gồm nhiều hơn 1 dòng/ một cột thì kết quả là một: DF

**** Cú pháp truy vấn LOC và ILOC
- DF hỗ trợ thuộc tính loc & iloc để truy xuất dòng và cột. Cú pháp:
df.loc[<danh_sach_dong>, <danh_sach_cot>]
df.iloc[<danh_sach_dong>, <danh_sach_cot>]
- Mô tả: danh_sach_dong, danh_sach_dong có thể là
+ một dòng/ cột
+ một danh sách các dòng/ cột
+ Cú pháp list slicing: [<bắt đầu>: <kết thúc>]


Chi tiết:
loc[]
- Cú pháp: var_name.loc[row_label, col_label]
- Công dụng: Truy xuất dữ liệu dựa trên nhãn hàng và cột. Loc[] sử dụng nhãn để xác định hàng và cột.

iloc[]
- Cú pháp: var_name.iloc[row_index, col_index]
- Công dụng: Truy xuất dữ liệu dựa trên chỉ số hàng và cột. iloc[] sử dụng chỉ số (index) thay vì nhãn.