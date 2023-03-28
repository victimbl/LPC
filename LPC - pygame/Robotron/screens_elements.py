import pygame


class Walls:
    def __init__(self, screen_x, screen_y):
        self.up_wall = pygame.Rect(screen_x * 0.144, screen_y * 0.05, screen_x * 0.855 - screen_x * 0.144, 5)
        self.down_wall = pygame.Rect(screen_x * 0.144, screen_y * 0.947, screen_x * 0.855 - screen_x * 0.144 + 5, 5)
        self.left_wall = pygame.Rect(screen_x * 0.144, screen_y * 0.05, 5, screen_y * 0.947 - screen_y * 0.05)
        self.right_wall = pygame.Rect(screen_x * 0.855, screen_y * 0.05, 5, screen_y * 0.947 - screen_y * 0.05)
        self.list_walls = [self.up_wall, self.down_wall, self.left_wall, self.right_wall]

    def draw_walls(self, surf: pygame.Surface, cor):
        for wall in self.list_walls:
            pygame.draw.rect(surf, cor, wall)

    def get_walls(self):
        return self.list_walls

    title_img = pygame.image.load("assets/title.png")
