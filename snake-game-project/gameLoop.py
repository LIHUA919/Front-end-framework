level = 1
level_speed = snake_speed + (level - 1) * 2

# 在每次吃到食物后，增加蛇的速度
if Length_of_snake % 5 == 0:
    level += 1
    level_speed = snake_speed + (level - 1) * 2

clock.tick(level_speed)




paused = False

while not game_over:
    while game_close == True:
        # 处理游戏结束逻辑
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
            if not paused:
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

    if paused:
        continue

    # 游戏逻辑
    pass



@app.route('/menu', methods=['GET'])
def menu():
    return jsonify({'status': 'Menu'})

@app.route('/help', methods=['GET'])
def help():
    return jsonify({'status': 'Help'})

@app.route('/exit', methods=['GET'])
def exit_game():
    pygame.quit()
    quit()
    return jsonify({'status': 'Game exited'})




lives = 3

while not game_over:
    while game_close == True:
        dis.fill(blue)
        message(f"你输了! 按Q退出或按C重试 (剩余生命: {lives})", red)
        Your_score(Length_of_snake - 1)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    lives -= 1
                    if lives > 0:
                        gameLoop()
                    else:
                        game_over = True
                        game_close = False

    # 游戏逻辑
    pass




obstacles = []

# 生成障碍物
for _ in range(10):
    obstacle_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    obstacle_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    obstacles.append([obstacle_x, obstacle_y])

while not game_over:
    while game_close == True:
        # 处理游戏结束逻辑
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
            if not paused:
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

    if paused:
        continue

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_close = True
        game_over_sound.play()
    x1 += x1_change
    y1 += y1_change
    dis.fill(blue)
    pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

    # 绘制障碍物
    for obstacle in obstacles:
        pygame.draw.rect(dis, black, [obstacle[0], obstacle[1], snake_block, snake_block])

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

    # 检查蛇是否撞到障碍物
    for obstacle in obstacles:
        if x1 == obstacle[0] and y1 == obstacle[1]:
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





    food_types = ['speed_up', 'speed_down', 'length_up']

while not game_over:
    while game_close == True:
        # 处理游戏结束逻辑
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
            if not paused:
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

    if paused:
        continue

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_close = True
        game_over_sound.play()
    x1 += x1_change
    y1 += y1_change
    dis.fill(blue)
    pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

    # 绘制障碍物
    for obstacle in obstacles:
        pygame.draw.rect(dis, black, [obstacle[0], obstacle[1], snake_block, snake_block])

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

    # 检查蛇是否撞到障碍物
    for obstacle in obstacles:
        if x1 == obstacle[0] and y1 == obstacle[1]:
            game_close = True
            game_over_sound.play()

    our_snake(snake_block, snake_List)
    Your_score(Length_of_snake - 1)

    pygame.display.update()

    if x1 == foodx and y1 == foody:
        eat_sound.play()
        food_type = random.choice(food_types)
        if food_type == 'speed_up':
            level_speed += 2
        elif food_type == 'speed_down':
            level_speed -= 2
        elif food_type == 'length_up':
            Length_of_snake += 2
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    clock.tick(level_speed)