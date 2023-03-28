import pygame
pygame.font.init()
pygame.mixer.init()


class Config:
    black = (0, 0, 0)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    purple = (148, 0, 211)

    screen_w = 1366
    screen_h = 768
    # , pygame.FULLSCREEN | pygame.SCALED
    screen = pygame.display.set_mode((screen_w, screen_h), pygame.WINDOWMAXIMIZED)

    speed = 5
    list_axes_move = [0, 0]
    list_axes_move_last = [0, -1]
    list_axes_shoot = [0, 0]

    speed_grunt = 8
    number_robots = 20
    restart = True
    speed_hulk = 8
    colors = [yellow, red, green, blue, purple]
    number_of_electrodes = 20

    number_family = 10
    speed_human = 6

    speed_bullet = 20
    time_recharge = 0.12

    font = pygame.font.Font("assets/Minecraft.ttf", 25)

    intro = pygame.mixer.Sound("assets/sounds/Intro.mp3")
    shoot1 = pygame.mixer.Sound("assets/sounds/Shoot1.wav")
    shoot2 = pygame.mixer.Sound("assets/sounds/Shoot2.mp3")
    transition = pygame.mixer.Sound("assets/sounds/Transition.mp3")
    explosion = pygame.mixer.Sound("assets/sounds/Explosion.wav")

    loop_game = True
    loop_intro = True
