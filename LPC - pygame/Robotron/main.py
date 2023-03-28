import pygame
from config import Config
from game import Game
game = Game()
pygame.init()
pygame.font.init()
pygame.joystick.init()
j = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
clock = pygame.time.Clock()

game.intro()
game.title_screen()

while Config.loop_game:
    game.update()
    game.action()
    game.next_wave()
    game.move_people()
    game.draw_people()
    game.delete_people()
    game.creat_robots_family()
    game.take_damage()
    game.shoot()
    game.destroy_robots()
    game.save_family()
    game.choose_target()
    game.dead_people()
    game.change_target()
    game.update_target()
    game.restart_wave()
    game.add_life()
    pygame.display.flip()
    clock.tick(60)

game.game_over(clock)

# game over