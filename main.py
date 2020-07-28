import pygame
import time
import random
import sys

pygame.init ()

gray = (119, 118, 110)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 128, 0)
bright_green = (124, 252, 0)
bright_red = (139, 0, 0)
blue = (0, 0, 255)
bright_blue = (173, 216, 230)
pause = False

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode ((screen_width, screen_height))
pygame.display.set_caption (('Car Game'))
clock = pygame.time.Clock ()
bgimg = pygame.image.load ('car1.png')
background_img = pygame.image.load ('background.png')
intro_background = pygame.image.load ('Welcome.png')
instruction_background = pygame.image.load ('intro.png')

car_width = 20
font = pygame.font.SysFont (None, 60)


def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                pygame.quit ()
                quit ()
        screen.blit (intro_background, (0, 0))
        screen_text = pygame.font.Font ('freesansbold.ttf', 115)
        text_surf, text_rect = text_object ('CAR GAME', screen_text)
        text_rect.center = (400, 100)
        screen.blit (text_surf, text_rect)
        button ('START', 150, 520, 100, 50, green, bright_green, 'play')
        button ('QUIT', 550, 520, 100, 50, red, bright_red, 'quit')
        button ('INSTRUCTION', 300, 520, 200, 50, blue, bright_blue, 'intro')
        pygame.display.update ()
        clock.tick (50)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos ()
    click = pygame.mouse.get_pressed ()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect (screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == 'play':
                countdown()
            elif action == 'quit':
                pygame.quit ()
                quit ()
                sys.exit ()
            elif action == 'intro':
                instruction_loop ()
            elif action == 'menu':
                intro_loop ()
            elif action == 'pause':
                # print('in')
                paused ()
            elif action == 'unpause':
                unpaused ()
    else:
        pygame.draw.rect (screen, ic, (x, y, w, h))
    screen_text = pygame.font.Font ('freesansbold.ttf', 20)
    text_surf, text_rect = text_object (msg, screen_text)
    text_rect.center = ((x + (w // 2), y + (h // 2)))
    screen.blit (text_surf, text_rect)


def paused():
    global pause
    if pause == True:
        pause = False
    while not pause:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                pygame.quit ()
                quit ()
                sys.exit ()
        screen.blit (instruction_background, (0, 0))
        largetext = pygame.font.Font ('freesansbold.ttf', 115)
        text_surf, text_rect = text_object ('PAUSED', largetext)
        text_rect.center = (screen_width // 2, screen_height // 2)
        screen.blit (text_surf, text_rect)
        button ('CONTINUE', 150, 450, 150, 50, green, bright_green, 'unpause')
        button ('RESTART', 350, 450, 150, 50, red, bright_red, 'play')
        button ('MAIN MENU', 550, 450, 150, 50, blue, bright_blue, 'menu')
        pygame.display.update ()
        clock.tick (30)


def unpaused():
    global pause
    pause = True

def countdown_background():
    font = pygame.font.SysFont(None, 25)
    x = int(screen_width*0.5)
    y = int(screen_height*0.8)
    screen.blit(background_img, (0, 0))
    screen.blit(bgimg, (x, y))
    text = font.render('DODGED : ', True, black)
    score = font.render('SCORE : ', True, red)
    screen.blit(text, (10, 50))
    screen.blit(score, (10, 30))
    button('PAUSE', 650, 0, 150, 50, blue, bright_blue, 'pause')

def countdown():
    countdown = True
    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        text_surf, text_rect = text_object('3', largetext)
        text_rect.center = (screen_width//2, screen_height//2)
        screen.blit(text_surf, text_rect)
        pygame.display.update()
        clock.tick(1)

        screen.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        text_surf, text_rect = text_object ('2', largetext)
        text_rect.center = (screen_width // 2, screen_height // 2)
        screen.blit (text_surf, text_rect)
        pygame.display.update ()
        clock.tick (1)

        screen.fill (gray)
        countdown_background ()
        largetext = pygame.font.Font ('freesansbold.ttf', 115)
        text_surf, text_rect = text_object ('1', largetext)
        text_rect.center = (screen_width // 2, screen_height // 2)
        screen.blit (text_surf, text_rect)
        pygame.display.update ()
        clock.tick (1)

        screen.fill (gray)
        countdown_background ()
        largetext = pygame.font.Font ('freesansbold.ttf', 115)
        text_surf, text_rect = text_object ('GO!!!', largetext)
        text_rect.center = (screen_width // 2, screen_height // 2)
        screen.blit(text_surf, text_rect)
        pygame.display.update()
        clock.tick(1)
        game_loop()

def instruction_loop():
    instruction = True
    while instruction:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                pygame.quit ()
                quit ()
                sys.exit ()
        screen.blit (instruction_background, (0, 0))
        largetext = pygame.font.Font ('freesansbold.ttf', 80)
        smalltext = pygame.font.Font ('freesansbold.ttf', 20)
        mediumtext = pygame.font.Font ('freesansbold.ttf', 40)
        xtext_surf, xtext_rect = text_object ('This is car game in which you need to dodge the coming cars.', smalltext)
        xtext_rect.center = (350, 200)
        ytext_surf, ytext_rect = text_object ('INSTRUCTION', largetext)
        ytext_rect.center = (400, 100)
        screen.blit (xtext_surf, xtext_rect)
        screen.blit (ytext_surf, ytext_rect)

        stext_surf, stext_rect = text_object ('ARROW LEFT : LEFT TURN', smalltext)
        stext_rect.center = (150, 400)

        htext_surf, htext_rect = text_object ('ARROW RIGHT : RIGHT TURN', smalltext)
        htext_rect.center = (150, 450)

        atext_surf, atext_rect = text_object ('A : ACCELERATION', smalltext)
        atext_rect.center = (150, 500)

        rtext_surf, rtext_rect = text_object ('B : BREAKS', smalltext)
        rtext_rect.center = (150, 550)

        ptext_surf, ptext_rect = text_object ('P : PAUSE', smalltext)
        ptext_rect.center = (150, 350)

        mtext_surf, mtext_rect = text_object ('CONTROLS', mediumtext)
        mtext_rect.center = (350, 300)

        screen.blit (stext_surf, stext_rect)
        screen.blit (htext_surf, htext_rect)
        screen.blit (atext_surf, atext_rect)
        screen.blit (rtext_surf, rtext_rect)
        screen.blit (ptext_surf, ptext_rect)
        screen.blit (mtext_surf, mtext_rect)
        button ('BACK', 600, 450, 100, 50, blue, bright_blue, 'menu')
        pygame.display.update ()
        clock.tick (30)


def obstacles(obs_startx, obs_starty, obs):
    global obs_pic
    if obs == 0:
        obs_pic = pygame.image.load ('car2.png')
    elif obs == 1:
        obs_pic = pygame.image.load ('car3.png')
    elif obs == 2:
        obs_pic = pygame.image.load ('car4.png')
    elif obs == 3:
        obs_pic = pygame.image.load ('car5.png')
    elif obs == 4:
        obs_pic = pygame.image.load ('car6.png')
    elif obs == 5:
        obs_pic = pygame.image.load ('car7.png')
    screen.blit (obs_pic, (obs_startx, obs_starty))


def score_system(passed, score):
    font = pygame.font.SysFont (None, 30)
    text = font.render ('Passed : ' + str (passed), True, black)
    score = font.render ('Score : ' + str (score), True, red)
    screen.blit (score, (10, 30))
    screen.blit (text, (10, 50))


def car_img(x, y):
    screen.blit (bgimg, [x, y])


def background():
    screen.blit (background_img, (0, 0))


def text_object(text, font):
    s_text = font.render (text, True, black)
    return s_text, s_text.get_rect ()


def text_screen(text):
    screen_text = pygame.font.Font ('freesansbold.ttf', 80)
    text_surf, text_rect = text_object (text, screen_text)
    text_rect.center = ((screen_width // 2), (screen_height // 2))
    screen.blit (text_surf, text_rect)
    pygame.display.update ()
    time.sleep (3)
    game_loop ()


def crash():
    text_screen ('You Crashed')


def game_loop():
    global pause

    x = int(screen_width * 0.5)
    y = int(screen_height * 0.8)
    obstacle_speed = 9
    y_change = 0
    obs = 0
    obs_startx = random.randrange(200, screen_width - 200)
    obs_starty = -750
    obs_width = 20
    obs_height = 120
    passed = 0
    level = 0
    score = 0
    y2 = 7

    x_change = 0
    exit_game = False
    while not exit_game:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                pygame.quit ()
                quit ()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5

                if event.key == pygame.K_RIGHT:
                    x_change = 5

                if event.key == pygame.K_a:
                    obstacle_speed += 2

                if event.key == pygame.K_b:
                    obstacle_speed -= 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        screen.fill (gray)

        rel_y = y2%background_img.get_rect().width
        screen.blit(background_img, (0, rel_y-background_img.get_rect().width))
        screen.blit(background_img, (700, rel_y - background_img.get_rect().width))
        if rel_y < 800:
            screen.blit(background_img, (0, rel_y))

        y2 += obstacle_speed

        obs_starty -= obstacle_speed // 4
        obstacles (obs_startx, obs_starty, obs)
        obs_starty += obstacle_speed
        car_img (x, y)
        score_system (passed, score)

        if x > 690 - car_width or x < 110:
            crash ()

        if x > screen_width - (car_width + 150) or x < 150:
            crash ()

        if obs_starty > screen_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange (150, (screen_width - 150))
            obs = random.randrange (0, 6)
            passed += 1
            score = passed * 10
            if int (passed) % 10 == 0:
                level = level + 1
                obstacle_speed = obstacle_speed + 2
                screen_text = pygame.font.Font ('freesansbold.ttf', 80)
                text_surf, text_rect = text_object ('LEVEL ' + str (level), screen_text)
                text_rect.center = ((screen_width // 2), (screen_height // 2))
                screen.blit (text_surf, text_rect)
                pygame.display.update ()
                time.sleep (3)

        if y < obs_starty + obs_height:
            if obs_startx < x and x < obs_startx + obs_width or obs_startx < x + car_width and x < obs_startx + obs_width:
                crash ()

        button ('PAUSE', 650, 0, 150, 50, blue, bright_blue, 'pause')
        pygame.display.update ()
        clock.tick (60)
    # pygame.quit()
    # quit()


intro_loop ()
game_loop ()
pygame.quit ()
quit ()
