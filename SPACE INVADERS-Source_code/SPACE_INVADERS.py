'''
----------------------------About the game-----------------------------------------------------------
Space invaders is a  shooting game developed using pygame (python).

The game space invaders have a simple plotline. Alien invaders have come to Earth. The player is in control of the missile cannon and must destroy all of the Aliens before they reach Earth.

The player controls a cannon and can moves left and right on the 
X-Axis near the bottom of the screen.

The Player has three controls, left, right and fire. player objective is to destroy the Aliens before they reach the bottom of the screen. The player receives one point for destroying the one Alien.

-----------------------License-------------------------------------------------------------------------------
MIT License

Copyright (c) 2021 Arwaz Khan 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

----------------------------Source code available-----------------------------
► Game Website - https://arwazkhan189.github.io/SPACE-INVADERS/
► Github repository link -https://github.com/arwazkhan189/SPACE-INVADERS
------------------Follow Me On Social Media-----------------------------------

► Website  - https://arwazkhan189.github.io/
► Facebook - https://www.facebook.com/arwazkhan189
► Instagram - https://instagram.com/iamarwaz
► Twitter - https://twitter.com/arwazkhan189
► LinkedIn - https://www.linkedin.com/in/arwaz-khan-bb52a1134/
► Github - https://github.com/arwazkhan189
​
'''
# -----------------module importing-------------------
import pygame
import random
import math
import sys
import os

#-----------------requirement for pyinstaller-------
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# ------------------initilize pygame-------------------
pygame.init()

# --------------------Game Resolution-----------------------
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# -------------------clock/fps--------------------------
FPS = 3000  # frames per second setting
clock = pygame.time.Clock()

# ----------------title and icon----------------------
pygame.display.set_caption("SPACE INVADERS")
icon_path=resource_path("Assets/images/icon.png")
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)

# -----------Game Fonts-------------------------
pygame.font.init()
font = resource_path("Assets/fonts.ttf")

# ---------------Colors--------------------
white = (255, 255, 255)
black = (0, 0, 0)
title_color = "yellow"

# ----------------background image----------------------
bg_path=resource_path("Assets/images/bgmenu.png")
background = pygame.image.load(bg_path)  # menu background

# ----------------------load music files-------------------
pygame.mixer.init()
btn_sound_path=resource_path("Assets/audio/up_down_button_sound.wav")
button_sound = pygame.mixer.Sound(btn_sound_path)  # up,down,back sound
enter_sound_path=resource_path("Assets/audio/select_button_sound.wav")
enter_sound = pygame.mixer.Sound(enter_sound_path)    # enter , exit sound

