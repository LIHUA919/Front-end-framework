from flask import Flask, jsonify, request
import threading
import pygame
import time
import random

app = Flask(__name__)

# 初始化Pygame
pygame.init()

# 定义颜色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 定义屏幕尺寸
dis_width = 800
dis_height = 600

# 创建游戏窗口
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('贪吃蛇游戏')

# 定义时钟
clock = pygame.time.Clock()

# 定义蛇的初始速度和大小
snake_block = 10
snake_speed = 15

# 定义字体
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# 加载音效
pygame.mixer.init()
eat_sound = pygame.mixer.Sound('static/eat_sound.wav')  # 替换为你的音效文件
game_over_sound = pygame.mixer.Sound('static/game_over_sound.wav')  # 替换为你的音效文件

# 显示分数
def Your_score(score):
    value = score_font.render("你的分数: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# 画蛇
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# 显示消息
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# 主函数
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    level = 1
    level_speed = snake_speed + (level - 1) * 2

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("你输了! 按Q退出或按C重试", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
            game_over_sound.play()
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
                game_over_sound.play()

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            eat_sound.play()
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            if Length_of_snake % 5 == 0:
                level += 1
                level_speed = snake_speed + (level - 1) * 2

        clock.tick(level_speed)

    pygame.quit()
    quit()

@app.route('/start', methods=['POST'])
def start_game():
    threading.Thread(target=gameLoop).start()
    return jsonify({'status': 'Game started'})

if __name__ == '__main__':
    app.run(debug=True)