import pygame
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
icon = pygame.image.load('')

# для остановки бесконечного цикла
running = True
while running:
    pass

# завершение и выход из игры
pygame.quit()