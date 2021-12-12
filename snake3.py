#https://ichi.pro/pl/jak-zaimplementowac-gre-snake-w-pythonie-za-pomoca-pygame-80810187419306
import time
import pygame
import random
#tworzy gre
pygame.init()

#colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

#wielkosc pola po którym sunie waz

dis_width = 800
dis_height = 800
dis = pygame.display.set_mode((dis_width, dis_height))

#napis na górze
pygame.display.set_caption("kocham pythona")

game_over = False

#dane startowe i wielksoc weza
#zmiena predkosci weza

snake_speed = 30

snake_block = 10

x1 = dis_width / 2
y1 = dis_height / 2

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

#czcionka wyswietlenia
font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg,[dis_width/2, dis_height/2])



#sterowanie
while not game_over:
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
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1<0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(black)

    #punkt startowy
    pygame.draw.rect(dis, blue, [x1, y1, snake_block, snake_block])
    pygame.display.update()

    #predkosc weza
    clock.tick(snake_speed)

message("you lost", red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()

# Dodawanie jedzenia: