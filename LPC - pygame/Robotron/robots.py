import random

import pygame
from sprite_player import Img


class Grunt:
    def __init__(self, x, y, speed):
        self.__photo = Img.grunt_stop
        self.__eye = Img.grunt_eye1
        self.__rect = self.__photo.get_rect()
        self.__xcor = x
        self.__ycor = y
        self.__life = 1
        self.__speed = speed
        self.__spawn = True
        self.__walk = True
        self.__counter1 = 0
        self.__counter2 = 0
        self.__type_robot = "Grunt"

    def move(self, x, y):
        if self.__counter1 % 20 == 0:
            if x >= self.__xcor and self.__walk:
                if y >= self.__ycor:
                    self.__xcor += self.__speed
                    self.__ycor += self.__speed
                elif y < self.__ycor:
                    self.__xcor += self.__speed
                    self.__ycor -= self.__speed
            elif x < self.__xcor and self.__walk:
                if y >= self.__ycor:
                    self.__xcor -= self.__speed
                    self.__ycor += self.__speed
                elif y < self.__ycor:
                    self.__xcor -= self.__speed
                    self.__ycor -= self.__speed

    def draw(self, surface: pygame.Surface):
        self.__counter1 += 1
        self.__counter2 += 1
        if self.__counter1 >= 80:
            self.__counter1 = 0
        if self.__counter2 >= 20:
            self.__counter2 = 0
        self.__photo = Img.list_grunt[int(self.__counter1/20)]
        self.__eye = Img.list_grunt_eyes[int(self.__counter2/5)]
        self.__rect = self.__photo.get_rect()
        self.__rect.center = (self.__xcor, self.__ycor)
        surface.blit(self.__photo, self.__rect)
        surface.blit(self.__eye, self.__rect)

    def limit(self, up, down, left, right):
        w = self.__photo.get_width()
        h = self.__photo.get_height()
        if self.__ycor - h/2 < up:
            self.__ycor += self.__speed
        elif self.__ycor + h/2 > down:
            self.__ycor -= self.__speed
        if self.__xcor - w/2 < left:
            self.__xcor += self.__speed
        elif self.__xcor + w/2 > right-5:
            self.__xcor -= self.__speed

    def get_rect(self):
        return self.__rect

    def get_type(self):
        return self.__type_robot


class Hulk:
    def __init__(self, x, y, speed, colors):
        self.__photo = Img.hulk_front_stop
        self.__rect = self.__photo.get_rect()
        self.__xcor = x
        self.__ycor = y
        self.__speed = speed
        self.__counter = 0
        self.__color = 0
        self.__list_color: list = colors
        self.__vector = (0, self.__speed)
        self.__width = self.__photo.get_width()
        self.__height = self.__photo.get_height()
        self.__detector_rect = pygame.Rect(self.__xcor, self.__ycor, 2000, self.__height)
        self.__direction = "down"
        self.__type_robot = "Hulk"
        self.__time_change_direction = -10000

    def move(self, x, y):
        x += 0
        y += 0
        if self.__counter % 10 == 0:
            if self.__direction == "up":
                self.__ycor -= self.__speed * 0.7
            elif self.__direction == "down":
                self.__ycor += self.__speed * 0.7
            elif self.__direction == "left":
                self.__xcor -= self.__speed * 1.3
            elif self.__direction == "right":
                self.__xcor += self.__speed * 1.3

    def change_direction(self, x, y, rect: pygame.Rect, counter):
        self.__detector_rect.center = (self.__xcor, self.__ycor)
        if counter - self.__time_change_direction > 2000:
            if self.__detector_rect.colliderect(rect):
                if self.__xcor > x:
                    self.__direction = "left"
                    self.__time_change_direction = pygame.time.get_ticks()
                elif self.__xcor < x:
                    self.__direction = "right"
                    self.__time_change_direction = pygame.time.get_ticks()
            else:
                if self.__ycor > y:
                    self.__direction = "up"
                elif self.__ycor < y:
                    self.__direction = "down"

    def draw(self, surface: pygame.Surface):
        self.__change_img()
        self.__color += 1
        if self.__color >= 25:
            self.__color = 0
        self.__rect = self.__photo.get_rect()
        self.__rect.center = (self.__xcor, self.__ycor)
        pygame.draw.rect(surface, self.__list_color[int(self.__color/5)], self.__rect)
        surface.blit(self.__photo, self.__rect)

    def __change_img(self):
        self.__counter += 1
        if self.__counter >= 40:
            self.__counter = 0
        if self.__counter % 10 == 0:
            if self.__direction == "up" or self.__direction == "down":
                self.__photo = Img.hulk_front[int(self.__counter/10)]
            elif self.__direction == "left":
                self.__photo = Img.hulk_left[int(self.__counter/10)]
            elif self.__direction == "right":
                self.__photo = Img.hulk_right[int(self.__counter/10)]

    def limit(self, up, down, left, right):
        w = self.__photo.get_width()
        h = self.__photo.get_height()
        if self.__ycor - h/2 < up:
            self.__ycor += self.__speed * 1.1
        elif self.__ycor + h/2 > down:
            self.__ycor -= self.__speed * 1.1
        if self.__xcor - w/2 < left:
            self.__xcor += self.__speed * 1.1
        elif self.__xcor + w/2 > right-5:
            self.__xcor -= self.__speed * 1.1

    def get_rect(self):
        return self.__rect

    def get_type(self):
        return self.__type_robot


class Electrodes:
    def __init__(self, x, y, colors):
        self.__photo = random.choice(Img.electrodes)
        self.__rect = self.__photo.get_rect()
        self.__xcor = x
        self.__ycor = y
        self.__colors = colors
        self.__cor = 0
        self.__rect_color = pygame.Rect(x, y, self.__photo.get_width(), self.__photo.get_height())
        self.__delete = False

    def draw(self, surface: pygame.Surface):
        self.__cor += 1
        if self.__cor >= 25:
            self.__cor = 0
        self.__rect_color.center = (self.__xcor, self.__ycor)
        self.__rect.center = (self.__xcor, self.__ycor)
        pygame.draw.rect(surface, self.__colors[int(self.__cor/5)], self.__rect_color)
        surface.blit(self.__photo, self.__rect)

    def set_delete(self):
        self.__delete = True

    def get_delete(self):
        return self.__delete

    def get_rect(self):
        return self.__rect
