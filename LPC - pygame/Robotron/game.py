import pygame
import joystick
import screens_elements
import robots
import random
import family
from config import Config
from player import Player
from bullet import Bullet
from rbtext import RainbowText
from pyvidplayer import Video


class Game:
    def __init__(self):
        self.__counter = 0
        self.__wave = 0
        self.__player = Player(Config.screen_w/2, Config.screen_h/2)
        self.__score = 0
        self.__number_human_saves = 0
        self.__number_grunt_destroyed = 0
        self.__last_score = 0
        self.__list_of_bullets = []
        self.__list_of_robots = []
        self.__list_of_electrodes = []
        self.__list_of_family = []
        self.__list_of_death_human = []
        self.__list_of_saved_human = []
        self.__list_target = []
        self.__walls = screens_elements.Walls(Config.screen_w, Config.screen_h)
        self.__limit_up = int(Config.screen_h * 0.05)
        self.__limit_down = int(Config.screen_h * 0.947)
        self.__limit_left = int(Config.screen_w * 0.144)
        self.__limit_right = int(Config.screen_w * 0.855)
        self.score_text = str(self.__score)
        self.rainbow_score_text = RainbowText(Config.screen, self.score_text, Config.font, Config.screen_w * 0.4, Config.screen_h * 0.019, 5)
        self.wave_text = "WAVE  " + str(self.__wave)
        self.rainbow_wave_text = RainbowText(Config.screen, self.wave_text, Config.font, Config.screen_w/2, Config.screen_h * 0.976, 5)
        self.life_text = "LIVES  " + str(self.__player.get_life())
        self.rainbow_life_text = RainbowText(Config.screen, self.life_text, Config.font, Config.screen_w * 0.47, Config.screen_h * 0.019, 5)
        self.__video_intro = "video"

    def intro(self):
        if Config.loop_intro:
            self.__video_intro = Video("IntroVideo.mp4")
            self.__video_intro.set_size((1366, 768))
        while Config.loop_intro:
            self.__video_intro.draw(Config.screen, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.JOYBUTTONDOWN:
                    self.__video_intro.close()
                    Config.loop_intro = False

    def title_screen(self):
        while Config.loop_game:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.KEYDOWN:
                    Config.loop_game = False
            Config.screen.fill(Config.black)
            rect = self.__walls.title_img.get_rect()
            rect.center = (Config.screen_w/2, Config.screen_h/2)
            Config.screen.blit(self.__walls.title_img, rect)
            pygame.display.flip()
        Config.loop_game = True

    def update(self):
        self.__counter = pygame.time.get_ticks()
        Config.screen.fill(Config.black)
        self.__walls.draw_walls(Config.screen, Config.yellow)
        self.rainbow_score_text.update()
        self.rainbow_score_text.text = str(self.__score)
        self.rainbow_wave_text.update()
        self.rainbow_wave_text.text = "WAVE  " + str(self.__wave)
        self.rainbow_life_text.update()
        self.rainbow_life_text.text = "LIVES  " + str(self.__player.get_life())

    def action(self):
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                joystick.axes(event)
            if event.type == pygame.KEYDOWN:
                joystick.key_down(event)
            if event.type == pygame.KEYUP:
                joystick.key_up(event)
        joystick.last_axes()

    def move_people(self):
        if not self.__player.get_death():
            self.__player.move()
            self.__player.spin(Config.list_axes_move[0], Config.list_axes_move[1])
            self.__player.limit(self.__limit_up, self.__limit_down, self.__limit_left, self.__limit_right)
            for bullet in self.__list_of_bullets:
                bullet.move()
            for robot in self.__list_of_robots:
                robot.move(self.__player.get_x(), self.__player.get_y())
                robot.limit(self.__limit_up, self.__limit_down, self.__limit_left, self.__limit_right)
            for human in self.__list_of_family:
                human.move()
                human.limit(self.__limit_up, self.__limit_down, self.__limit_left, self.__limit_right)
                human.change_vector(self.__counter)

    def draw_people(self):
        self.__player.draw_player()
        for bullet in self.__list_of_bullets:
            bullet.draw()
        for robot in self.__list_of_robots:
            robot.draw(Config.screen)
        for human in self.__list_of_family:
            human.draw(Config.screen)
        for human in self.__list_of_death_human:
            human.draw(Config.screen)
        for human in self.__list_of_saved_human:
            human.draw(Config.screen)
        for electrode in self.__list_of_electrodes:
            electrode.draw(Config.screen)

    def delete_people(self):
        for bullet in self.__list_of_bullets:
            if bullet.get_delete():
                self.__list_of_bullets.remove(bullet)
                break
        for human in self.__list_of_death_human:
            if human.get_delete():
                self.__list_of_death_human.remove(human)
                break
        for human in self.__list_of_saved_human:
            if human.get_delete():
                self.__list_of_saved_human.remove(human)
                break
        for electrode in self.__list_of_electrodes:
            if electrode.get_delete():
                self.__list_of_electrodes.remove(electrode)
                break

    def creat_robots_family(self):
        if Config.restart:
            self.__type_wave()
            self.__list_of_robots.clear()
            self.__list_of_bullets.clear()
            x, y = 300, 300
            for a in range(Config.number_robots):
                up_or_down = random.randint(1, 2)
                left_or_right = random.randint(1, 2)
                type_robot = random.randint(1, 2)
                robot = 1
                if up_or_down == 1:
                    y = random.randint(self.__limit_up, Config.screen_h/2 - 50)
                elif up_or_down == 2:
                    y = random.randint(Config.screen_h/2 + 50, self.__limit_down)
                if left_or_right == 1:
                    x = random.randint(self.__limit_left, Config.screen_w/2 - 50)
                elif left_or_right == 2:
                    x = random.randint(Config.screen_w/2 + 50, self.__limit_right)
                if type_robot == 1:
                    robot = robots.Grunt(x, y, Config.speed_grunt)
                elif type_robot == 2:
                    robot = robots.Hulk(x, y, Config.speed_hulk, Config.colors)
                self.__list_of_robots.append(robot)

            self.__list_of_family.clear()
            for a in range(Config.number_family):
                up_or_down = random.randint(1, 2)
                left_or_right = random.randint(1, 2)
                if up_or_down == 1:
                    y = random.randint(self.__limit_up, Config.screen_h / 2 - 50)
                elif up_or_down == 2:
                    y = random.randint(Config.screen_h / 2 + 50, self.__limit_down)
                if left_or_right == 1:
                    x = random.randint(self.__limit_left, Config.screen_w / 2 - 50)
                elif left_or_right == 2:
                    x = random.randint(Config.screen_w / 2 + 50, self.__limit_right)
                human = family.Human(x, y, Config.speed_human)
                self.__list_of_family.append(human)

            self.__list_of_electrodes.clear()
            for a in range(Config.number_of_electrodes):
                up_or_down = random.randint(1, 2)
                left_or_right = random.randint(1, 2)
                if up_or_down == 1:
                    y = random.randint(self.__limit_up + 20, Config.screen_h / 2 - 50)
                elif up_or_down == 2:
                    y = random.randint(Config.screen_h / 2 + 50, self.__limit_down - 20)
                if left_or_right == 1:
                    x = random.randint(self.__limit_left + 20, Config.screen_w / 2 - 50)
                elif left_or_right == 2:
                    x = random.randint(Config.screen_w / 2 + 50, self.__limit_right - 20)
                electrodes = robots.Electrodes(x, y, Config.colors)
                self.__list_of_electrodes.append(electrodes)

    def __type_wave(self):
        if self.__wave < 2:
            Config.number_robots = 30
        elif self.__wave % 2 == 0:
            Config.number_robots += 5

    def take_damage(self):
        for robot in self.__list_of_robots:
            self.__player.damage(robot.get_rect(), Config.explosion)
        for electrode in self.__list_of_electrodes:
            self.__player.damage(electrode.get_rect(), Config.explosion)
        if self.__player.get_life() <= 0:
            Config.loop_game = False

    def restart_wave(self):
        if Config.restart:
            Config.transition.play()
            Config.restart = False
        if self.__player.get_death():
            self.__player.respawn(self.__counter, Config.screen_w/2, Config.screen_h/2)

    def shoot(self):
        if (self.__counter - self.__player.get_recharge() > Config.time_recharge * 1000
                and (Config.list_axes_shoot[0] != 0 or Config.list_axes_shoot[1] != 0)) and not self.__player.get_death():
            bullet = Bullet(self.__player.get_x(), self.__player.get_y())
            bullet.select_angle(Config.list_axes_shoot[0], Config.list_axes_shoot[1])
            self.__list_of_bullets.append(bullet)
            self.__player.set_recharge()
            Config.shoot1.play()

    def destroy_robots(self):
        for bullet in self.__list_of_bullets:
            for robot in self.__list_of_robots:
                if bullet.get_rect().colliderect(robot.get_rect()):
                    Config.explosion.play()
                    if robot.get_type() == "Grunt":
                        self.__list_of_robots.remove(robot)
                        bullet.set_delete()
                        self.__score += 100
                        self.__number_grunt_destroyed += 1
                    if robot.get_type() == "Hulk":
                        bullet.set_delete()
            for electrode in self.__list_of_electrodes:
                if bullet.get_rect().colliderect(electrode.get_rect()):
                    electrode.set_delete()
                    bullet.set_delete()

    def save_family(self):
        for human in self.__list_of_family:
            human.save(self.__player.get_rect(), Config.red)
            if human.get_saved():
                self.__list_of_saved_human.append(human)
                self.__list_of_family.remove(human)
                self.__score += 1000
                self.__number_human_saves += 1

    def choose_target(self):
        if Config.restart:
            self.__list_target.clear()
            n = 0
            for human in self.__list_of_family:
                self.__list_target.append(human)
                if n < len(self.__list_of_family):
                    n += 1

    def dead_people(self):
        n = -1
        for human in self.__list_of_family:
            n += 1
            for robot in self.__list_of_robots:
                if robot.get_type() == "Hulk":
                    human.dead(robot.get_rect())
                    if human.get_death():
                        self.__list_of_death_human.append(human)
                        self.__list_of_family.remove(human)
                        break

    def change_target(self):
        n = 0
        self.__list_target.clear()
        for human in self.__list_of_family:
            if n < 3:
                self.__list_target.append(human)
                n += 1

    def update_target(self):
        n = 0
        for robot in self.__list_of_robots:
            if n >= 3 or n >= len(self.__list_target):
                n = 0
            if robot.get_type() == "Hulk" and len(self.__list_target) != 0:
                robot.change_direction(self.__list_target[n].get_x(), self.__list_target[n].get_y(),
                                       self.__list_target[n].get_rect(), self.__counter)
                n += 1
            if len(self.__list_target) == 0 and robot.get_type() == "Hulk":
                robot.change_direction(self.__player.get_x(), self.__player.get_y(), self.__player.get_rect(), self.__counter)

    def next_wave(self):
        n = 0
        for robot in self.__list_of_robots:
            if robot.get_type() == "Grunt":
                n += 1
        if n == 0:
            Config.restart = True
            self.__wave += 1
            self.__player.respawn_player(Config.screen_w/2, Config.screen_h/2)
            Config.transition.play()

    def add_life(self):
        if self.__score // 25000 > self.__last_score:
            self.__last_score = self.__score // 25000
            self.__player.add_life()

    def game_over(self, clock: pygame.time.Clock):
        loop = True
        text = "YOU LOSE"
        font = pygame.font.Font("assets/Minecraft.ttf", 70)
        game_over_text = RainbowText(Config.screen, text, font, Config.screen_w/2, Config.screen_h/4, 5)
        text_score = "YOUR SCORE: " + str(self.__score)
        score = RainbowText(Config.screen, text_score, Config.font, Config.screen_w/2, Config.screen_h/3, 5)
        humans_saved = "HUMANS SAVED: " + str(self.__number_human_saves)
        robots_destroyed = "GRUNTS DESTROYED: " + str(self.__number_grunt_destroyed)
        humans_saved_text = RainbowText(Config.screen, humans_saved, Config.font, Config.screen_w/2, Config.screen_h/3 * 1.1, 5)
        robots_destroyed_text = RainbowText(Config.screen, robots_destroyed, Config.font, Config.screen_w/2, Config.screen_h/3 * 1.2, 5)
        text = "developers: Lucas Trovao, Rahilson Dias, Victor Emanuel, Giulia Sales, Leonardo Castro"
        devs_text = RainbowText(Config.screen, text, Config.font, Config.screen_w/2, Config.screen_h/2 * 1.7, 5)
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.KEYDOWN:
                    loop = False
            Config.screen.fill(Config.black)
            game_over_text.update()
            devs_text.update()
            score.update()
            humans_saved_text.update()
            robots_destroyed_text.update()
            pygame.display.flip()
            clock.tick(60)
