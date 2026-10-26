import pygame
import os
import time
import sys

#make it work
pygame.init()

window_width = 1400
window_height = 800
screen=pygame.display.set_mode([window_width, window_height])

runing = True
clock = pygame.time.Clock()

def play_sound(filename):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    sound_path = os.path.join(BASE_DIR, filename)
    try:
        sound = pygame.mixer.Sound(sound_path)
        sound.play()
    except pygame.error as e:
        print(f"error playing '{sound_path}': {e}")

def immage_render(immage_name, size_percentege, transparicy=False):
    # lerns the way to this folder and sets it up so that future vars can set themselves as the sprite
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    immage_path = os.path.join(BASE_DIR, immage_name)
    
    # loades base immage
    final_immage = pygame.image.load(immage_path)
    
    # applys transparency if needed
    if transparicy:
        final_immage = final_immage.convert_alpha()
    else:
        final_immage = final_immage.convert() 
        
    final_immage = pygame.transform.scale(final_immage, (int(final_immage.get_width() * size_percentege / 100), int(final_immage.get_height() * size_percentege / 100)))
    return final_immage
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

font_path = os.path.join(BASE_DIR, "Minecraft.ttf")

text_font = pygame.font.Font(font_path, 24)

def desplay_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def green_calc(op_hp, op_hp_total):
    #make it start with 128 and slowly get better
    convercion = op_hp_total/255
    convercion = op_hp/convercion
    if (convercion == 0 )or convercion <0:
        convercion = 0
    return convercion

    




def red_calc(op_hp, op_hp_total):

    convercion = op_hp_total*305
    resault = (op_hp_total - op_hp)*convercion


    if resault > 255:
        resault = 255
    return resault

def reder_oponent(op_size, op_x, op_center, op_y, op_hb_x, op_hb_y, text_font):
    screen.blit(immage_render("oponent_ml_.png", op_size, True), (op_x - op_center, op_y - op_center))

    screen.blit(immage_render("health_bar.png", op_hb_size, True), (op_hb_x, op_hb_y))
    
    desplay_text("Ml322_", text_font, (0, 0, 0), op_hb_x + 72, op_hb_y + 160)

    #op health
    pygame.draw.rect(screen, (red_calc(op_hp, op_hp_total), green_calc(op_hp, op_hp_total), 0), ((op_hb_x + 67) + op_hp_total*2.76 - op_hp*2.76, op_hb_y + 190, op_hp*2.76, 20))

def reder_player(text_font, op_size, op_hb_size):
    screen.blit(immage_render("player.png", op_size*2, True), (138, 10))
    screen.blit(immage_render("health_bar.png", op_hb_size, True), (20, 188))
    desplay_text("you", text_font, (0, 0, 0), 20 + 72, 188 + 160)
    #health
    
    pygame.draw.rect(screen, (red_calc(hp, hp_total), green_calc(hp, hp_total), 0), ((20 + 67) + hp_total*2.76 - hp*2.76, 188 + 190, hp*2.76, 20))

#set the oponents's vars
op_spirte_size = 200
op_size = 250
op_center = op_spirte_size*(op_size/100)/2

op_x = window_width/1.4
op_y = window_height/3.2

op_hb_size = op_size - op_size/5
op_hb_x = op_x - op_spirte_size*2.5
op_hb_y = -75
op_hp_total = 100
op_hp = op_hp_total

hb_size = op_hb_size
hb_x = 138
hb_y = 10
hp_total = 100
hp = hp_total



# an example of a draw an image
#screen.blit(immage_render(name, size), position x, position y))
placed = False

while runing:
    clock.tick(60)
    # Look for events (mouse clicks, key presses)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

    mouse_x, mouse_y = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()
    #if enter (return) is prest tell the curent position of the mouse witch is curently the placeholder guy
    if key[pygame.K_RETURN]:
        op_hp -= 1
        print(mouse_x, mouse_y)
    # chaing the backround color to any RGB value
    #olso a way to clear the screen
    screen.fill((0, 128, 0))

    #draw player
    reder_player(text_font, op_size, op_hb_size)
    #draw oponent
    reder_oponent(op_size, op_x, op_center, op_y, op_hb_x, op_hb_y, text_font)
    #just a test
    pygame.draw.rect(screen, (255, 0, 0), (848, 520, 1084-848, 639-520))

    
    if ((848 <= mouse_x <= 1084) and (520 <= mouse_y <= 639)) and pygame.mouse.get_just_pressed()[0]:
        op_hp -= 10
        hp -= 10
        


    screen.blit(immage_render("attack_button.png", 150, True), (848, 520))
 
    
    

    # Update the actual display
    pygame.display.flip()



pygame.quit()
sys.exit()
#no ai
