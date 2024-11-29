import pandas as pd

### Data gốc
CSA09 = {
    'Name': ['Khánh','Du','Phong', 'Vũ', 'Lâm'],
    'Age': [15, 17, 17, 15, 16],
    'Point': [8, 9, 10, 9.5, 8]
}

### Tạo DF 
df = pd.DataFrame(CSA09)

### yc1: Truy xuất tuổi của học sinh đứng thứ 2 trong danh sách
# print(df['Age'][1])

### yc2: Truy xuất cột 'tên' và 'điểm số' từ DF học sinh
# print(df[['Name', 'Point']])

### yc3: Truy xuất tất cả học sinh có điểm số lớn hơn 8.5
# print(df['Point'] > 8.5)

### yc4: Truy xuất học sinh có tên là 'Khánh' và lấy điểm số của bạn đó
# print(df.loc[df['Name'] == 'Khánh', 'Point'])

### yc5: Truy xuất tên và tuổi của học sinh thứ 3 trong DF
# print(df.iloc[2, [0, 1]])


### yc6: Lọc học sinh có Age = 17 và Point = 10
# print(df[(df['Age'] == 17) & (df['Point'] == 10)])

### yc7: Sắp xếp theo điểm số giảm dần
# print(df.sort_values(by='Point', ascending=False))

### yc8: Tính điểm trung bình của tất cả học sinh trong lớp: mean()
# print(df['Point'].mean())

### yc9: Thêm cột 'Pass' với giá trị "Pass" nếu Point > 8, ngược lại là "Fail"
# df['Pass'] = df['Point'].apply(lambda x: 'Pass' if x > 8 else 'Fail')
# print(df)