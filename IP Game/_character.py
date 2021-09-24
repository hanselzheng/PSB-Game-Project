#importing packages/libraries
import random as rr
import pygame
from datetime import datetime

#class to create characters
class Character:
    __profession = ''
    __name = ''
    __hp = 0
    __exp = 0
    __lvl = 0
    __atk = 0
    __defence = 0
    __alive = True
    
    
    def __init__(self, profession, name):
        self.__profession = profession
        self.__name = name
        self.game_setup(profession)

     #set initial value of stats
    def game_setup(self, profession):
        self.__hp = 100
        self.__exp = 0
        self.__lvl = 1
        self.__alive = True
        
        if(profession == 'W' or profession == 'w'):
            self.__profession = 'Warrior'
            self.__atk = rr.randint(5, 20)
            self.__defence = rr.randint(1, 10)
        elif(profession == 'T' or profession == 't'):
            self.__profession = 'Tanker'
            self.__atk = rr.randint(1, 10)
            self.__defence = rr.randint(5, 15)
        
        
    #method for class object to attack similar class object
    def player_attack(self, target):
        crit = 10+self.__atk
        if(self.__atk != 0 and self.__hp != 0):
            dmg_point = self.__atk - target.getDefence() + rr.randint(-5, 20)
            if dmg_point > 0:
                target.minusCurrentHP(dmg_point)
                print('\n{} has dealt {} with {} dmg'.format(self.__name, target.get_name(), dmg_point))
                print('{} gain {} exp'.format(self.__name, dmg_point))
                print('{} gain {} exp'.format(target.get_name(), target.getDefence()))

                if(dmg_point >= crit):
                    print('It was a critical hit!')
            elif(dmg_point <= 0):
                print('\nOH NO! {} did not deal enough damage to {}!!!! ({} dmg)'.format(self.__name, target.get_name(), dmg_point))

            self.expDistribution(target, dmg_point)

            target.checkExpCap()
            self.checkExpCap()
            

     #distributes exp to attacker and target objects based on damage dealt and damage mitigated
    def expDistribution(self, target, dmg_point):
        df = target.getDefence()
        twentypercent_extra_exp = int(20 / 100) * df
        fiftypercent_extra_exp = int(50 / 100) * df

        if dmg_point > 0:
            self.__exp += dmg_point
            target.setExp(target.getExp() + df ) 

            if dmg_point > 10:
                target.setExp(target.getExp() + twentypercent_extra_exp) 

        elif dmg_point  <= 0:
            target.setExp(target.getExp() + df + fiftypercent_extra_exp)

    # print class objects' name and profession
    def __str__(self):
        text = 'Player name: {}'.format(self.__name)
        text += ' Profession: {}'.format(self.__profession)
        return text 

    # print class objects' stats
    def showStats(self):
        print('Name: {}   Hp: {}   Atk: {}   Def: {}   Exp: {}   Lvl: {}   Profession: {}'.format(self.__name,
            self.__hp, self.__atk, self.__defence, self.__exp, self.__lvl, self.__profession))

    # deduct from class objects cureent hp based on damage taken and kill class object if no hp
    def minusCurrentHP(self, dmgtaken):
        if(self.__hp > 0):
            self.__hp-=dmgtaken

        if(self.__hp <= 0 and self.__alive):
            self.killCharacter()
            print(f'\n{self.__name} has died')

    #recursive methods to check exp limit
    def checkExpCap(self):
        if self.__lvl < 10:
            if self.__exp>= 100:
                self.__exp -= 100
                self.__lvl += 1

            while self.__exp>= 100:
                self.checkExpCap()

#----------------------------------------------------------------------------------------------------------------------------------
    #Accessor methods
#----------------------------------------------------------------------------------------------------------------------------------
   
    #get string for all stats 
    def getStatsStr(self):
        stats = 'Name: {}   Hp: {}   Atk: {}   Def: {}   Exp: {}   Lvl: {}   Profession: {}'.format(self.__name,
            self.__hp, self.__atk, self.__defence, self.__exp, self.__lvl, self.__profession)

        # log event
        f = open('log.txt', 'a')
        now = datetime.now()
        c_date = str(now.date())
        c_time = str(now.strftime("%H:%M:%S"))
        f.write(c_date + ' ' + c_time + '\n           ' + stats + '\n')
        f.close()

        return stats
        
    #get class objects' name   
    def get_name(self):
        return self.__name

    #get class objects' attack   
    def getAttack(self):
        return self.__atk

    #get class objects' defence
    def getDefence(self):
        return self.__defence

    #get class objects' current hp
    def getCurrentHP(self):
        return self.__hp

    #get class objects' exp
    def getExp(self):
        return self.__exp

    #get class objects' lvl
    def getLvl(self):
        return self.__lvl

    #get class objects' alive status
    def checkAlive(self):
        return self.__alive


#----------------------------------------------------------------------------------------------------------------------------------
    #Mutator methods
#----------------------------------------------------------------------------------------------------------------------------------  
    #set class objects' name
    def set_name(self, new_name):
        self.__name = new_name

    #set class objects' attack
    def setAttack(self, newAtk):
        if(newAtk > 0):
            self.__atk = newAtk

    #set class objects' defence
    def setDefence(self, newDef):
        if(newDef > 0):
            self.__defence = newDef

    #set class objects' current hp
    def setCurrentHP(self, newHp):
        self.__hp = newHp

    #set class objects' exp
    def setExp(self, newExp):
        self.__exp = newExp

    #set class objects' lvl
    def setLvl(self, newLvl):
        self.__lvl = newLvl
    
    # kill alive object
    def killCharacter(self):
        self.__alive = False

     # revive dead object   
    def reviveCharacter(self):
        self.__alive = True

    #get class objects' profession 
    def getProfession(self):
        return self.__profession
        


#=======================================================================================================================================v

# to search the image of character type in file
class Fighter(Character):
    def __init__(self, profession, name, isAi, x, y):
        super().__init__(profession, name)

        # so user input can find the image in file directory
        file_directory = "enemy" if isAi else "player"
        

        # to search in file directory
        self.image = pygame.image.load(f'img/characters/{file_directory}/{self.getProfession()}.png')
        self.image = pygame.transform.scale(self.image, (140, 160))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)



    def draw(self, screen):
        screen.blit(self.image, self.rect)            





# health bar
class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp, screen, red, green):
        # update with new health
        self.hp = hp
        # calculate health ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, red,(self.x, self.y , 150, 20))
        pygame.draw.rect(screen, green,(self.x, self.y , 150 * ratio, 20))
    
    
        