# ------------------Game-------------------------------------
def start_game():
    # -------------------clock/fps--------------------------
    FPS = 3000  # frames per second setting
    clock = pygame.time.Clock()

    # ----------------background image----------------------
    bgi_path=resource_path("Assets/images/background.jpg")
    background = pygame.image.load(bgi_path)

    # ------------music and sound--------------------------
    pygame.mixer.init()
    music_bg_path=resource_path("Assets/audio/bgsound.wav")
    pygame.mixer.music.load(music_bg_path)
    pygame.mixer.music.play(-1)

    # ---------------player-------------------------------
    pi_path=resource_path("Assets/images/player.png")
    playerimg = pygame.image.load(pi_path)
    playerx = 370
    playery = 480
    playerxchange = 0

    def player(x, y):
        screen.blit(playerimg, (x, y))

    # ---------------enemy-------------------------------
    enemyimg = []
    enemyx = []
    enemyy = []
    enemyxchange = []
    enemyychange = []
    num_of_enemies = 4

    for i in range(num_of_enemies):
        ei_path=resource_path("Assets/images/enemy.png")
        enemyimg.append(pygame.image.load(ei_path))
        enemyx.append(random.randint(0, 735))
        enemyy.append(random.randint(50, 150))
        enemyxchange.append(0.5)
        enemyychange.append(40)

    def enemy(x, y, i):
        screen.blit(enemyimg[i], (x, y))

    # ---------------bullet-------------------------------
    bu_path=resource_path("Assets/images/bullet.png")
    bulletimg = pygame.image.load(bu_path)
    bulletx = 0
    bullety = 480  # spaceship position
    bulletychange = 0.6
    bulletstate = "ready"  # ready-> rest, fire-> move bullet

    def fire_bullet(x, y):
        # appears bullet above from spaceship
        screen.blit(bulletimg, (x+16, y+10))

    # ---------------------boom--------------------------------------------------------
    boomimg_path=resource_path("Assets/images/boom.png")
    boomimg = pygame.image.load(boomimg_path)

    def boom(x, y):
        enemyimg = boomimg
        screen.blit(enemyimg, (x, y))
        player(playerx, playery)
        show_score(textx, texty)
        pygame.display.update()
        clock.tick(7)

    # -------------------------------iscollisoion---------------------------------------------
    def iscollision(enemyx, enemyy, bulletx, bullety):
        distance = math.sqrt(((enemyx-bulletx)**2)+((enemyy-bullety)**2))  # distance formula
        if (distance < 27):
            return True
        else:
            return False

    # ----------------------score---------------------------------
    score = 0
    fnt_path=resource_path("Assets/fonts.ttf")
    font = pygame.font.Font(fnt_path, 32)
    textx = 10
    texty = 10

    def show_score(x, y):
        display_score = font.render("SCORE :"+str(score), True, (255, 255, 255))
        screen.blit(display_score, (x, y))

    # ----------------------game over---------------------------------------
    def game_over():
        gameover_fnt_path=resource_path("Assets/fonts.ttf")
        game_over_font = pygame.font.Font(gameover_fnt_path, 64)
        game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(game_over_text, (170, 250))

    # ---------------------game loop----------------------------
    running = True
    while running:
        # ----background----------------
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    pygame.mixer.music.pause()  # pause the music and go back to menu
                    running=False
                    main_menu()
                if (event.key == pygame.K_LEFT):
                    playerxchange = -0.5
                if (event.key == pygame.K_RIGHT):
                    playerxchange = 0.5
                if (event.key == pygame.K_SPACE):
                    if (bulletstate == "ready"):
                        bu_sound_path=resource_path("Assets/audio/shoot.wav")
                        bullet_sound = pygame.mixer.Sound(bu_sound_path)  # bullet release sound
                        bullet_sound.play()
                        bulletx = playerx
                        bulletstate = "fire"
                        fire_bullet(bulletx, bullety)
            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                    playerxchange = 0
        # ---player movement----
        playerx += playerxchange
        if (playerx <= 0):
            playerx = 0
        elif(playerx >= 736):
            playerx = 736

        # ---enemy movement----
        for i in range(num_of_enemies):
            # -----------game over condition-------------
            if (enemyy[i] > 440):
                for j in range(num_of_enemies):
                    enemyy[j] = 2000
                game_over()
                # ---After game over player action set to none
                bulletstate = ''
                playerxchange = 0
                playerx = 370
                playery = 480
                break

            enemyx[i] += enemyxchange[i]
            if (enemyx[i] <= 0):
                enemyxchange[i] = 0.3
                enemyy[i] += enemyychange[i]
            elif(enemyx[i] >= 736):
                enemyxchange[i] = -0.3
                enemyy[i] += enemyychange[i]
            # ------hit enemy---------------------------------------
            collision = iscollision(enemyx[i], enemyy[i], bulletx, bullety)
            if collision:
                boom(enemyx[i], enemyy[i])
                # bullet hit to enemy sound
                exp_sound_path=resource_path("Assets/audio/boom.wav")
                explosion_sound = pygame.mixer.Sound(exp_sound_path)
                explosion_sound.play()
                bullety = 480
                bulletstate = "ready"
                score += 1
                enemyx[i] = random.randint(0, 735)
                enemyy[i] = random.randint(50, 150)
            enemy(enemyx[i], enemyy[i], i)
        # ---bullet movement-----
        if (bullety <= 0):
            bullety = 480
            bulletstate = "ready"
        if (bulletstate == "fire"):
            fire_bullet(bulletx, bullety)
            bullety -= bulletychange

        player(playerx, playery)
        show_score(textx, texty)
        pygame.display.update()
        clock.tick(FPS)


# ----------------- Text Renderer-----------------------
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText

# --------------------------about game---------------------------------
def about_game():
    about_bg_fnt_path=resource_path("Assets/images/about_bg.png")
    about_bg = pygame.image.load(about_bg_fnt_path)
    about = True
    # about reading sound
    pygame.mixer.init()
    am_path=resource_path("Assets/audio/About_read_audio.wav")
    pygame.mixer.music.load(am_path)
    pygame.mixer.music.play()  # play text sound
    while about:
        screen.blit(about_bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                about = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.pause()  # pause text sound
                    button_sound.play()
                    main_menu()
        pygame.display.update()
        clock.tick(60)

# -----------------Main Menu------------------
def main_menu():
    menu = True
    selected = "start"
    font = resource_path("Assets/fonts.ttf")
    while menu:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu=False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    button_sound.play()
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    button_sound.play()
                    selected = "about"
                elif event.key == pygame.K_ESCAPE:
                    menu=False
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        enter_sound.play()
                        start_game()  # start the game
                    if selected == "about":
                        enter_sound.play()
                        about_game()

        # ------------------Main Menu UI----------------
        title = text_format("SPACE INVADERS", font, 64, title_color)
        if selected == "start":
            text_start = text_format("START", font, 75, white)
        else:
            text_start = text_format("START", font, 75, black)
        if selected == "about":
            text_about = text_format("ABOUT", font, 75, white)
        else:
            text_about = text_format("ABOUT", font, 75, black)
        text_enter = text_format("PRESS ENTER TO SELECT OPTION", font, 20, "yellow")
        text_quit = text_format("PRESS ESC TO QUIT", font, 20, "yellow")

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        about_rect = text_about.get_rect()
        enter_rect = text_enter.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 220))
        screen.blit(text_about, (screen_width/2 - (about_rect[2]/2), 280))
        screen.blit(text_enter, (screen_width/2 - (enter_rect[2]/2), 0))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 568))
        pygame.display.update()
        clock.tick(FPS)

# -------------------start the game (main program)-----------------------------------------
main_menu()
pygame.quit()
sys.exit()
