import pygame
from random import randint


class Monster(pygame.sprite.Sprite):

    def __init__(self, screen, map_hostile):
        super().__init__()
        self.screen = screen
        self.map_hostile = map_hostile
        self.image = pygame.Surface((100, 100))
        self.rect = self.image.get_rect()

        self.current_pos = [13, 2]
        self.current_inside_house_pos = [0, 0]

        self.rect.x, self.rect.y = self.current_pos[0]*100, self.current_pos[1]*100

        self.frames = [pygame.image.load("assets/Bald Mob/tile000.png"),
                       pygame.image.load("assets/Bald Mob/tile001.png"),
                       pygame.image.load("assets/Bald Mob/tile002.png"),
                       pygame.image.load("assets/Bald Mob/tile003.png"),
                       pygame.image.load("assets/Bald Mob/tile004.png"),
                       pygame.image.load("assets/Bald Mob/tile005.png"),
                       pygame.image.load("assets/Bald Mob/tile006.png"),
                       pygame.image.load("assets/Bald Mob/tile007.png"),
                       pygame.image.load("assets/Bald Mob/tile008.png"),
                       pygame.image.load("assets/Bald Mob/tile009.png"),
                       pygame.image.load("assets/Bald Mob/tile010.png"),
                       pygame.image.load("assets/Bald Mob/tile011.png"),
                       pygame.image.load("assets/Bald Mob/tile012.png"),
                       pygame.image.load("assets/Bald Mob/tile013.png"),
                       pygame.image.load("assets/Bald Mob/tile014.png")]

        for i in range(len(self.frames)):
            self.frames[i] = pygame.transform.scale(self.frames[i], (80, 80))

        self.index_animation = 0
        self.image = self.frames[self.index_animation]

        self.current_time = pygame.time.get_ticks()
        self.delay = pygame.time.get_ticks()
        self.delay_movement = pygame.time.get_ticks()

    def moving(self, player_pos):
        """On décide ce que fait le monstre, s'il se déplace dans sa routine de déplacement
        ou s'il se met à poursuivre/attaquer le joueur"""

        # d'abord on traduit la position du joueur reçue, car elle n'est pas donnée sur la meme longueur
        # de liste et il peut ainsi y avoir des problèmes d'indexs

        player_pos = [i // 2 for i in player_pos]

        chase = False
        routine = False
        attack = False

        # en fonction de ou se trouve le joueur, l'ordinateur va choisir s'il le poursuit ou non, s'il l'attaque
        # ou non, ou s'il ne fait rien, ainsi, on récupère la map consacrée au monstre pour trouver la zone dans
        # laquelle le joueur se trouve
        if self.map_hostile[player_pos[1]][player_pos[0]] == 2:
            chase = False
        elif self.map_hostile[player_pos[1]][player_pos[0]] == 1:
            attack = False
        else:
            routine = True

        if self.current_time - self.delay_movement > 500:
            self.delay_movement = self.current_time
            if chase:
                pass  # how ?
            elif attack:
                pass  # how ?
            elif routine:
                choice = randint(1, 4)  # 1 => droite, 2 => gauche, 3 => haut, 4 => bas
                if choice == 1:
                    if self.map_hostile[self.current_pos[1]][self.current_pos[0]+1] == 1:
                        self.current_pos[0] += 1
                elif choice == 2:
                    if self.map_hostile[self.current_pos[1]][self.current_pos[0]-1] == 1:
                        self.current_pos[0] -= 1
                elif choice == 3:
                    if self.map_hostile[self.current_pos[1]-1][self.current_pos[0]] == 1:
                        self.current_pos[1] -= 1
                elif choice == 4:
                    if self.map_hostile[self.current_pos[1]+1][self.current_pos[0]] == 1:
                        self.current_pos[1] += 1

    def animation(self):

        self.current_time = pygame.time.get_ticks()

        if self.current_time - self.delay > 50:
            if self.index_animation < len(self.frames)-1:
                self.index_animation += 1
                self.delay = self.current_time
            else:
                self.index_animation = 0
                self.delay = self.current_time

        self.image = self.frames[self.index_animation]

    def update(self, current_pos):

        self.animation()
        self.moving(current_pos)

        self.rect.x, self.rect.y = self.current_pos[0]*100, self.current_pos[1]*100