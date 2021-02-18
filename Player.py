import pygame


class Player:

    def __init__(self, screen, current_map):
        self.screen = screen
        self.map = current_map
        self.current_pos = [10, 18]
        self.inside_pos = [8, 8]

        self.sprite_front = [pygame.image.load("assets/Player/Walk/walk down1.png"),
                             pygame.image.load("assets/Player/Walk/walk down2.png"),
                             pygame.image.load("assets/Player/Walk/walk down3.png"),
                             pygame.image.load("assets/Player/Walk/walk down4.png")]
        for i in self.sprite_front:  # redimensionne les images
            self.sprite_front[self.sprite_front.index(i)] = pygame.transform.scale(i, (i.get_width()*6, i.get_height()*6))

        self.sprite_back = [pygame.image.load("assets/Player/Walk/walk up1.png"),
                            pygame.image.load("assets/Player/Walk/walk up2.png"),
                            pygame.image.load("assets/Player/Walk/walk up3.png"),
                            pygame.image.load("assets/Player/Walk/walk up4.png")]
        for i in self.sprite_back:
            self.sprite_back[self.sprite_back.index(i)] = pygame.transform.scale(i, (i.get_width()*6, i.get_height()*6))

        self.sprite_right = [pygame.image.load("assets/Player/Walk/walk right1.png"),
                             pygame.image.load("assets/Player/Walk/walk right2.png"),
                             pygame.image.load("assets/Player/Walk/walk right3.png"),
                             pygame.image.load("assets/Player/Walk/walk right4.png")]
        for i in self.sprite_right:
            self.sprite_right[self.sprite_right.index(i)] = pygame.transform.scale(i, (i.get_width()*6, i.get_height()*6))

        self.sprite_left = [pygame.image.load("assets/Player/Walk/walk left1.png"),
                            pygame.image.load("assets/Player/Walk/walk left2.png"),
                            pygame.image.load("assets/Player/Walk/walk left3.png"),
                            pygame.image.load("assets/Player/Walk/walk left4.png")]
        for i in self.sprite_left:
            self.sprite_left[self.sprite_left.index(i)] = pygame.transform.scale(i, (i.get_width()*6, i.get_height()*6))

        self.index_animation = 0
        self.index_animation_att = 0
        self.image = self.sprite_left[0]

        self.rect = self.image.get_rect()

        self.time = pygame.time.get_ticks()
        self.delay_anim = pygame.time.get_ticks()
        self.delay_attack_anim = pygame.time.get_ticks()

        self.attack_sprites_right = [pygame.image.load("assets/Player/Attack/attack right1.png"),
                                     pygame.image.load("assets/Player/Attack/attack right2.png"),
                                     pygame.image.load("assets/Player/Attack/attack right3.png"),
                                     pygame.image.load("assets/Player/Attack/attack right4.png")]
        for i in self.attack_sprites_right:
            self.attack_sprites_right[self.attack_sprites_right.index(i)] = pygame.transform.scale(i, (i.get_width()*6, i.get_height()*6))

        self.attack_sprites_left = [pygame.image.load("assets/Player/Attack/attack left1.png"),
                                    pygame.image.load("assets/Player/Attack/attack left2.png"),
                                    pygame.image.load("assets/Player/Attack/attack left3.png"),
                                    pygame.image.load("assets/Player/Attack/attack left4.png")]
        for i in self.attack_sprites_left:
            self.attack_sprites_left[self.attack_sprites_left.index(i)] = pygame.transform.scale(i, (i.get_width()*6, i.get_height()*6))

        self.attack_sprites_front = [pygame.image.load("assets/Player/Attack/attack down1.png"),
                                     pygame.image.load("assets/Player/Attack/attack down2.png"),
                                     pygame.image.load("assets/Player/Attack/attack down3.png"),
                                     pygame.image.load("assets/Player/Attack/attack down4.png")]
        for i in self.attack_sprites_front:
            self.attack_sprites_front[self.attack_sprites_front.index(i)] = pygame.transform.scale(i, (i.get_width()*6, i.get_height()*6))

        self.attack_sprites_back = [pygame.image.load("assets/Player/Attack/attack up1.png"),
                                    pygame.image.load("assets/Player/Attack/attack up2.png"),
                                    pygame.image.load("assets/Player/Attack/attack up3.png"),
                                    pygame.image.load("assets/Player/Attack/attack up4.png")]
        for i in self.attack_sprites_back:
            self.attack_sprites_back[self.attack_sprites_back.index(i)] = pygame.transform.scale(i, (i.get_width()*6, i.get_height()*6))

    def move_animation(self, direction, moving):
        self.time = pygame.time.get_ticks()

        if self.time - self.delay_anim > 70:
            self.delay_anim = self.time
            if moving:
                if self.index_animation < 3:
                    self.index_animation += 1
                else:
                    self.index_animation = 0

        if direction == "front":
            self.image = self.sprite_front[self.index_animation]
        elif direction == "back":
            self.image = self.sprite_back[self.index_animation]
        elif direction == "right":
            self.image = self.sprite_right[self.index_animation]
        elif direction == "left":
            self.image = self.sprite_left[self.index_animation]

    def attack(self, direction):
        self.time = pygame.time.get_ticks()

        if self.time - self.delay_attack_anim > 20:
            self.delay_attack_anim = self.time
            if self.index_animation_att < 3:
                self.index_animation_att += 1

        if direction == "front":
            self.image = self.attack_sprites_front[self.index_animation_att]
        elif direction == "back":
            self.image = self.attack_sprites_back[self.index_animation_att]
        elif direction == "right":
            self.image = self.attack_sprites_right[self.index_animation_att]
        elif direction == "left":
            self.image = self.attack_sprites_left[self.index_animation_att]

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
