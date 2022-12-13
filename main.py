import pygame as pg
import numpy as np
import random


class Matrix:  # класс для работы с таблицей букв
    def __init__(self, app):
        self.app = app
        self.font_size = 8
        self.katakana = np.array([chr(int('0x30a0', 16) + i) for i in range(1, 95)] + ['' for i in range(20)])
        self.font = pg.font.Font('MS Mincho.ttf', self.font_size, bold=True)
        self.columns = app.WIDTH // self.font_size
        self.drops = [1 for i in range(0, self.columns)]

    def draw(self):   # функция отрисовки букв
        for i in range(0, len(self.drops)):
            char = random.choice(self.katakana)  # выбираем случайную букву из нашего алфавита
            char_render = self.font.render(char, False, (0, 200, 0))
            pos = i * self.font_size, self.drops[i] * self.font_size
            self.app.surface.blit(char_render, pos)
            if self.drops[i] * self.font_size > app.HEIGHT and random.uniform(0, 1) > 0.975:
                self.drops[i] = 0
            self.drops[i] = self.drops[i] + 1

    def run(self):
        self.draw()


class MatrixVision:    # класс для главного приложения(окна с картинкой)
    def __init__(self):
        self.RES = self.WIDTH, self.HEIGHT = 1100, 700  # задаём разрешение
        pg.init()                                       # инициализируем библиотеку
        self.screen = pg.display.set_mode(self.RES)     # создаём экран и передаём параметры разрешения
        self.surface = pg.Surface(self.RES, pg.SRCALPHA)             # параметры поверхности
        self.clock = pg.time.Clock()                    # выведем время выполнения кода
        self.matrix = Matrix(self)                      # экземпляр класса таблицы букв

    def draw(self):    # метод окраски экрана(фон)
        self.surface.fill((0, 0, 0, 10))
        self.matrix.run()
        self.screen.blit(self.surface, (0, 0))

    def run(self):    # функция запуска экрана
        while True:
            self.draw()    #вызываем функцию отрисовки
            [exit() for i in pg.event.get() if i.type == pg.QUIT]    # делаем проверку на закрытие экрана
            pg.display.flip()                                     # обновление поверхности
            self.clock.tick(30)    # установка количества кадров


if __name__ == '__main__':
    app = MatrixVision()    # создаём экземпляр класса приложения
    app.run()        # запускаем экран





