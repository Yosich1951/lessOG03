import pygame
import random
# инициализация
pygame.init()
# константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# создать окно
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# заголовок окна
pygame.display.set_caption('Игра Тир')
# загрузить иконку для игры
icon = pygame.image.load('img/young-gamer.jpg')
pygame.display.set_icon(icon)
# мишень
target_image = pygame.image.load('img/target.png')
target_width = 80
target_height = 80
# координаты мишени с учетом ее размеров
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
# цвет фона
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# для остановки бесконечного цикла
running = True
while running:
    pass

# завершение и выход из игры
pygame.quit()