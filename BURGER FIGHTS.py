import pygame
import sys
import random
from pygame import mixer

#Initializing:
pygame.init()
pygame.font.init()

pygame.mixer.pre_init(44100, -16, 2, 512)

#Display:
Window_size = (800,500)
screen = pygame.display.set_mode(Window_size,0,32)
display = pygame.Surface((800,400))

#time:
mainClock = pygame.time.Clock()
background_count = 0
air_timer = 0
title_down_count1 = 0
title_up_count1 = 0
title_down_count2 = 0
title_up_count2 = 0
instruction_count = 0
restart_game_count = 0

#Sound:
mixer.music.load("burger.wav")
mixer.music.play(-1)
jump_sound = mixer.Sound("jump2.wav")
jump_sound.set_volume(0.2)
click_sound = mixer.Sound("click.wav")
sword_sound = mixer.Sound("sword.wav")
sword_sound.set_volume(0.3)

#Colours:
White = (255,255,255)
Black = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)
hp_yellow = (246,202,32)
hp_red = (218,41,28)

#Game States:
start_screen = True
game_screen = False
play_again_screen = False
change_game_state = False

#Background:
background_1 = pygame.image.load("start_screen_background0%.png")
background_1 = pygame.transform.scale(background_1, (800,400))
background_2 = pygame.image.load("start_screen_background10%.png")
background_2 = pygame.transform.scale(background_2, (800,400))
background_3 = pygame.image.load("start_screen_background20%.png")
background_3 = pygame.transform.scale(background_3, (800,400))
background_4 = pygame.image.load("start_screen_backgroun40%.png")
background_4 = pygame.transform.scale(background_4, (800,400))
background_5 = pygame.image.load("start_screen_backgroun90%.png")
background_5 = pygame.transform.scale(background_5, (800,400))
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (800, 400))
background2 = pygame.image.load("game_sword.jpg")
background2 = pygame.transform.scale(background2,(400,400))
background3 = pygame.image.load("background.jpg")
background3 = pygame.transform.scale(background3,(800,400))

#Image Assets:
play_button = pygame.image.load("play button.png")
play_button = pygame.transform.scale(play_button, (180,65))
play_button_small = pygame.image.load("play button.png")
play_button_small = pygame.transform.scale(play_button_small, (148,41))
hover = False
click = False

player_right = pygame.image.load("neutral_right.png")
player_right = pygame.transform.scale(player_right, (160,130))
player_left = pygame.image.load("neutral_left.png")
player_left = pygame.transform.scale(player_left, (160,130))

platform_size = [50,40]
platform = pygame.image.load("jump.png")
platform = pygame.transform.scale(platform,(platform_size[0],platform_size[1]))

title1 = pygame.image.load("title1.png")
title1 = pygame.transform.scale(title1,(600,150))
title2 = pygame.image.load("title2.png")
title2 = pygame.transform.scale(title2,(600,150))

movement_image = pygame.image.load("movement.png")
movement_image = pygame.transform.scale(movement_image,(550,180))
combat_image = pygame.image.load("combat.png")
combat_image = pygame.transform.scale(combat_image,(550,180))
jump_boost_image = pygame.image.load("jumpboost.png")
jump_boost_image = pygame.transform.scale(jump_boost_image,(550,180))
good_luck_image = pygame.image.load("good_luck.png")
good_luck_image = pygame.transform.scale(good_luck_image,(550,180))

cursor_image = pygame.image.load("sword icon.png")
cursor_image = pygame.transform.scale(cursor_image,(100,200))

hp_bar = pygame.image.load("player_hp_bar.png")
hp_bar = pygame.transform.scale(hp_bar,(250,80))

platform_size_x = 230
platform_size_y = 10
high_platform = pygame.image.load("game_platform.png")
high_platform = pygame.transform.scale(high_platform,(platform_size_x,platform_size_y))

heart = pygame.image.load("hearts.png")
heart = pygame.transform.scale(heart,(37,30))

box_top = pygame.image.load("box1.png")
box_top = pygame.transform.scale(box_top,(50,40))
box_right = pygame.image.load("box_right.png")
box_right = pygame.transform.scale(box_right,(50,40))
box_left = pygame.image.load("box_left.png")
box_left = pygame.transform.scale(box_left,(50,40))
box_bot = pygame.image.load("box_bot.png")
box_bot = pygame.transform.scale(box_bot,(50,40))

enemy_hit_marker = pygame.image.load("25x25 player.png")
enemy_hit_marker = pygame.transform.scale(enemy_hit_marker,(50,20))
bat_sprite_right = pygame.image.load("bat sprite.png")
bat_sprite_right = pygame.transform.scale(bat_sprite_right,(125,60))
bat_sprite_left = pygame.image.load("bat sprite_left.png")
bat_sprite_left = pygame.transform.scale(bat_sprite_left,(125,60))
ogre_sprite_right = pygame.image.load("ogre_enemy_right.png")
ogre_sprite_right = pygame.transform.scale(ogre_sprite_right, (80,64))
ogre_sprite_left = pygame.image.load("ogre_enemy_left.png")
ogre_sprite_left = pygame.transform.scale(ogre_sprite_left, (80,64))
#Movement
player_posx = 350
player_posy = 270
moving_right = False
moving_left = False
facing_right = True
facing_left = False
vertical_momentum = 0

#Variables:
player_attack = False
title_down1 = True
title_up1 = False
title_down2 = False
title_up2 = True
title_pos1x = 110
title_pos1y = 2
title_pos2x = 110
title_pos2y = 45
up_or_down1 = 1
up_or_down2 = -1
title_vert_momentum1 = 0
title_vert_momentum2 = 0

instruct_movement = True
instruct_combat = False
instruct_jump_boost = False
instruct_good_luck = False
left_arrow = False
right_arrow = False

player_hp = 236
colour = Green
player_hp_bar_x = 10

box= "active"
box1 = "active"
box2 = "active"
box3 = "active"
box4 = "active"
box_count = 0
box_pos_1 = [330,40]
box_pos_2 = [330,40]
box_pos_3 = [330,40]
box_pos_4 = [330,40]
reset_box_count = 0
dissapear_box = False

heart_pos_x = 340
heart_pos_y = 50
heart_pos_x_momentum = 0
heart_pos_y_momentum = 0
gained_hp = False

enemy_pos_y = 300

original_bat_1_spawn = -250
bat_1_pos_x = original_bat_1_spawn
bat_1_facing_right = True
bat_1_facing_left = False
bat_1_moving_right = True
bat_1_moving_left = False
bat_speed = 0.6
bat_1_hp = 100
bat_1_spawn = True
bat_1_hit = False
bat_1_attack = False
bat_1_attack_count = 0
bat_1_hit_marker_count = 0

original_bat_2_spawn = 1200
bat_2_pos_x = original_bat_2_spawn
bat_2_facing_right = False
bat_2_facing_left = True
bat_2_moving_right = False
bat_2_moving_left = True
bat_2_hp = 100
bat_2_spawn = True
bat_2_hit = False
bat_2_attack = False
bat_2_attack_count = 0
bat_2_hit_marker_count = 0

original_bat_3_spawn = 950
bat_3_pos_x = original_bat_3_spawn
bat_3_facing_right = False
bat_3_facing_left = True
bat_3_moving_right = False
bat_3_moving_left = True
bat_3_hp = 100
bat_3_spawn = False
bat_3_hit = False
bat_3_attack = False
bat_3_attack_count = 0
bat_3_hit_marker_count = 0

original_ogre_1_spawn = -800
ogre_1_pos_x = original_ogre_1_spawn
ogre_1_facing_right = True
ogre_1_facing_left = False
ogre_1_moving_right = True
ogre_1_moving_left = False
ogre_speed = 0.3
ogre_1_hp = 250
ogre_1_spawn = True
ogre_1_hit = False
ogre_1_attack = False
ogre_1_attack_count = 0
ogre_1_hit_marker_count = 0

original_ogre_2_spawn = 1300
ogre_2_pos_x = original_ogre_2_spawn
ogre_2_facing_right = True
ogre_2_facing_left = False
ogre_2_moving_right = True
ogre_2_moving_left = False
ogre_2_hp = 250
ogre_2_spawn = False
ogre_2_hit = False
ogre_2_attack = False
ogre_2_attack_count = 0
ogre_2_hit_marker_count = 0

#Attacking:
left_attack1 = pygame.image.load("attack_left_first.png")
left_attack1 = pygame.transform.scale(left_attack1, (160,130))
left_attack2 = pygame.image.load("attack_left_second.png")
left_attack2 = pygame.transform.scale(left_attack2, (160,130))
left_attack3 = pygame.image.load("attack_left_1.png")
left_attack3 = pygame.transform.scale(left_attack3, (160,130))
left_attack4 = pygame.image.load("neutral_left.png")
left_attack4 = pygame.transform.scale(left_attack4, (160,130))
left_attacking = (left_attack1,left_attack1,left_attack1,left_attack1,left_attack2,left_attack2,left_attack2,left_attack2,left_attack3,left_attack3,left_attack3,left_attack3,left_attack4,left_attack4,left_attack4,left_attack4)
attack_index = 0
right_attack1 = pygame.image.load("attack_right_first.png")
right_attack1 = pygame.transform.scale(right_attack1, (160,130))
right_attack2 = pygame.image.load("attack_right_second.png")
right_attack2 = pygame.transform.scale(right_attack2, (160,130))
right_attack3 = pygame.image.load("attack_right_1.png")
right_attack3 = pygame.transform.scale(right_attack3, (160,130))
right_attack4 = pygame.image.load("neutral_right.png")
right_attack4 = pygame.transform.scale(right_attack4, (160,130))
right_attacking = (right_attack1,right_attack1,right_attack1,right_attack1,right_attack2,right_attack2,right_attack2,right_attack2,right_attack3,right_attack3,right_attack3,right_attack3,right_attack4,right_attack4,right_attack4,right_attack4)

#Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 28)
def show_score(x,y):
    score_text = font.render("Score: " + str(score),True,White)
    display.blit(score_text,(x,y))
def show_play_again(x,y):
    play_again_text = font.render("Press SPACE to play again",True,White)
    display.blit(play_again_text,(x,y))

#Game loop:
while True:
#EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_screen == True:
                player_attack = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if game_screen == True:
                    player_attack = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if game_screen == True:
                    player_attack = False

    mouse_pos = pygame.mouse.get_pos()
    display.blit(cursor_image, (mouse_pos[0], mouse_pos[1]))
#START SCREEN
    if start_screen == True:
        background_count += 1
        if background_count > 0:
            display.blit(background_1,(0,0))
        if background_count > 5:
            display.blit(background_2,(0,0))
        if background_count > 10:
            display.blit(background_3,(0,0))
        if background_count > 15:
            display.blit(background_4,(0,0))
        if background_count > 20:
            display.blit(background_5, (0, 0))
        if background_count > 25:
            display.blit(background, (0, 0))
#INSTRUCTIONS:
            instruction_count += 1
            if instruction_count > 1:
                instruct_movement = True
                instruct_combat = False
                instruct_jump_boost = False
                instruct_good_luck = False
            if instruction_count > 120:
                instruct_movement = False
                instruct_combat = True
                instruct_jump_boost = False
                instruct_good_luck = False
            if instruction_count > 240:
                instruct_movement = False
                instruct_combat = False
                instruct_jump_boost = True
                instruct_good_luck = False
            if instruction_count > 360:
                instruct_movement = False
                instruct_combat = False
                instruct_jump_boost = False
                instruct_good_luck = True
            if instruction_count > 480:
                instruction_count = 0
            if mouse_pos[0] > 140 and mouse_pos[0] < 175 and mouse_pos[1] > 300 and mouse_pos[1] < 345:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if instruction_count > 120:
                        left_arrow = True
            if left_arrow == True:
                instruction_count -= 60
                left_arrow = False
            if mouse_pos[0] > 600 and mouse_pos[0] < 635 and mouse_pos[1] > 300 and mouse_pos[1] < 345:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if instruction_count < 360:
                        right_arrow = True
            if right_arrow == True:
                instruction_count += 60
                right_arrow = False
            if instruct_movement == True:
                display.blit(movement_image,(115,150))
            if instruct_combat == True:
                display.blit(combat_image,(115,150))
            if instruct_jump_boost == True:
                display.blit(jump_boost_image,(115,150))
            if instruct_good_luck == True:
                display.blit(good_luck_image,(115,150))
#TITLE:
            display.blit(title1, (int(title_pos1x), int(title_pos1y)))
            display.blit(title2, (int(title_pos2x), int(title_pos2y)))
            if title_up1 == True:
                up_or_down1 = -1
                title_up_count1 += 1
            if title_down1 == True:
                up_or_down1 = 1
                title_down_count1 += 1
            if title_down_count1 > 30:
                title_vert_momentum1 = 0
                title_down1 = False
                title_up1 = True
                title_down_count1 = 0
            if title_up_count1 > 30:
                title_vert_momentum1 = 0
                title_down1 = True
                title_up1 = False
                title_up_count1 = 0
            title_vert_momentum1 += up_or_down1 * 0.08
            title_pos1y += title_vert_momentum1

            if title_up2 == True:
                up_or_down2 = -1
                title_up_count2 += 1
            if title_down2 == True:
                up_or_down2 = 1
                title_down_count2 += 1
            if title_down_count2 > 30:
                title_vert_momentum2 = 0
                title_down2 = False
                title_up2 = True
                title_down_count2 = 0
            if title_up_count2 > 30:
                title_vert_momentum2 = 0
                title_down2 = True
                title_up2 = False
                title_up_count2 = 0
            title_vert_momentum2 += up_or_down2 * 0.1
            title_pos2y += title_vert_momentum2
        if background_count > 40:
            if mouse_pos[0] > 330 and mouse_pos[0] < 470 and mouse_pos[1] > 395 and mouse_pos[1] < 460:
                hover = True
                display.blit(play_button,(310,300 + 20))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                if event.type == pygame.MOUSEBUTTONUP:
                    click = False
            else:
                display.blit(play_button_small, (330,312 +20))
        if click == True:
            click_sound.play()
            game_screen = True
            click = False
            start_screen = False

#GAME SCREEN
    if game_screen == True:
        display.blit(background2, (0, 0))
        display.blit(background2, (400, 0))
        display.blit(platform, (80, 235))
        display.blit(platform,(554,235))
        display.blit(high_platform,(250,90))
        show_score(30,80)
        if player_posx > 250 -130 and player_posx < 220 + platform_size_x:
            if player_posy < 2:
                player_posy = -2
        if player_hp > 118:
            colour = Green
        elif player_hp > 59:
            colour = hp_yellow
        else:
            colour = hp_red
        pygame.draw.rect(display, colour, ((player_hp_bar_x + 70),30,(18 + int(player_hp/2)),30))
        display.blit(hp_bar,(player_hp_bar_x,10))
