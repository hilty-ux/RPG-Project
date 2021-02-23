import pygame
import json


class MainDisplay:

    def __init__(self, screen):
        self.screen = screen
        self.W = self.screen.get_width()
        self.H = self.screen.get_height()

        with open("map storage/map.json") as m:
            self.maps = json.load(m)

        self.maps_group = pygame.sprite.Group()

        index = 0
        for name, dict_ in self.maps["all maps"].items():
            self.maps_group.add(CreateFile(self.screen, dict_['path_preview'], name, index))
            print(index)
            index += 1

        self.police = pygame.font.Font("assets/Police/advanced_pixel-7.ttf", 50)
        self.button_restore_default = self.police.render("Restore Default Map", True, (0, 0, 0))
        self.button_restore_default_rect = self.button_restore_default.get_rect()
        self.button_restore_default_surf = pygame.Surface((350, 50))
        self.button_restore_default_surf.fill((255, 255, 255))
        self.button_restore_default_surf_rect = self.button_restore_default_surf.get_rect()

        self.button_restore_default_rect.left = 50
        self.button_restore_default_rect.y = self.H - 50
        self.button_restore_default_surf_rect.left = 25
        self.button_restore_default_surf_rect.y = self.H - 50

    def update(self):
        for table in self.maps_group:
            table.remove()

        index = 0
        for name, dict_ in self.maps["all maps"].items():
            self.maps_group.add(CreateFile(self.screen, dict_['path_preview'], name, index))
            index += 1

    def display(self):

        self.screen.fill((0, 0, 0))
        self.maps_group.draw(self.screen)
        if self.button_restore_default_surf_rect.collidepoint(pygame.mouse.get_pos()):
            self.button_restore_default_surf.fill((255, 0, 0))
        else:
            self.button_restore_default_surf.fill((255, 255, 255))
        self.screen.blit(self.button_restore_default_surf, self.button_restore_default_surf_rect)
        self.screen.blit(self.button_restore_default, self.button_restore_default_rect)


def play_map(name):
    with open("map storage/actual_map.json") as actual_map:
        current_map = json.load(actual_map)

    current_map["actual_map"] = name

    with open("map storage/actual_map.json", "w") as actual_map:
        json.dump(current_map, actual_map, indent=2)


# variable pour savoir si le main.py doit mettre à jour la map
update_map = False


class CreateFile(pygame.sprite.Sprite):

    def __init__(self, screen, path, name, index):
        super().__init__()

        with open("map storage/map.json") as m:
            self.actual_map = json.load(m)
            self.actual_map = name

        self.screen = screen
        self.W = self.screen.get_width()
        self.H = self.screen.get_height()
        self.name = name
        self.image = pygame.Surface((self.W - 200, 300))
        self.image.fill((255, 255, 255))

        self.preview = pygame.image.load(path)
        self.preview = pygame.transform.scale(self.preview, (self.W // 4, self.H // 4))
        self.image.blit(self.preview, (self.image.get_width() - 300 - self.preview.get_width(), 15))

        self.police_title = pygame.font.Font("assets/Police/advanced_pixel-7.ttf", 100)
        self.police_writes = pygame.font.Font("assets/Police/advanced_pixel-7.ttf", 50)

        self.title = self.police_title.render(name, True, (0, 0, 0))
        self.commentary = self.police_writes.render("Preview :", True, (0, 0, 0))

        self.rect_title = self.title.get_rect()
        self.rect_title.left = 20
        self.rect_title.y = 20
        self.image.blit(self.title, self.rect_title)
        self.rect_comment = self.commentary.get_rect()
        self.rect_comment.right = self.image.get_width() - 325 - self.preview.get_width()
        self.rect_comment.y = 25
        self.image.blit(self.commentary, self.rect_comment)

        self.police_buttons = pygame.font.Font("assets/Police/advanced_pixel-7.ttf", 120)
        self.buttons = [self.police_buttons.render("Play", True, (0, 0, 0)),
                        self.police_buttons.render("Edit", True, (0, 0, 0))]
        self.buttons_rect = [i.get_rect() for i in self.buttons]
        self.shining_surf = [pygame.Surface((200, 100)),
                             pygame.Surface((200, 100))]
        for i in self.shining_surf:
            i.fill((0, 255, 0))
        self.shining_rect = [pygame.Rect(0, 0, 200, 100),
                             pygame.Rect(0, 0, 200, 100)]

        for i in range(2):
            self.buttons_rect[i].center = self.image.get_width() - 150, 100 + i * 100
            self.image.blit(self.buttons[i], self.buttons_rect[i])

        for i in range(2):
            self.shining_rect[i].center = self.buttons_rect[i].center

        self.button_delete = self.police_buttons.render("delete", True, (0, 0, 0))
        self.button_delete_rect = self.button_delete.get_rect()
        self.button_delete_surf = pygame.Surface((250, 75))
        self.button_delete_surf_rect = self.button_delete_surf.get_rect()
        self.button_delete_surf.fill((255, 255, 255))

        self.button_delete_rect.left = 25
        self.button_delete_rect.bottom = 300
        self.button_delete_surf_rect.center = self.button_delete_rect.center

        self.image.blit(self.button_delete_surf, self.button_delete_surf_rect)
        self.image.blit(self.button_delete, self.button_delete_rect)

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = index * 325

    def delete(self):
        with open("map storage/map.json") as map_:
            maps = json.load(map_)

        del maps["all maps"][self.name]

        with open("map storage/map.json", "w") as map_:
            json.dump(maps, map_)

        self.kill()

    def update(self, move, click, pos):
        global update_map

        if move == "up":
            self.rect.y -= 40
        elif move == "down":
            self.rect.y += 40

        if click:
            if self.shining_rect[0].collidepoint((pos[0] - self.rect.x, pos[1] - self.rect.y)):
                play_map(self.name)
                update_map = True
            elif self.shining_rect[1].collidepoint((pos[0] - self.rect.x, pos[1] - self.rect.y)):
                print("edit")

            if self.button_delete_surf_rect.collidepoint((pos[0] - self.rect.x, pos[1] - self.rect.y)):
                self.delete()

        for i in range(2):
            if self.shining_rect[i].collidepoint((pos[0] - self.rect.x, pos[1] - self.rect.y)):
                self.shining_surf[i].fill((255, 0, 0))
            else:
                self.shining_surf[i].fill((255, 255, 255))

        if self.button_delete_surf_rect.collidepoint((pos[0] - self.rect.x, pos[1] - self.rect.y)):
            self.button_delete_surf.fill((255, 0, 0))
        else:
            self.button_delete_surf.fill((255, 255, 255))

        self.image.blit(self.button_delete_surf, self.button_delete_surf_rect)
        self.image.blit(self.button_delete, self.button_delete_rect)

        for i in range(2):
            self.image.blit(self.shining_surf[i], self.shining_rect[i])

        for i in range(2):
            self.image.blit(self.buttons[i], self.buttons_rect[i])
