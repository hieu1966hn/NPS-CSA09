import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt



df = pd.read_excel('./SS12/provinces_updated.xls')
df = df.sort_values('Population')

# print(df)


## Khai báo 2 biến 
fig, ax = plt.subplots(figsize=(16, 6))

## Biểu đồ cột (Bar)
plt.bar(range(len(df)), df['Population'], width=0.6, tick_label=range(1, len(df)+1))


## chỉnh sửa chút axes:
plt.xlim(-1, 63)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

## Đặt tiêu đề & các trường
plt.suptitle('Population in Vietnam Provinces & Cities', fontsize=24, color='#444444', x=0.125, ha='left')
plt.title('sorted ascending')
plt.xlabel('Province/City', fontsize=18, color='#333333')
plt.ylabel('Population (1000 people)', fontsize=18, color='#333333')


plt.show()
