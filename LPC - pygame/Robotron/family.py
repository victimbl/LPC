import pygame
import random
from sprite_player import Img


class Human:
    def __init__(self, x, y, speed):
        self.person = random.randint(1, 3)
        if self.person == 1:
            self.__front = Img.list_daddy_front
            self.__behind = Img.list_daddy_behind
            self.__left = Img.list_daddy_left
            self.__right = Img.list_daddy_right
        elif self.person == 2:
            self.__front = Img.list_mommy_front
            self.__behind = Img.list_mommy_behind
            self.__left = Img.list_mommy_left
            self.__right = Img.list_mommy_right
        elif self.person == 3:
            self.__front = Img.list_mike_front
            self.__behind = Img.list_mike_behind
            self.__left = Img.list_mike_left
            self.__right = Img.list_mike_right
        self.__photo = Img.daddy_front_stop
        self.__rect = self.__photo.get_rect()
        self.__speed = speed
        self.__xcor = x
        self.__ycor = y
        self.__direction1 = "down"
        self.__direction2 = "nothing"
        self.__vector = (0, self.__speed)
        self.__death = False
        self.__saved = False
        self.__delete = False
        self.__counter = 0
        self.__time_change_direction = -10000
        self.__n = 0

    def move(self):
        self.__n += 1
        if not self.__death and self.__counter % 10 == 0 and not self.__saved:
            self.__xcor += self.__vector[0]
            self.__ycor += self.__vector[1]

    def draw(self, surface: pygame.Surface):
        self.__change_img()
        self.__rect = self.__photo.get_rect()
        self.__rect.center = (self.__xcor, self.__ycor)
        surface.blit(self.__photo, self.__rect)

    def __change_img(self):
        if not self.__death and not self.__saved:
            self.__counter += 1
            if self.__counter >= 40:
                self.__counter = 0
            if self.__direction1 == "up":
                self.__photo = self.__behind[int(self.__counter/10)]
            elif self.__direction1 == "down":
                self.__photo = self.__front[int(self.__counter/10)]
            elif self.__direction1 == "left":
                self.__photo = self.__left[int(self.__counter/10)]
            elif self.__direction1 == "right":
                self.__photo = self.__right[int(self.__counter/10)]
        elif self.__death:
            self.__counter += 1
            if self.__counter >= 80:
                self.__delete = True
        elif self.__saved:
            self.__counter += 1
            if self.__counter >= 80:
                self.__delete = True

    def change_vector(self, counter):
        if counter - self.__time_change_direction > 6000:
            self.__time_change_direction = pygame.time.get_ticks()
            list_directions1 = ["up", "down", "left", "right"]
            list_directions2 = ["upper_diagonal", "lower_diagonal", "normal"]
            self.__direction1 = random.choice(list_directions1)
            self.__direction2 = random.choice(list_directions2)

            if self.__direction1 == "up":
                self.__vector = (0, -self.__speed)
            elif self.__direction1 == "down":
                self.__vector = (0, self.__speed)
            elif self.__direction1 == "left":
                if self.__direction2 == "upper_diagonal":
                    self.__vector = (-self.__speed * 0.5, -self.__speed * 0.5)
                elif self.__direction2 == "lower_diagonal":
                    self.__vector = (-self.__speed * 0.5, self.__speed * 0.5)
                else:
                    self.__vector = (-self.__speed, 0)
            elif self.__direction1 == "right":
                if self.__direction2 == "upper_diagonal":
                    self.__vector = (self.__speed * 0.5, -self.__speed * 0.5)
                elif self.__direction2 == "lower_diagonal":
                    self.__vector = (self.__speed * 0.5, self.__speed * 0.5)
                else:
                    self.__vector = (self.__speed, 0)

    def dead(self, rect: pygame.Rect):
        if self.__rect.colliderect(rect) and not self.__death and self.__n > 100:
            self.__photo = Img.family_death
            self.__death = True
            self.__counter = 0

    def save(self, rect: pygame.Rect, color):
        if self.__rect.colliderect(rect) and not self.__death and self.__n > 100:
            self.__photo = Img.family_saved.render("1000", True, color)
            self.__rect = self.__photo.get_rect()
            self.__saved = True

    def limit(self, up, down, left, right):
        w = self.__photo.get_width()
        h = self.__photo.get_height()
        if self.__ycor - h/2 < up:
            self.__ycor += abs(self.__vector[1] * 1.1)
        elif self.__ycor + h/2 > down:
            self.__ycor -= abs(self.__vector[1] * 1.1)
        if self.__xcor - w/2 < left:
            self.__xcor += abs(self.__vector[0] * 1.1)
        elif self.__xcor + w/2 > right-5:
            self.__xcor -= abs(self.__vector[0] * 1.1)

    def get_rect(self):
        return self.__rect

    def get_death(self):
        return self.__death

    def get_saved(self):
        return self.__saved

    def get_x(self):
        return self.__xcor

    def get_y(self):
        return self.__ycor

    def get_delete(self):
        return self.__delete

