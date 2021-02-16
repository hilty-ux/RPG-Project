import pygame as pg


class BlueTree(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/props n decorations/generic-rpg-tree01.png")
        self.image = pg.transform.scale(self.image, (159, 222))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class RedTree(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/props n decorations/generic-rpg-tree02.png")
        self.image = pg.transform.scale(self.image, (159, 222))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class Fern(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/props n decorations/generic-rpg-grass01.png")
        self.image = pg.transform.scale(self.image, (39, 21))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class Lake(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/props n decorations/generic-rpg-mini-lake.png")
        self.image = pg.transform.scale(self.image, (200, 200))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates