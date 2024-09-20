#### Bài tập OOP phân số
class PhanSo:
    def __init__(self, tuso, mauso):
        self.tuso = tuso
        self.mauso = mauso

    ### Hàm tìm UCLN 
    def find_UCLN(self, a, b): ## 3 , 6
        smaller = min(abs(a), abs(b)) ## 3
        ucln = 1 ## mặc định bằng 1
        for i in range(1, smaller + 1): ## phạm vi: 1, 2, 3
            if a % i == 0 and b % i  ==0: 
                ucln = i ## 1, 3
        return ucln

    ### Hàm rút gọn phân số
    def rutGonPhanSo(self):
        ucln = self.find_UCLN(self.tuso, self.mauso)
        self.tuso = self.tuso/ucln
        self.mauso = self.mauso/ucln
        return PhanSo(self.tuso, self.mauso)
        

    ### Hàm hiển thị phân số => mặc định tự gọi khi sử dụng hàm print
    def __str__(self):
        return f"{self.tuso}/{self.mauso}"


    ### Có phương thức gì cho phân số: +, -, *, /
    ## Hàm cộng 2 phân số 
    def add(self, other):
        new_tuso = self.tuso * other.mauso + other.tuso * self.mauso
        new_mauso = self.mauso * other.mauso
        return PhanSo(new_tuso, new_mauso)
    
    ## Hàm trừ 2 phân số 
    def sub(self, other):
        new_tuso = self.tuso * other.mauso - other.tuso * self.mauso
        new_mauso = self.mauso * other.mauso
        return PhanSo(new_tuso, new_mauso)
    
    ## Hàm nhân 2 phân số 
    def multiply(self, other):
        new_tuso = self.tuso * other.tuso
        new_mauso = self.mauso * other.mauso
        return PhanSo(new_tuso, new_mauso)
    
    ## Hàm chia 2 phân số 
    def divide(self, other):
        new_tuso = self.tuso * other.mauso
        new_mauso = self.mauso * other.tuso
        return PhanSo(new_tuso, new_mauso)

## Khai báo các phân số
phanso1 = PhanSo(3, 2)
phanso2 = PhanSo(7, 5)
phanso3 = PhanSo(3, 6)

### hiển thị được phân số 3 ở dạng rút gọn: 
### Cộng, trừ, nhân, chia các phân số => ra kết quả và hiển thị trên màn hình terminal
phanso3.rutGonPhanSo()
print(phanso3.tuso)
print(phanso3) 