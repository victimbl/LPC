import pygame
from config import Config
from sprite_player import Img


class Player:
    def __init__(self, x, y):
        self.__photo = pygame.image.load("assets/player/body/front_stop.png")
        self.__eyes = Img.front_eyes1
        self.__rect = self.__photo.get_rect()
        self.__width = self.__photo.get_width()
        self.__height = self.__photo.get_height()
        self.__xcor = x
        self.__ycor = y
        self.__vector_init = pygame.Vector2(0, -Config.speed)
        self.__vector = self.__vector_init
        self.__time_recharge = 0
        self.__movement = False
        self.__death = False
        self.__spawn = True
        self.__counter1 = 0
        self.__counter2 = 0
        self.__counter_spawn = 0
        self.__angle = 180
        self.__time_dead = 0
        self.__life = 3

    def draw_player(self):
        if not self.__death and not self.__spawn:
            self.__change_img()
            self.__rect = self.__photo.get_rect()
            self.__rect.center = (self.__xcor, self.__ycor)
            Config.screen.blit(self.__photo, self.__rect)
            Config.screen.blit(self.__eyes, self.__rect)
        if self.__spawn:
            self.__photo = Img.list_img_spawn[int(self.__counter_spawn/2)]
            self.__rect = self.__photo.get_rect()
            self.__rect.center = (self.__xcor, self.__ycor)
            Config.screen.blit(self.__photo, self.__rect)
            self.__counter_spawn += 1
            if self.__counter_spawn >= 26:
                self.__spawn = False
                self.__counter_spawn = 0
                self.__rect = Img.front_stop.get_rect()

    def move(self):
        self.__xcor += self.__vector[0]
        self.__ycor += self.__vector[1]

        # limit
        self.__rect = self.__photo.get_rect()
        if self.__xcor <= self.__width / 2 or self.__xcor >= Config.screen_w - self.__width / 2:
            self.__xcor -= self.__vector[0]
        if self.__ycor <= self.__height / 2 or self.__ycor >= Config.screen_h - self.__height / 2:
            self.__ycor -= self.__vector[1]

    def spin(self, x, y):
        if x != 0 or y != 0:
            self.__movement = True
        if x == 0 and y == 0:
            self.__vector = (0, 0)
            self.__movement = False
        elif x == 0 and y == 1:
            self.__vector = self.__vector_init.rotate(0)
        elif x == 1 and y == 1:
            self.__vector = self.__vector_init.rotate(45)
        elif x == 1 and y == 0:
            self.__vector = self.__vector_init.rotate(90)
        elif x == 1 and y == -1:
            self.__vector = self.__vector_init.rotate(135)
        elif x == 0 and y == -1:
            self.__vector = self.__vector_init.rotate(180)
        elif x == -1 and y == -1:
            self.__vector = self.__vector_init.rotate(225)
        elif x == -1 and y == 0:
            self.__vector = self.__vector_init.rotate(270)
        elif x == -1 and y == 1:
            self.__vector = self.__vector_init.rotate(315)

    def __change_img(self):
        self.__counter1 += 0.2
        self.__counter2 += 0.2
        if self.__counter1 >= 2:
            self.__counter1 = 0
        if self.__counter2 >= 4:
            self.__counter2 = 0
        if Config.list_axes_move_last[0] == 0 and Config.list_axes_move_last[1] == -1:
            self.__photo = Img.front_stop
            self.__eyes = Img.front_eyes[int(self.__counter2)]
            if self.__movement:
                n = int(self.__counter1)
                self.__photo = Img.front_walk[n]
        elif Config.list_axes_move_last[0] == 0 and Config.list_axes_move_last[1] == 1:
            self.__photo = Img.behind_stop
            self.__eyes = Img.back_eyes[int(self.__counter2)]
            if self.__movement:
                n = int(self.__counter1)
                self.__photo = Img.behind_walk[n]
        elif Config.list_axes_move_last[0] == -1:
            self.__photo = Img.left_stop
            self.__eyes = Img.left_eyes[int(self.__counter2)]
            if self.__movement:
                n = int(self.__counter1)
                self.__photo = Img.left_walk[n]
        elif Config.list_axes_move_last[0] == 1:
            self.__photo = Img.right_stop
            self.__eyes = Img.right_eyes[int(self.__counter2)]
            if self.__movement:
                n = int(self.__counter1)
                self.__photo = Img.right_walk[n]

    def damage(self, rect: pygame.Rect, sound: pygame.mixer.Sound):
        if self.__rect.colliderect(rect) and not self.__death and not self.__spawn:
            self.__death = True
            self.__time_dead = pygame.time.get_ticks()
            self.__life -= 1
            sound.play()

    def respawn(self, counter, x, y):
        if counter - self.__time_dead > 2000 and self.__death and not self.__spawn:
            self.__spawn = True
            self.__death = False
            self.__xcor = x
            self.__ycor = y
            Config.restart = True

    def limit(self, up, down, left, right):
        w = self.__photo.get_width()
        h = self.__photo.get_height()
        if self.__ycor - h/2 < up:
            self.__ycor += abs(self.__vector[1]) * 1.1
        elif self.__ycor + h/2 > down:
            self.__ycor -= abs(self.__vector[1]) * 1.1
        if self.__xcor - w/2 < left:
            self.__xcor += abs(self.__vector[0]) * 1.1
        elif self.__xcor + w/2 > right-5:
            self.__xcor -= abs(self.__vector[0]) * 1.1

    def add_life(self):
        self.__life += 1

    def get_life(self):
        return self.__life

    def set_recharge(self):
        self.__time_recharge = pygame.time.get_ticks()

    def get_recharge(self):
        return self.__time_recharge

    def get_x(self):
        return self.__xcor

    def get_y(self):
        return self.__ycor

    def get_rect(self):
        return self.__rect

    def get_death(self):
        return self.__death

    def respawn_player(self, x, y):
        self.__spawn = True
        self.__xcor = x
        self.__ycor = y

