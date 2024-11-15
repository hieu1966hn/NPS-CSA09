import pandas as pd


# Ví dụ 1 series
# s = pd.Series([1, 2, 3 ,4])
# print(s)


# Ví dụ 1 dataframe
# data = {
#     'Name': ['Khánh', "Lâm"],
#     'Age': [25, None]
# }
# df = pd.DataFrame(data)
# print(df)


# CSA09 = {
#     'Name': ['Khánh','Du','Phong', 'Vũ', 'Lâm'],
#     'Age': [15, 17, 17, 15, 16],
#     'Point': [8, 9, 10, 9.5, 8]
# }

## Tạo DF
# CSA09_DF = pd.DataFrame(CSA09)
# print(CSA09_DF.head())
# print(CSA09_DF.info())

### Xuất dữ liệu lớp học CSA09 ra file CSV
# CSA09_DF.to_csv('./SS10/CSA09_Students.csv', index=False)



### Chữa bài luyện tập 2
# CSA09 = {
#     'Name': ['Khánh','Du','Phong', 'Vũ', 'Lâm'],
#     'Age': [15, 17, 17, 15, 16],
#     'Point': [8, 9, 10, 9.5, 8]
# }

## Thêm một khóa Point2 vào dictionary
# CSA09['Point2'] = [1, 2, 3, 4, 5]
# print(CSA09)

## Tạo DF CSA09
# CSA09_DF = pd.DataFrame(CSA09)
# CSA09_DF['Average'] = (CSA09_DF['Point'] + CSA09_DF['Point2'])/2
# print(CSA09_DF)

### Học sinh có điểm trung bình cao nhất
# highest_avg_student = CSA09_DF['Average'].max()
# # print(highest_avg_student) ## 6.75
# for i in CSA09_DF:
#     # print(i) ## từng key
#     if i == "Average":
#         if CSA09_DF[i] == highest_avg_student:
#             print(CSA09_DF[i])
    # if CSA09_DF[i] == highest_avg_student:  
    #     print(CSA09_DF[i])



### Thực hành bài số 3:
# Xuất dữ liệu ra file CSV
# CSA09_DF.to_csv('./SS10/CSA09_Info.csv', index=False)

### Đọc dữ liệu từ file CSV vừa xuất
df_csa09 = pd.read_csv('./SS10/CSA09_Info.csv')

## Viết hàm xử lý xếp loại học sinh
def classify(avg):
    if avg>8:
        return 'Giỏi'
    elif avg >= 6.5:
        return 'Khá'
    elif avg >= 5:
        return 'Trung bình'
    else:
        return 'Yếu'

df_csa09['Classification'] = df_csa09['Average'].apply(classify)
print(df_csa09)

df_csa09.to_csv('./SS10/classified_students.csv', index=False)
