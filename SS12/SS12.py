### Sử dụng thư viện Matplotlib
import matplotlib as plt
import matplotlib.pyplot as plt

### Ví dụ với biểu đồ đường
# x = [1, 2, 3, 4]
# y = [10, 20, 30, 40]
# plt.plot(x, y, label="Dữ liệu mẫu")
# plt.xlabel('Thời gian')
# plt.ylabel('Giá trị')
# plt.title("Biểu đồ tăng trưởng")

# plt.show()


### Ví dụ với Figure
# plt.figure(figsize=(10, 5))
# plt.plot([1,2,3], [4,5,6])
# plt.show()

### Ví dụ với biểu đồ histtogram: Biểu diễn tần suất dữ liệu xuất hiện
# data = [1,2,2,3,3,3,4,4,4,4] ## Tập dữ liệu
# plt.hist(data, bins = 1000 ) ## bins=n chia thành n cột dựa trên tần suất của các giá trị từ 1 đến n.
# plt.show()


### Biểu đồ tròn pie
sizes = [20, 30, 25, 20, 5]
labelNames = ['Đông Du', 'Phong', 'Vũ', 'lâm', 'Khánh']
plt.pie(sizes, labels=labelNames)

### Xuất biểu đồ dưới dạng hình ảnh
plt.savefig('./SS12/bieudohinhtron.jpg')
# plt.show()