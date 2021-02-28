import pygame


class Player:

    def __init__(self, screen, current_map):
        self.screen = screen
        self.map = current_map
        self.current_pos = [35, 1]
        self.inside_pos = [1, 4]
        self.life = 100
        self.W = self.screen.get_width()
        self.H = self.screen.get_height()

        self.sprite_front = [pygame.image.load("assets/Player2/Walk/walk down1.png"),
                             pygame.image.load("assets/Player2/Walk/walk down2.png"),
                             pygame.image.load("assets/Player2/Walk/walk down3.png"),
                             pygame.image.load("assets/Player2/Walk/walk down4.png")]
        for i in self.sprite_front:  # redimensionne les images
            self.sprite_front[self.sprite_front.index(i)] = pygame.transform.scale(i, (i.get_width()*6, i.get_height()*6))

        self.sprite_back = [pygame.image.load("assets/Player2/Walk/walk up1.png"),
                            pygame.image.load("assets/Player2/Walk/walk up2.png"),
                            pygame.image.load("assets/Player2/Walk/walk up3.png"),
                            pygame.image.load("assets/Player2/Walk/walk up4.png")]
        for i in self.sprite_back:
            self.sprite_back[self.sprite_back.index(i)] = pygame.transform.scale(i, (i.get_width()*6, i.get_height()*6))

        self.sprite_right = [pygame.image.load("assets/Player2/Walk/walk right1.png"),
                             pygame.image.load("assets/Player2/Walk/walk right2.png"),
                             pygame.image.load("assets/Player2/Walk/walk right3.png"),
                             pygame.image.load("assets/Player2/Walk/walk right4.png")]
        for i in self.sprite_right:
            self.sprite_right[self.sprite_right.index(i)] = pygame.transform.scale(i, (i.get_width()*6, i.get_height()*6))

        self.sprite_left = [pygame.image.load("assets/Player2/Walk/walk left1.png"),
                            pygame.image.load("assets/Player2/Walk/walk left2.png"),
                            pygame.image.load("assets/Player2/Walk/walk left3.png"),
                            pygame.image.load("assets/Player2/Walk/walk left4.png")]
        for i in self.sprite_left:
            self.sprite_left[self.sprite_left.index(i)] = pygame.transform.scale(i, (i.get_width()*6, i.get_height()*6))

        self.index_animation = 0
        self.index_animation_att = 0
        self.image = self.sprite_left[0]

        self.rect = self.image.get_rect()

        self.time = pygame.time.get_ticks()
        self.delay_anim = pygame.time.get_ticks()
        self.delay_attack_anim = pygame.time.get_ticks()

        self.attack_sprites_right = [pygame.image.load("assets/Player2/Attack/attack right1.png"),
                                     pygame.image.load("assets/Player2/Attack/attack right2.png"),
                                     pygame.image.load("assets/Player2/Attack/attack right3.png"),
                                     pygame.image.load("assets/Player2/Attack/attack right4.png")]
        for i in self.attack_sprites_right:
            self.attack_sprites_right[self.attack_sprites_right.index(i)] = pygame.transform.scale(i, (i.get_width()*6, i.get_height()*6))

        self.attack_sprites_left = [pygame.image.load("assets/Player2/Attack/attack left1.png"),
                                    pygame.image.load("assets/Player2/Attack/attack left2.png"),
                                    pygame.image.load("assets/Player2/Attack/attack left3.png"),
                                    pygame.image.load("assets/Player2/Attack/attack left4.png")]
        for i in self.attack_sprites_left:
            self.attack_sprites_left[self.attack_sprites_left.index(i)] = pygame.transform.scale(i, (i.get_width()*6, i.get_height()*6))

        self.attack_sprites_front = [pygame.image.load("assets/Player2/Attack/attack down1.png"),
                                     pygame.image.load("assets/Player2/Attack/attack down2.png"),
                                     pygame.image.load("assets/Player2/Attack/attack down3.png"),
                                     pygame.image.load("assets/Player2/Attack/attack down4.png")]
        for i in self.attack_sprites_front:
            self.attack_sprites_front[self.attack_sprites_front.index(i)] = pygame.transform.scale(i, (i.get_width()*6, i.get_height()*6))

        self.attack_sprites_back = [pygame.image.load("assets/Player2/Attack/attack up1.png"),
                                    pygame.image.load("assets/Player2/Attack/attack up2.png"),
                                    pygame.image.load("assets/Player2/Attack/attack up3.png"),
                                    pygame.image.load("assets/Player2/Attack/attack up4.png")]
        for i in self.attack_sprites_back:
            self.attack_sprites_back[self.attack_sprites_back.index(i)] = pygame.transform.scale(i, (i.get_width()*6, i.get_height()*6))

        self.police_name = pygame.font.Font("assets/Police/advanced_pixel-7.ttf", 50)
        self.name = self.police_name.render("Red Player", True, (255, 0, 0))
        self.name_rect = self.name.get_rect()
        self.name_rect.x, self.name_rect.y = self.W - 10 - self.name.get_width(), 15

        self.block_back = pygame.image.load("assets/Player2/Block/block up.png")
        self.block_back = pygame.transform.scale(self.block_back,
                                                 (self.block_back.get_width() * 6, self.block_back.get_height() * 6))

        self.block_front = pygame.image.load("assets/Player2/Block/block down.png")
        self.block_front = pygame.transform.scale(self.block_front,
                                                  (self.block_front.get_width() * 6, self.block_front.get_height() * 6))

        self.block_left = pygame.image.load("assets/Player2/Block/block left.png")
        self.block_left = pygame.transform.scale(self.block_left,
                                                 (self.block_left.get_width() * 6, self.block_left.get_height() * 6))
        self.block_right = pygame.image.load("assets/Player2/Block/block right.png")
        self.block_right = pygame.transform.scale(self.block_right,
                                                  (self.block_right.get_width() * 6, self.block_right.get_height() * 6))

    def move_animation(self, direction, moving, blocking):
        self.time = pygame.time.get_ticks()

        if not blocking:
            if self.time - self.delay_anim > 70:
                self.delay_anim = self.time
                for i in moving:
                    if i:
                        if self.index_animation < 3:
                            self.index_animation += 1
                        else:
                            self.index_animation = 0
                        break

            if direction == "front":
                self.image = self.sprite_front[self.index_animation]
            elif direction == "back":
                self.image = self.sprite_back[self.index_animation]
            elif direction == "right":
                self.image = self.sprite_right[self.index_animation]
            elif direction == "left":
                self.image = self.sprite_left[self.index_animation]

        else:
            if direction == "front":
                self.image = self.block_front
            elif direction == "back":
                self.image = self.block_back
            elif direction == "right":
                self.image = self.block_right
            elif direction == "left":
                self.image = self.block_left

    def attack(self, direction):
        self.time = pygame.time.get_ticks()

        # délai entre chaque frame est de 22 ms
        if self.time - self.delay_attack_anim > 22:
            self.delay_attack_anim = self.time
            if self.index_animation_att < 3:
                self.index_animation_att += 1

        # en fonction de la direction les sprites sont différentes
        if direction == "front":
            self.image = self.attack_sprites_front[self.index_animation_att]
        elif direction == "back":
            self.image = self.attack_sprites_back[self.index_animation_att]
        elif direction == "right":
            self.image = self.attack_sprites_right[self.index_animation_att]
        elif direction == "left":
            self.image = self.attack_sprites_left[self.index_animation_att]

        # dis si l'animation est terminée ou pas pour savoir si le joueur peut bouger ou non
        if self.index_animation_att < 3:
            return "not ended"
        else:
            return "end"

    def move(self, direction, inside_map, inside):

        if not inside:
            if direction == "up":
                try:
                    if self.map[self.current_pos[1] - 1][self.current_pos[0]] != 3:
                        if self.current_pos[1] > 0:
                            self.current_pos[1] -= 1
                except IndexError as e:
                    print(e)
            elif direction == "down":
                try:
                    if self.map[self.current_pos[1] + 1][self.current_pos[0]] != 3:
                        self.current_pos[1] += 1
                except IndexError as e:
                    print(e)
            elif direction == "left":
                try:
                    if self.map[self.current_pos[1]][self.current_pos[0] - 1] != 3:
                        if self.current_pos[0] > 0:
                            self.current_pos[0] -= 1
                except IndexError as e:
                    print(e)
            elif direction == "right":
                try:
                    if self.map[self.current_pos[1]][self.current_pos[0] + 1] != 3:
                        self.current_pos[0] += 1
                except IndexError as e:
                    print(e)
        else:
            if direction == "up":
                try:
                    if inside_map[self.inside_pos[1] - 1][self.inside_pos[0]] != 3:
                        if self.inside_pos[1] > 0:
                            self.inside_pos[1] -= 1
                except IndexError as e:
                    print(e)
            elif direction == "down":
                try:
                    if inside_map[self.inside_pos[1] + 1][self.inside_pos[0]] != 3:
                        self.inside_pos[1] += 1
                except IndexError as e:
                    print(e)
            elif direction == "left":
                try:
                    if inside_map[self.inside_pos[1]][self.inside_pos[0] - 1] != 3:
                        if self.inside_pos[0] > 0:
                            self.inside_pos[0] -= 1
                except IndexError as e:
                    print(e)
            elif direction == "right":
                try:
                    if inside_map[self.inside_pos[1]][self.inside_pos[0] + 1] != 3:
                        self.inside_pos[0] += 1
                except IndexError as e:
                    print(e)

    def update(self, inside_house):
        self.rect = self.image.get_rect()
        try:
            print(self.map[self.current_pos[1]][self.current_pos[0]], self.current_pos)
        except Exception as e:
            print(e)
        if not inside_house:
            self.rect.center = self.current_pos[0] * 50 + 25, self.current_pos[1] * 50 + 25
            self.screen.blit(self.image, self.rect)
        else:
            self.rect.center = self.inside_pos[0] * 50 + 25 + 250, self.inside_pos[1] * 50 + 25 + 250
            self.screen.blit(self.image, self.rect)

    def life_bar(self):

        pygame.draw.rect(self.screen, (0, 0, 0), [self.W - 10 - (self.W // 2 - 150), 5, self.W // 2 - 150, 10])
        pygame.draw.rect(self.screen, (255, 0, 0),
                         [self.W - 10 - (((self.W // 2 - 150) // 100) * self.life), 5, ((self.W // 2 - 150) // 100) * self.life,
                          10])
        self.screen.blit(self.name, self.name_rect)
