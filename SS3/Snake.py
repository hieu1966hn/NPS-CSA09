## Nhúng các thư viện cần có để làm game.

import pygame
import sys

## khởi tạo game
pygame.init()

### Kích thước màn hình
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))


### Thiết lập màu sắc
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)

### Tốc độ FPS
fps = pygame.time.Clock()
snake_speed = 15

class Snake:
    def __init__(self):
        ### Khởi tạo các thuộc tính cho rắn
        self.size = 10
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT" ## Hướng di chuyển ban đầu
        self.change_to = self.direction
    
    ### Hàm thay đổi hướng đi của rắn
    def change_direction(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        if direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        if direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        if direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

    ### Hàm di chuyển rắn theo hướng hiện tại
    def move(self):
        head = self.body[0] ## [100, 50]
        if self.direction == "UP":
            new_head = [head[0], head[1] - self.size]
        if self.direction == "DOWN":
            new_head = [head[0], head[1] + self.size]
        if self.direction == "LEFT":
            new_head = [head[0] - self.size, head[1]]
        if self.direction == "RIGHT":
            new_head = [head[0] + self.size, head[1]]

        ## Thêm đầu mới của rắn vào thân
        self.body.insert(0, new_head)

        ## Xóa phần cuối (đuôi) của rắn nếu nó không ăn thức ăn
        self.body.pop()

    ### Thêm một khối vào thân rắn (tăng kích thước rắn)
    def grow(self):
        tail = self.body[-1]
        if self.direction == "UP":
            new_tail = [tail[0], tail[1] + self.size]
        if self.direction == "DOWN":
            new_tail = [tail[0], tail[1] - self.size]
        if self.direction == "LEFT":
            new_tail = [tail[0] + self.size, tail[1]]
        if self.direction == "RIGHT":
            new_tail = [tail[0] - self.size, tail[1]]
    
        ## Thêm khối mới đó vào thân
        self.body.append(new_tail)
    
    ### Kiểm tra xem rắn va chạm: tường và chính nó
    def check_collision(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= screen_width or head[1] < 0 or head[1] >= screen_height:
            return True

        ### Kiểm tra nếu đầu rắn chạm vào thân
        if head in self.body[1:]:
            return True
        
        return False