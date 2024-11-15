import pandas as pd


# Ví dụ 1 series
s = pd.Series([1, 2, 3 ,4])
print(s)


# Ví dụ 1 dataframe
data = {
    'Name': ['Khánh', "Lâm"],
    'Age': [25, None]
}
df = pd.DataFrame(data)
print(df)