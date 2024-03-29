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

# Вариант 2: расчет очков в зависимости от точности попадания
def calc_dist_to_center_of_target(target_x, target_y, score2):
    # Находим центр цели
    target_center_x = target_x + target_width / 2
    target_center_y = target_y + target_height / 2
    # Расстояние до точки попадания
    distance = ((target_center_x - mouse_x) ** 2 + (target_center_y - mouse_y) ** 2) ** 0.5
    return distance

# для остановки бесконечного цикла
running = True
# Счет
score = 0
score2 = 0
while running:
    screen.fill(color)
    # перебираем все события
    for event in pygame.event.get():
        # событие закрыть окно
        if event.type == pygame.QUIT:
            running = False
        # событие нажатие ЛК мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # проверка попадания мышки в цель
            tar_x = target_x < mouse_x < target_x + target_width
            tar_y = target_y < mouse_y < target_y + target_height
            if tar_x and tar_y:
                # Вариант 1: фиксированное количество очков
                score += 1
                print(f'Счет (вариант 1): {score}')
                distance = calc_dist_to_center_of_target(target_x, target_y, score2)
                # Чем ближе к центру, тем больше очков:
                # максимум 10, минус 1 очко за каждые 10 пикселей отклонения
                score2 += max(0, 10 - int(distance / 10))
                print(f'Счет (вариант 2): {score2}')
                # снова задать рандомные координаты
                # координаты мишени с учетом ее размеров
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))
    # обновление экрана
    pygame.display.update()


# завершение и выход из игры
pygame.quit()