# ENEMIES:
        if bat_1_spawn == True:
            if bat_1_hp > 0:
                if bat_1_facing_right == True:
                    display.blit(bat_sprite_right, (int(bat_1_pos_x), int(enemy_pos_y)))
                if bat_1_facing_left == True:
                    display.blit(bat_sprite_left,(int(bat_1_pos_x),int(enemy_pos_y)))
            if bat_1_hp < 1:
                score += 100
                bat_1_hp = 100
                bat_1_hit_marker_count = 0
                bat_1_pos_x = original_bat_1_spawn
        if bat_2_spawn == True:
            if bat_2_hp > 0:
                if bat_2_facing_right == True:
                    display.blit(bat_sprite_right, (int(bat_2_pos_x), int(enemy_pos_y)))
                if bat_2_facing_left == True:
                    display.blit(bat_sprite_left, (int(bat_2_pos_x), int(enemy_pos_y)))
            if bat_2_hp < 1:
                score += 100
                bat_2_hp = 100
                bat_2_hit_marker_count = 0
                bat_2_pos_x = original_bat_2_spawn
        if bat_3_spawn == True:
            if bat_3_hp > 0:
                if bat_3_facing_right == True:
                    display.blit(bat_sprite_right, (int(bat_3_pos_x), int(enemy_pos_y)))
                if bat_3_facing_left == True:
                    display.blit(bat_sprite_left, (int(bat_3_pos_x), int(enemy_pos_y)))
            if bat_3_hp < 1:
                score += 100
                bat_3_hp = 100
                bat_3_hit_marker_count = 0
                bat_3_pos_x = original_bat_3_spawn
        if ogre_1_spawn == True:
            if ogre_1_hp > 0:
                if ogre_1_facing_right == True:
                    display.blit(ogre_sprite_right, (int(ogre_1_pos_x), int(enemy_pos_y)))
                if ogre_1_facing_left == True:
                    display.blit(ogre_sprite_left,(int(ogre_1_pos_x),int(enemy_pos_y)))
            if ogre_1_hp < 1:
                score += 200
                ogre_1_hp = 250
                ogre_1_hit_marker_count = 0
                ogre_1_pos_x = original_ogre_1_spawn
        if ogre_2_spawn == True:
            if ogre_2_hp > 0:
                if ogre_2_facing_right == True:
                    display.blit(ogre_sprite_right, (int(ogre_2_pos_x), int(enemy_pos_y)))
                if ogre_2_facing_left == True:
                    display.blit(ogre_sprite_left,(int(ogre_2_pos_x),int(enemy_pos_y)))
            if ogre_2_hp < 1:
                score += 200
                ogre_2_hp = 250
                ogre_2_hit_marker_count = 0
                ogre_2_pos_x = original_ogre_2_spawn
#ENEMY MOVEMENT:
        if bat_1_spawn == True:
            if bat_1_hp > 0:
                if bat_1_pos_x < player_posx - 90:
                    bat_1_facing_right = True
                    bat_1_facing_left = False
                    bat_1_pos_x += bat_speed
                if bat_1_pos_x > player_posx + 120:
                    bat_1_facing_right = False
                    bat_1_facing_left = True
                    bat_1_pos_x -= bat_speed
        if bat_2_spawn == True:
            if bat_2_hp > 0:
                if bat_2_pos_x < player_posx - 90:
                    bat_2_facing_right = True
                    bat_2_facing_left = False
                    bat_2_pos_x += bat_speed
                if bat_2_pos_x > player_posx + 120:
                    bat_2_facing_right = False
                    bat_2_facing_left = True
                    bat_2_pos_x -= bat_speed
        if bat_3_spawn == True:
            if bat_3_hp > 0:
                if bat_3_pos_x < player_posx - 90:
                    bat_3_facing_right = True
                    bat_3_facing_left = False
                    bat_3_pos_x += bat_speed
                if bat_3_pos_x > player_posx + 120:
                    bat_3_facing_right = False
                    bat_3_facing_left = True
                    bat_3_pos_x -= bat_speed
        if ogre_1_spawn == True:
            if ogre_1_hp > 0:
                if ogre_1_pos_x < player_posx - 40:
                    ogre_1_facing_right = True
                    ogre_1_facing_left = False
                    ogre_1_pos_x += ogre_speed
                if ogre_1_pos_x > player_posx + 110:
                    ogre_1_facing_right = False
                    ogre_1_facing_left = True
                    ogre_1_pos_x -= ogre_speed
        if ogre_2_spawn == True:
            if ogre_2_hp > 0:
                if ogre_2_pos_x < player_posx - 40:
                    ogre_2_facing_right = True
                    ogre_2_facing_left = False
                    ogre_2_pos_x += ogre_speed
                if ogre_2_pos_x > player_posx + 110:
                    ogre_2_facing_right = False
                    ogre_2_facing_left = True
                    ogre_2_pos_x -= ogre_speed
