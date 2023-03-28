import sys
from config import Config
import pygame


def key_down(event: pygame.event):
    if event.key == pygame.K_RETURN:
        sys.exit()
    if event.key == pygame.K_a:
        Config.list_axes_move[0] = -1
    elif event.key == pygame.K_d:
        Config.list_axes_move[0] = 1
    if event.key == pygame.K_w:
        Config.list_axes_move[1] = 1
    elif event.key == pygame.K_s:
        Config.list_axes_move[1] = -1
    if event.key == pygame.K_j:
        Config.list_axes_shoot[0] = -1
    elif event.key == pygame.K_l:
        Config.list_axes_shoot[0] = 1
    if event.key == pygame.K_i:
        Config.list_axes_shoot[1] = 1
    elif event.key == pygame.K_k:
        Config.list_axes_shoot[1] = -1


def key_up(event: pygame.event):
    if event.key == pygame.K_a:
        Config.list_axes_move[0] = 0
    elif event.key == pygame.K_d:
        Config.list_axes_move[0] = 0
    elif event.key == pygame.K_w:
        Config.list_axes_move[1] = 0
    elif event.key == pygame.K_s:
        Config.list_axes_move[1] = 0
    if event.key == pygame.K_j:
        Config.list_axes_shoot[0] = 0
    elif event.key == pygame.K_l:
        Config.list_axes_shoot[0] = 0
    if event.key == pygame.K_i:
        Config.list_axes_shoot[1] = 0
    elif event.key == pygame.K_k:
        Config.list_axes_shoot[1] = -0


def axes(event: pygame.event):
    # move direction
    if event.axis == 0:
        if event.value > 0.4:
            Config.list_axes_move[0] = 1
        elif event.value < -0.4:
            Config.list_axes_move[0] = -1
        else:
            Config.list_axes_move[0] = 0

    if event.axis == 1:
        if event.value > 0.4:
            Config.list_axes_move[1] = -1
        elif event.value < -0.4:
            Config.list_axes_move[1] = 1
        else:
            Config.list_axes_move[1] = 0

    # shoot direction
    if event.axis == 2:
        if 1.1 > event.value > 0.4:
            Config.list_axes_shoot[0] = 1
        elif -1.1 < event.value < -0.4:
            Config.list_axes_shoot[0] = -1
        else:
            Config.list_axes_shoot[0] = 0

    if event.axis == 3:
        if 1.1 > event.value > 0.4:
            Config.list_axes_shoot[1] = -1
        elif -1.1 < event.value < -0.4:
            Config.list_axes_shoot[1] = 1
        else:
            Config.list_axes_shoot[1] = 0


def last_axes():
    if Config.list_axes_move[0] != 0 or Config.list_axes_move[1] != 0:
        Config.list_axes_move_last[0] = Config.list_axes_move[0]
        Config.list_axes_move_last[1] = Config.list_axes_move[1]
