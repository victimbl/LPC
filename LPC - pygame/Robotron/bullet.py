import pygame
from config import Config


class Bullet:
    def __init__(self, x: float, y: float):
        self.__img_fixed1 = pygame.image.load("assets/bullet_white.png")
        self.__img_fixed2 = pygame.image.load("assets/bullet_blue.png")
        self.__img_fixed3 = pygame.image.load("assets/bullet_red.png")
        self.__img_fixed4 = pygame.image.load("assets/bullet_green.png")
        self.__img_fixed5 = pygame.image.load("assets/bullet_purple.png")
        self.__xcor = x
        self.__ycor = y
        self.__rect = self.__img_fixed1.get_rect()
        self.__vector_init = pygame.Vector2(0, -Config.speed_bullet)
        self.__vector = self.__vector_init
        self.__angle = 0
        self.__number = 0
        self.__delete = False

    def move(self):
        self.__xcor += self.__vector[0]
        self.__ycor += self.__vector[1]

        # limit
        if (self.__xcor > Config.screen_w + 20 or self.__xcor < -20
                or self.__ycor > Config.screen_h + 20 or self.__ycor < -20):
            self.__delete = True

    def draw(self):
        img = self.__choose_img()

        self.__rect = img.get_rect()
        self.__rect.center = (self.__xcor, self.__ycor)
        Config.screen.blit(img, self.__rect)

    def __choose_img(self):
        self.__number += 1
        img = pygame.image.load("assets/nothing.png")
        if self.__number >= 25:
            self.__number = 0
        if self.__number < 5:
            img = pygame.transform.rotate(self.__img_fixed1, -self.__angle)
        elif self.__number < 10:
            img = pygame.transform.rotate(self.__img_fixed2, -self.__angle)
        elif self.__number < 15:
            img = pygame.transform.rotate(self.__img_fixed3, -self.__angle)
        elif self.__number < 20:
            img = pygame.transform.rotate(self.__img_fixed4, -self.__angle)
        elif self.__number < 25:
            img = pygame.transform.rotate(self.__img_fixed5, -self.__angle)

        return img

    def select_angle(self, x, y):
        if x == 0 and y == 1:
            self.__vector = self.__vector_init.rotate(0)
            self.__angle = 0
        elif x == 1 and y == 1:
            self.__vector = self.__vector_init.rotate(45)
            self.__angle = 45
        elif x == 1 and y == 0:
            self.__vector = self.__vector_init.rotate(90)
            self.__angle = 90
        elif x == 1 and y == -1:
            self.__vector = self.__vector_init.rotate(135)
            self.__angle = 135
        elif x == 0 and y == -1:
            self.__vector = self.__vector_init.rotate(180)
            self.__angle = 180
        elif x == -1 and y == -1:
            self.__vector = self.__vector_init.rotate(225)
            self.__angle = 225
        elif x == -1 and y == 0:
            self.__vector = self.__vector_init.rotate(270)
            self.__angle = 270
        elif x == -1 and y == 1:
            self.__vector = self.__vector_init.rotate(315)
            self.__angle = 315

    def get_delete(self):
        return self.__delete

    def set_delete(self):
        self.__delete = True

    def get_rect(self):
        return self.__rect