#BAT ATTACK:
        if player_hp > 0:
            if bat_1_pos_x > player_posx - 92 and bat_1_pos_x < player_posx + 122:
                if player_posy >250:
                    bat_1_attack = True
            if bat_1_attack == True:
                bat_1_attack_count += 1
            if bat_1_attack_count == 20:
                player_hp -= 30
            if bat_1_attack_count == 30:
                bat_1_attack_count = 0
                bat_1_attack = False
            if bat_2_pos_x > player_posx - 92 and bat_2_pos_x < player_posx + 122:
                if player_posy >250:
                    bat_2_attack = True
            if bat_2_attack == True:
                bat_2_attack_count += 1
            if bat_2_attack_count == 20:
                player_hp -= 30
            if bat_2_attack_count == 30:
                bat_2_attack_count = 0
                bat_2_attack = False
            if bat_3_pos_x > player_posx - 92 and bat_3_pos_x < player_posx + 122:
                if player_posy >250:
                    bat_3_attack = True
            if bat_3_attack == True:
                bat_3_attack_count += 1
            if bat_3_attack_count == 20:
                player_hp -= 30
            if bat_3_attack_count == 30:
                bat_3_attack_count = 0
                bat_3_attack = False
            if ogre_1_pos_x > player_posx - 41 and ogre_1_pos_x < player_posx + 111:
                if player_posy >250:
                    ogre_1_attack = True
            if ogre_1_attack == True:
                ogre_1_attack_count += 1
            if ogre_1_attack_count == 20:
                player_hp -= 30
            if ogre_1_attack_count == 30:
                ogre_1_attack_count = 0
                ogre_1_attack = False
            if ogre_2_pos_x > player_posx - 41 and ogre_2_pos_x < player_posx + 111:
                if player_posy >250:
                    ogre_2_attack = True
            if ogre_2_attack == True:
                ogre_2_attack_count += 1
            if ogre_2_attack_count == 20:
                player_hp -= 30
            if ogre_2_attack_count == 30:
                ogre_2_attack_count = 0
                ogre_2_attack = False

#BOXES:
        if dissapear_box != True:
            display.blit(heart, (heart_pos_x,heart_pos_y))
        else:
            if gained_hp == False:
                if heart_pos_x > player_hp_bar_x + 90:
                    heart_pos_x_momentum += 0.3
                    heart_pos_x -= heart_pos_x_momentum
                if heart_pos_y > 40:
                    heart_pos_y_momentum += 0.3
                    heart_pos_y -= heart_pos_y_momentum
                if int(heart_pos_x) != 93:
                    display.blit(heart, (int(heart_pos_x), int(heart_pos_y)))
                if int(heart_pos_y) != 39:
                    display.blit(heart, (int(heart_pos_x),int(heart_pos_y)))
                if int(heart_pos_x) == 93 and int(heart_pos_y) == 39:
                    if player_hp < 236 - 50:
                        player_hp += 50
                    if player_hp >= 236 - 50:
                        player_hp += 236 - player_hp
                    gained_hp = True
            if gained_hp == True:
                heart_pos_x = 340
                heart_pos_y = 50
                heart_pos_x_momentum = 0
                heart_pos_y_momentum = 0
                reset_box_count += 1
                if reset_box_count == 150:
                    box4 = "active"
                if reset_box_count == 300:
                    box3 = "active"
                if reset_box_count == 450:
                    box2 = "active"
                if reset_box_count == 600:
                    box = "active"
                    box1 = "active"
                    box_count = 0
                    reset_box_count = 0
                    gained_hp = False
                    dissapear_box = False
        if box1 == "active":
            display.blit(box_top,(340, 40))
        if box2 == "active":
            display.blit(box_right,(340,40))
        if box3 == "active":
            display.blit(box_left,(340,40))
        if box4 == "active":
            display.blit(box_bot,(340,40))
#Collisions:
        if player_posx > -40 and player_posx < 80 and player_posy < 250 and player_posy > 200:
            if vertical_momentum < 0:
                player_posy = 135
        if player_posx > 427 and player_posx < 564 and player_posy < 250 and player_posy > 200:
            if vertical_momentum < 0:
                player_posy = 135
