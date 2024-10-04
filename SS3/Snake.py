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
    
    ### Vẽ rắn lên màn hình 
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, green, pygame.Rect(segment[0], segment[1], self.size, self.size))
    

#### Hàm chính của trò chơi
def main():
    ## Khởi tạo đối tượng rắn con và thức ăn
    snake = Snake()

    ## Khởi tạo điểm số cho trò chơi
    score = 0

    ### chạy vòng lặp kiểm tra sự kiện bấm phím của người chơi
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            ### kiểm tra phím di chuyển nào được bấm
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_to = "UP" ## Hướng thay đổi là lên
                if event.key == pygame.K_DOWN:
                    snake.change_to = "DOWN" ## Hướng thay đổi là xuống
                if event.key == pygame.K_LEFT:
                    snake.change_to = "LEFT" ## Hướng thay đổi là trái 
                if event.key == pygame.K_RIGHT:
                    snake.change_to = "RIGHT" ## Hướng thay đổi là phải

        ### Cập nhật hướng đi của rắn
        snake.change_direction(snake.change_to)

        ### Di chuyển rắn
        snake.move()

        ### Vẽ mọi thứ lên màn hình 
        screen.fill(black)
        snake.draw(screen)

        ### Cập nhật màn hình
        pygame.display.update()

        ### Điều chỉnh tốc độ khung hình
        fps.tick(snake_speed)
    
### Chạy trò chơi
if __name__ == "__main__":
    main()

