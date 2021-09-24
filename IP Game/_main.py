#importing packages/libraries/files
from _character import *
from _functions import *

#=======================================================================================================================================v
from math import exp
import pygame
import time
import random as rr
from tkinter import *


pygame.init()

clock = pygame.time.Clock()
fps = 60

# game window size
bottom_panel = 200
screen_width = 1000
screen_height = 600 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle Game')
icon = pygame.image.load('img/background/swordicon.png')
pygame.display.set_icon(icon)


# define fonts
font = pygame.font.SysFont('Joystix Monospace', 25)

# define colors
red = (255, 0, 0)
green = (0, 255, 0)
brown = pygame.Color('#4C0F0F')
darkbrown = pygame.Color('#7F2E0C')
lightbrown = pygame.Color('#B27F6A')

# load images
background_img = pygame.image.load('img/background/forest1.png').convert_alpha()
panel_img = pygame.image.load('img/background/panel.png').convert_alpha()
victory_img = pygame.image.load('img/background/victory.png').convert_alpha()
defeat_img = pygame.image.load('img/background/defeat.png').convert_alpha()


# for game over
game_over = 0

#=======================================================================================================================================^

character_list = []
aicharacter_list = []
profession_list = ['w','W','T','t']
counter = 0


def main():
    global character_list
    global aicharacter_list
    global profession_list
    global counter
    
    

    for x in range(3):
        profession = input('\nChoose profession W-warrior T-tanker: ')
        while profession not in profession_list:
            print("Please enter a proper profession")
            profession = input('Choose profession W-warrior T-tanker: ')

        name = input('Enter character name: ')
        character_list.append(Fighter(profession, name, 0, 200, 200 + x * 140)) 

        profession = rr.choice(['W', 'T'])
        name = 'AI'+str(rr.randint(10,99))+rr.choice(['A', 'B', 'C', 'D', 'E'])
        aicharacter_list.append(Fighter(profession, name, 1, 800, 200 + x * 140))

    print()    
    for obj in character_list:
        print(obj.__str__())

    print()   
    for obj in aicharacter_list:
        print(obj.__str__())
        
#=======================================================================================================================================v
    draw_bg(screen, background_img)

    # draw panel
    draw_panel(character_list, aicharacter_list, screen,panel_img,screen_height,bottom_panel, font, lightbrown, red, green)

    pygame.event.get()
    pygame.display.update()
#=======================================================================================================================================^
    
   
    while whoWins(character_list, aicharacter_list):
        
        
        newList(character_list, aicharacter_list)
        
        print (f'\n========== Round {counter + 1} ==========')
        
        if(counter%2 == 0):
            playerChoice(character_list, aicharacter_list, counter%2)
        else:
            playerChoice(aicharacter_list, character_list, counter%2)

        input('\nPress ENTER to continue...')
        
        counter+=1
        pygame.event.pump()
        alive(character_list, aicharacter_list)

#=======================================================================================================================================v       
        draw_bg(screen, background_img)
        draw_panel(character_list, aicharacter_list, screen,panel_img,screen_height,bottom_panel, font, lightbrown, red, green)

        pygame.display.update()
        
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        
    
    # game is over
    if len(aicharacter_list) == 0:
        screen.blit(victory_img, (360, 268))
        # enemy wins
    elif len(character_list) == 0:
        screen.blit(defeat_img, (380, 268))

    pygame.event.pump()
    pygame.display.update()

    input('\nPress ENTER to continue...')

    pygame.quit()
#=======================================================================================================================================^   
        
        
        
if __name__ == '__main__':
    main()