#FACING LEFT OR RIGHT:
        if facing_right == True:
            if player_attack == False:
                display.blit(player_right, (int(player_posx),int(player_posy)))
        if facing_left == True:
            if player_attack == False:
                display.blit(player_left, (int(player_posx),int(player_posy)))
        if box4 == "broken":
            if dissapear_box == False:
                box_count += 1
                reset_box_count += 1
            if box_count == 60:
                dissapear_box = True

#PLAYER ATTACK:
        if player_attack == True:
            if facing_left == True:
                display.blit(left_attacking[attack_index],(int(player_posx),int(player_posy)))
                if attack_index == 10:
                    player_hit_pos_x = int(player_posx) + 10
                    player_hit_pos_y = int(player_posy)
#HITTING BATS:
                    if bat_1_hp > 0:
                        if player_hit_pos_x > bat_1_pos_x and player_hit_pos_x < bat_1_pos_x + 125:
                            if player_hit_pos_y > 240 and player_hit_pos_y < 280:
                                if bat_1_hit == False:
                                    bat_1_hit = True
                    if bat_2_hp > 0:
                        if player_hit_pos_x > bat_2_pos_x and player_hit_pos_x < bat_2_pos_x + 125:
                            if player_hit_pos_y > 240 and player_hit_pos_y < 280:
                                if bat_2_hit == False:
                                    bat_2_hit = True
                    if bat_3_hp > 0:
                        if player_hit_pos_x > bat_3_pos_x and player_hit_pos_x < bat_3_pos_x + 125:
                            if player_hit_pos_y > 240 and player_hit_pos_y < 280:
                                if bat_3_hit == False:
                                    bat_3_hit = True
#HITTING OGRES
                    if ogre_1_hp > 0:
                        if player_hit_pos_x > ogre_1_pos_x and player_hit_pos_x < ogre_1_pos_x + 80:
                            if player_hit_pos_y > 240 and player_hit_pos_y < 280:
                                if ogre_1_hit == False:
                                    ogre_1_hit = True
                    if ogre_2_hp > 0:
                        if player_hit_pos_x > ogre_2_pos_x and player_hit_pos_x < ogre_2_pos_x + 80:
                            if player_hit_pos_y > 240 and player_hit_pos_y < 280:
                                if ogre_2_hit == False:
                                    ogre_2_hit = True

#HITTING BOX:
                    if player_hit_pos_x > 340 and player_hit_pos_x < 340 + 50:
                        if player_hit_pos_y == -2:
                            if box == "active":
                                if box1 == "broken":
                                    if box2 == "broken":
                                        if box3 == "broken":
                                            if box4 == "broken":
                                                box = "broken"
                                            else:
                                                box4 = "broken"
                                                box = "broken"
                                        else:
                                            box3 = "broken"
                                    else:
                                        box2 = "broken"
                                else:
                                    box1 = "broken"
            if facing_right == True:
                display.blit(right_attacking[attack_index], (int(player_posx), int(player_posy)))
                if attack_index == 10:
                    player_hit_pos_x = int(player_posx) + 150
                    player_hit_pos_y = int(player_posy)

#HITTING BATS:
                    if bat_1_hp > 0:
                        if player_hit_pos_x > bat_1_pos_x and player_hit_pos_x < bat_1_pos_x + 125:
                            if player_hit_pos_y > 240 and player_hit_pos_y < 280:
                                if bat_1_hit == False:
                                    bat_1_hit = True
                    if bat_2_hp > 0:
                        if player_hit_pos_x > bat_2_pos_x and player_hit_pos_x < bat_2_pos_x + 125:
                            if player_hit_pos_y > 240 and player_hit_pos_y < 280:
                                if bat_2_hit == False:
                                    bat_2_hit = True
                    if bat_3_hp > 0:
                        if player_hit_pos_x > bat_3_pos_x and player_hit_pos_x < bat_3_pos_x + 125:
                            if player_hit_pos_y > 240 and player_hit_pos_y < 280:
                                if bat_3_hit == False:
                                    bat_3_hit = True
