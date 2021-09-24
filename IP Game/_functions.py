#importing packages/libraries
import random as rr
import pygame

#player needs to give input/instruction to the program on who to attack based on index and ai randomly selects an index to attack
def playerChoice(list1, list2, isAi):

    lenOflist1 = len(list1) 
    lenOflist2 = len(list2)
    choosePlayer = -1
    chooseTarget = -1

    
    if isAi == 0:
        if lenOflist1 > 1:
            while choosePlayer not in range(lenOflist1):
                try:
                    choosePlayer = int(input('Select team character to attack with. Use index number from (1 - {})  '.format(lenOflist1)))
                    choosePlayer -= 1
                    if choosePlayer not in range(lenOflist1):
                        print('\n<Please enter correct number>')

                except:
                    print('\n<ValueError, Please enter number within specified range>')
                    continue
        elif lenOflist1 == 1:
            print('\nYou have one character left! (Character will be automatically selected)')
            choosePlayer = 0
            input('Press ENTER to continue...')

        if lenOflist2 > 1: 
            while chooseTarget not in range(lenOflist2):
                try:
                    chooseTarget = int(input('Select target to attack. Use index number from (1 - {}) '.format(lenOflist2)))
                    chooseTarget -= 1
                    if chooseTarget not in range(lenOflist2):
                            print('\n<Please enter correct number>')
                        
                except:
                    print('\n<ValueError, Please enter number within specified range>')
                    continue
        elif lenOflist1 == 1:
            print('\nYou have one target left! (Target will be automatically selected)')
            chooseTarget = 0
            input('Press ENTER to continue...')


    elif isAi == 1:
        choosePlayer = rr.randrange(0, lenOflist1)
        chooseTarget = rr.randrange(0, lenOflist2)


    list1[choosePlayer].player_attack(list2[chooseTarget])

# if any characters in the list is dead, remove character from the list of characters
def alive(character_list, aicharacter_list):
    for i in character_list:
        if i.checkAlive() == False:
            character_list.remove(i)
        
            
    for i in aicharacter_list:
        if i.checkAlive() == False:
            aicharacter_list.remove(i)

# if an opponent loses all his characters, display victory message   
def whoWins(character_list, aicharacter_list):
    if (len(character_list) == 0):
        print('--- AI HAS WON!! ---')
        print('Thank you for playing!')
        return False
    
    elif (len(aicharacter_list) == 0):
        print('--- WE HAVE WON!! ---')
        print('Congratulations!')
        return False
    
    else:
        return True

# print out full list of charcaters and stats     
def newList(character_list, aicharacter_list):
    index = 1
    print('\nList of Characters')
    
    print('============ Player ============')
    if(len(character_list)>0):
        for obj in character_list:
            print(f'{index}) ' + obj.getStatsStr())
            index += 1
            
    print()
    index = 1
    print('============= Ai =============')        
    if(len(aicharacter_list)>0):
        for obj in aicharacter_list:

            print(f'{index}) ' + obj.getStatsStr())
            index += 1
            


#=======================================================================================================================================v
# create function for drawing texts
def draw_text(text, font, text_color, x, y, screen):
    img = font.render(text, True, text_color)
    screen.blit(img, (x,y))


# function for drawing background
def draw_bg(screen, background_img):
    screen.blit(background_img, (0,0))

# function for drawing the health bar
def draw_healthbar(x, y, hp, max_hp, screen, red, green):
    ratio = hp / max_hp
    pygame.draw.rect(screen, red,(x, y , 150, 20))
    pygame.draw.rect(screen, green,(x, y , 150 * ratio, 20))

# function for drawing panel
def draw_panel(character_list, enemy_list,screen,panel_img,screen_height,bottom_panel, font, lightbrown, red, green):
    

    # draw panel rectangle
    screen.blit(panel_img, (0, screen_height - bottom_panel))
    
    # to draw the name and stats of each player in the bottom panel
    for x, player in enumerate(character_list):
        draw_text(f'{player.get_name()}', font, lightbrown, 50, screen_height - bottom_panel + 20 + x*60, screen)
        draw_text(f'HP: {player.getCurrentHP()}/100    lvl: {player.getLvl()}', font, lightbrown, 150, screen_height - bottom_panel + 15 + x*60, screen)
        draw_healthbar(150, screen_height - bottom_panel + 40 + x*60, player.getCurrentHP(), 100, screen, red, green)
        player.draw(screen)

    # to draw the name and stats of each enemy in the bottom panel
    for x, enemy in enumerate(enemy_list):
        draw_text(f'{enemy.get_name()}', font, lightbrown, 670, screen_height - bottom_panel + 20 + x*60, screen)
        draw_text(f'HP: {enemy.getCurrentHP()}/100    lvl: {enemy.getLvl()}', font, lightbrown, 730, screen_height - bottom_panel + 15 + x*60, screen)
        draw_healthbar(730, screen_height - bottom_panel + 40 + x*60, enemy.getCurrentHP(), 100, screen, red, green)
        enemy.draw(screen)


    
 
            