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


CSA09 = {
    'Name': ['Khánh','Du','Phong', 'Vũ', 'Lâm'],
    'Age': [15, 17, 17, 15, 16],
    'Point': [8, 9, 10, 9.5, 8]
}

## Tạo DF
CSA09_DF = pd.DataFrame(CSA09)
# print(CSA09_DF.head())
# print(CSA09_DF.info())

### Xuất dữ liệu lớp học CSA09 ra file CSV
CSA09_DF.to_csv('./SS10/CSA09_Students.csv', index=False)