#HITTING OGRES
                    if ogre_1_hp > 0:
                        if player_hit_pos_x > ogre_1_pos_x and player_hit_pos_x < ogre_1_pos_x + 80:
                            if player_hit_pos_y > 240 and player_hit_pos_y < 280:
                                if ogre_1_hit == False:
                                    ogre_1_hit = True
                    if ogre_2_hp > 0:
                        if player_hit_pos_x > ogre_2_pos_x and player_hit_pos_x < ogre_2_pos_x + 80:
                            if player_hit_pos_y > 240 and player_hit_pos_y < 280:
                                if ogre_2_hit == False:
                                    ogre_2_hit = True

#HITTING BOX:
                    if player_hit_pos_x > 340 and player_hit_pos_x < 340 + 50:
                        if player_hit_pos_y == -2:
                            if box == "active":
                                if box1 == "broken":
                                    if box2 == "broken":
                                        if box3 == "broken":
                                            if box4 == "broken":
                                                box = "broken"
                                            else:
                                                box4 = "broken"
                                                box = "broken"
                                        else:
                                            box3 = "broken"
                                    else:
                                        box2 = "broken"
                                else:
                                    box1 = "broken"
            if attack_index < 15:
                attack_index += 1
            else:
                attack_index = 0
                player_attack = False
            if attack_index == 1:
                sword_sound.play()

# IF ENEMIES ARE HIT:
        if bat_1_hit == True:
            bat_1_hit_marker_count += 1
            if bat_1_hit_marker_count == 1:
                bat_1_hp -= 50
            bat_1_hit_marker_count = 0
            bat_1_hit = False
        if bat_2_hit == True:
            bat_2_hit_marker_count += 1
            if bat_2_hit_marker_count == 1:
                bat_2_hp -= 50
            bat_2_hit_marker_count = 0
            bat_2_hit = False
        if bat_3_hit == True:
            bat_3_hit_marker_count += 1
            if bat_3_hit_marker_count == 1:
                bat_3_hp -= 50
            bat_3_hit_marker_count = 0
            bat_3_hit = False
        if ogre_1_hit == True:
            ogre_1_hit_marker_count += 1
            if ogre_1_hit_marker_count == 1:
                ogre_1_hp -= 50
            ogre_1_hit_marker_count = 0
            ogre_1_hit = False
        if ogre_2_hit == True:
            ogre_2_hit_marker_count += 1
            if ogre_2_hit_marker_count == 1:
                ogre_2_hp -= 50
            ogre_2_hit_marker_count = 0
            ogre_2_hit = False
#PLAYER MOVEMENT:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moving_left = False
                facing_left = False
                facing_right = True
                moving_right = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moving_right = False
                facing_right = False
                facing_left = True
                moving_left = True
            if event.key == pygame.K_w or event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if air_timer < 6:
                    vertical_momentum = -5
                    jump_sound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moving_left = False
        if moving_right == True:
            if player_posx < 650:
                player_posx += 2
        if moving_left == True:
            if player_posx > -10:
                player_posx -= 2
        vertical_momentum += 0.08
        if vertical_momentum > 3:
            vertical_momentum = 3
        if player_posy > 270:
            player_posy = 270
        if player_posy == 270:
            air_timer = 0
        else:
            air_timer += 1
        player_posy += vertical_momentum

#IF THE PLAYER LOSES
        if player_hp < 1:
            restart_game_count += 1
            if restart_game_count == 60:
                restart_game_count = 0
                game_screen = False
                bat_1_pos_x = original_bat_1_spawn
                bat_2_pos_x = original_bat_2_spawn
                bat_3_pos_x = original_bat_3_spawn
                ogre_1_pos_x = original_ogre_1_spawn
                ogre_2_pos_x = original_ogre_2_spawn
                player_hp = 236
                play_again_screen = True
        if score > 300:
            bat_3_spawn = True
        if score> 800:
            ogre_2_spawn = True

#PLAY AGAIN SCREEN
    if play_again_screen == True:
        display.blit(background2, (0, 0))
        display.blit(background2, (400, 0))
        show_score(335,300)


    screen.blit(pygame.transform.scale(display, Window_size), (0, 0))
    pygame.display.update()
    mainClock.tick(60)
#HIGHSCORE: 8700 set by CLUTCH MASTER ARCAZARD