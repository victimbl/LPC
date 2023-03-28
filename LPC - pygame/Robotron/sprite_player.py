import pygame
pygame.font.init()


class Img:
    front_walking1 = pygame.image.load("assets/player/body/front_walking1.png")
    front_walking2 = pygame.image.load("assets/player/body/front_walking2.png")
    front_stop = pygame.image.load("assets/player/body/front_stop.png")
    behind_stop = pygame.image.load("assets/player/body/behind_stop.png")
    behind_walking1 = pygame.image.load("assets/player/body/behind_walking1.png")
    behind_walking2 = pygame.image.load("assets/player/body/behind_walking2.png")
    left_stop = pygame.image.load("assets/player/body/left_stop.png")
    left_walking = pygame.image.load("assets/player/body/left_walking.png")
    right_stop = pygame.image.load("assets/player/body/right_stop.png")
    right_walking = pygame.image.load("assets/player/body/right_walking.png")

    front_walk = [front_walking1, front_walking2]
    behind_walk = [behind_walking1, behind_walking2]
    left_walk = [left_stop, left_walking]
    right_walk = [right_stop, right_walking]

    back_eyes1 = pygame.image.load("assets/player/eyes/back_eyes1.png")
    back_eyes2 = pygame.image.load("assets/player/eyes/back_eyes2.png")
    back_eyes3 = pygame.image.load("assets/player/eyes/back_eyes3.png")
    back_eyes4 = pygame.image.load("assets/player/eyes/back_eyes4.png")
    front_eyes1 = pygame.image.load("assets/player/eyes/front_eyes1.png")
    front_eyes2 = pygame.image.load("assets/player/eyes/front_eyes2.png")
    front_eyes3 = pygame.image.load("assets/player/eyes/front_eyes3.png")
    front_eyes4 = pygame.image.load("assets/player/eyes/front_eyes4.png")
    left_eyes1 = pygame.image.load("assets/player/eyes/left_eyes1.png")
    left_eyes2 = pygame.image.load("assets/player/eyes/left_eyes2.png")
    left_eyes3 = pygame.image.load("assets/player/eyes/left_eyes3.png")
    left_eyes4 = pygame.image.load("assets/player/eyes/left_eyes4.png")
    right_eyes1 = pygame.image.load("assets/player/eyes/right_eyes1.png")
    right_eyes2 = pygame.image.load("assets/player/eyes/right_eyes2.png")
    right_eyes3 = pygame.image.load("assets/player/eyes/right_eyes3.png")
    right_eyes4 = pygame.image.load("assets/player/eyes/right_eyes4.png")

    back_eyes = [back_eyes1, back_eyes2, back_eyes3, back_eyes4]
    front_eyes = [front_eyes1, front_eyes2, front_eyes3, front_eyes4]
    left_eyes = [left_eyes1, left_eyes2, left_eyes3, left_eyes4]
    right_eyes = [right_eyes1, right_eyes2, right_eyes3, right_eyes4]

    spawn1 = pygame.image.load("assets/player/spawn img/img1.png")
    spawn2 = pygame.image.load("assets/player/spawn img/img2.png")
    spawn3 = pygame.image.load("assets/player/spawn img/img3.png")
    spawn4 = pygame.image.load("assets/player/spawn img/img4.png")
    spawn5 = pygame.image.load("assets/player/spawn img/img5.png")
    spawn6 = pygame.image.load("assets/player/spawn img/img6.png")
    spawn7 = pygame.image.load("assets/player/spawn img/img7.png")
    spawn8 = pygame.image.load("assets/player/spawn img/img8.png")
    spawn9 = pygame.image.load("assets/player/spawn img/img9.png")
    spawn10 = pygame.image.load("assets/player/spawn img/img10.png")
    spawn11 = pygame.image.load("assets/player/spawn img/img11.png")
    spawn12 = pygame.image.load("assets/player/spawn img/img12.png")
    spawn13 = pygame.image.load("assets/player/spawn img/img13.png")
    list_img_spawn = [spawn1, spawn2, spawn3, spawn4, spawn5, spawn6, spawn7, spawn8, spawn9, spawn10, spawn11,
                      spawn12, spawn13]

    grunt_stop = pygame.image.load("assets/robots/robot1/body/stop.png")
    grunt_walking1 = pygame.image.load("assets/robots/robot1/body/walking1.png")
    grunt_walking2 = pygame.image.load("assets/robots/robot1/body/walking2.png")
    list_grunt = [grunt_stop, grunt_walking1, grunt_stop, grunt_walking2]

    grunt_eye1 = pygame.image.load("assets/robots/robot1/eyes/eyes1.png")
    grunt_eye2 = pygame.image.load("assets/robots/robot1/eyes/eyes2.png")
    grunt_eye3 = pygame.image.load("assets/robots/robot1/eyes/eyes3.png")
    grunt_eye4 = pygame.image.load("assets/robots/robot1/eyes/eyes4.png")
    list_grunt_eyes = [grunt_eye1, grunt_eye2, grunt_eye3, grunt_eye4]

    daddy_front_stop = pygame.image.load("assets/family/daddy/front_stop.png")
    daddy_front_walk1 = pygame.image.load("assets/family/daddy/front_walk1.png")
    daddy_front_walk2 = pygame.image.load("assets/family/daddy/front_walk2.png")
    daddy_behind_stop = pygame.image.load("assets/family/daddy/behind_stop.png")
    daddy_behind_walk1 = pygame.image.load("assets/family/daddy/behind_walk1.png")
    daddy_behind_walk2 = pygame.image.load("assets/family/daddy/behind_walk2.png")
    daddy_left_stop = pygame.image.load("assets/family/daddy/left_stop.png")
    daddy_left_walk1 = pygame.image.load("assets/family/daddy/left_walk1.png")
    daddy_left_walk2 = pygame.image.load("assets/family/daddy/left_walk2.png")
    daddy_right_stop = pygame.image.load("assets/family/daddy/right_stop.png")
    daddy_right_walk1 = pygame.image.load("assets/family/daddy/right_walk1.png")
    daddy_right_walk2 = pygame.image.load("assets/family/daddy/right_walk2.png")
    list_daddy_front = [daddy_front_stop, daddy_front_walk1, daddy_front_stop, daddy_front_walk2]
    list_daddy_behind = [daddy_behind_stop, daddy_behind_walk1, daddy_behind_stop, daddy_behind_walk2]
    list_daddy_left = [daddy_left_stop, daddy_left_walk1, daddy_left_stop, daddy_left_walk2]
    list_daddy_right = [daddy_right_stop, daddy_right_walk1, daddy_right_stop, daddy_right_walk2]

    mommy_front_stop = pygame.image.load("assets/family/mommy/front_stop.png")
    mommy_front_walk1 = pygame.image.load("assets/family/mommy/front_walk1.png")
    mommy_front_walk2 = pygame.image.load("assets/family/mommy/front_walk2.png")
    mommy_behind_stop = pygame.image.load("assets/family/mommy/behind_stop.png")
    mommy_behind_walk1 = pygame.image.load("assets/family/mommy/behind_walk1.png")
    mommy_behind_walk2 = pygame.image.load("assets/family/mommy/behind_walk2.png")
    mommy_left_stop = pygame.image.load("assets/family/mommy/left_stop.png")
    mommy_left_walk1 = pygame.image.load("assets/family/mommy/left_walk1.png")
    mommy_left_walk2 = pygame.image.load("assets/family/mommy/left_walk2.png")
    mommy_right_stop = pygame.image.load("assets/family/mommy/right_stop.png")
    mommy_right_walk1 = pygame.image.load("assets/family/mommy/right_walk1.png")
    mommy_right_walk2 = pygame.image.load("assets/family/mommy/right_walk2.png")
    list_mommy_front = [mommy_front_stop, mommy_front_walk1, mommy_front_stop, mommy_front_walk2]
    list_mommy_behind = [mommy_behind_stop, mommy_behind_walk1, mommy_behind_stop, mommy_behind_walk2]
    list_mommy_left = [mommy_left_stop, mommy_left_walk1, mommy_left_stop, mommy_left_walk2]
    list_mommy_right = [mommy_right_stop, mommy_right_walk1, mommy_right_stop, mommy_right_walk2]

    mike_front_stop = pygame.image.load("assets/family/mike/front_stop.png")
    mike_front_walk1 = pygame.image.load("assets/family/mike/front_walk1.png")
    mike_front_walk2 = pygame.image.load("assets/family/mike/front_walk2.png")
    mike_behind_stop = pygame.image.load("assets/family/mike/behind_stop.png")
    mike_behind_walk1 = pygame.image.load("assets/family/mike/behind_walk1.png")
    mike_behind_walk2 = pygame.image.load("assets/family/mike/behind_walk2.png")
    mike_left_stop = pygame.image.load("assets/family/mike/left_stop.png")
    mike_left_walk1 = pygame.image.load("assets/family/mike/left_walk1.png")
    mike_left_walk2 = pygame.image.load("assets/family/mike/left_walk2.png")
    mike_right_stop = pygame.image.load("assets/family/mike/right_stop.png")
    mike_right_walk1 = pygame.image.load("assets/family/mike/right_walk1.png")
    mike_right_walk2 = pygame.image.load("assets/family/mike/right_walk2.png")
    list_mike_front = [mike_front_stop, mike_front_walk1, mike_front_stop, mike_front_walk2]
    list_mike_behind = [mike_behind_stop, mike_behind_walk1, mike_behind_stop, mike_behind_walk2]
    list_mike_left = [mike_left_stop, mike_left_walk1, mike_left_stop, mike_left_walk2]
    list_mike_right = [mike_right_stop, mike_right_walk1, mike_right_stop, mike_right_walk2]

    family_death = pygame.image.load("assets/family/death.png")
    family_saved = pygame.font.Font("assets/Minecraft.ttf", 25)

    hulk_front_stop = pygame.image.load("assets/robots/robot2/front_stop.png")
    hulk_front_walk1 = pygame.image.load("assets/robots/robot2/front_walk1.png")
    hulk_front_walk2 = pygame.image.load("assets/robots/robot2/front_walk2.png")
    hulk_left_stop = pygame.image.load("assets/robots/robot2/left_stop.png")
    hulk_left_walk1 = pygame.image.load("assets/robots/robot2/left_walk1.png")
    hulk_left_walk2 = pygame.image.load("assets/robots/robot2/left_walk2.png")
    hulk_right_stop = pygame.image.load("assets/robots/robot2/right_stop.png")
    hulk_right_walk1 = pygame.image.load("assets/robots/robot2/right_walk1.png")
    hulk_right_walk2 = pygame.image.load("assets/robots/robot2/right_walk2.png")
    hulk_front = [hulk_front_stop, hulk_front_walk1, hulk_front_stop, hulk_front_walk2]
    hulk_left = [hulk_left_stop, hulk_left_walk1, hulk_left_stop, hulk_left_walk2]
    hulk_right = [hulk_right_stop, hulk_right_walk1, hulk_right_stop, hulk_right_walk2]

    electrode1 = pygame.image.load("assets/robots/robot3/electrodos 1.png")
    electrode2 = pygame.image.load("assets/robots/robot3/electrodos 2.png")
    electrode3 = pygame.image.load("assets/robots/robot3/electrodos 3.png")
    electrode4 = pygame.image.load("assets/robots/robot3/electrodos 4.png")
    electrode5 = pygame.image.load("assets/robots/robot3/electrodos 5.png")
    electrode6 = pygame.image.load("assets/robots/robot3/electrodos 6.png")
    electrode7 = pygame.image.load("assets/robots/robot3/electrodos 7.png")
    electrodes = [electrode1, electrode2, electrode3, electrode4, electrode5, electrode6, electrode7]

