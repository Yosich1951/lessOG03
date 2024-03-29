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
target_img = pygame.image.load('img/target.png')
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
    screen.fill(color)
    # перебираем все события
    for event in pygame.event.get():
        # событие закрыть окно
        if event.type == pygame.quit:
            running = False
        # событие нажатие ЛК мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # проверка попадания мышки в цель
            tar_x = target_x < mouse_x < target_x + target_width
            tar_y = target_y < mouse_y < target_y + target_height
            if tar_x and tar_y:
                # снова задать рандомные координаты
                # координаты мишени с учетом ее размеров
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))
    # обновление экрана
    pygame.display.update()


# завершение и выход из игры
pygame.quit()