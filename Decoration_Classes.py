import pygame as pg

"""Chaque classes représente une décoration différent, ces classes héritent de la superclasse pg.sprite.Sprite,
afin qu'ils soit ajoutable dans un groupe."""


class BlueTree(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/props n decorations/generic-rpg-tree01.png")
        self.image = pg.transform.scale(self.image, (159, 222))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates

    def update(self, resize):
        if resize:
            self.image = pg.transform.scale(self.image, (79, 110))


class RedTree(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/props n decorations/generic-rpg-tree02.png")
        self.image = pg.transform.scale(self.image, (159, 222))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates

    def update(self, resize):
        if resize:
            self.image = pg.transform.scale(self.image, (79, 110))


class Fern(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/props n decorations/generic-rpg-grass01.png")
        self.image = pg.transform.scale(self.image, (39, 21))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates

    def update(self, resize):
        if resize:
            self.image = pg.transform.scale(self.image, (52, 28))


class Lake(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/props n decorations/generic-rpg-mini-lake.png")
        self.image = pg.transform.scale(self.image, (200, 200))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates

    def update(self, resize):
        if resize:
            self.image = pg.transform.scale(self.image, (100, 100))


class House(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/props n decorations/generic-rpg-house-inn.png")
        self.image = pg.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates

    def update(self, resize):
        if resize:
            self.image = pg.transform.scale(self.image, (84, 105))


class Rock(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/props n decorations/generic-rpg-rock05.png")
        self.image = pg.transform.scale(self.image, (21*3, 15*3))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates

    def update(self, resize):
        if resize:
            self.image = pg.transform.scale(self.image, (63, 45))


class Barrier(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/props n decorations/generic-rpg-fence-complete.png")
        self.image = pg.transform.scale(self.image, (67*7, 62*8))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates

    def update(self, resize):
        if resize:
            self.image = pg.transform.scale(self.image, (100, 100))


class CaveStair(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Inside House/CaveStair.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates

    def update(self, resize):
        if resize:
            self.image = pg.transform.scale(self.image, (100, 100))


class CaveStair2(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Inside House/CaveStair2.png")
        self.image = pg.transform.scale(self.image, (200, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates

    def update(self, resize):
        if resize:
            self.image = pg.transform.scale(self.image, (100, 100))


class Column(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Inside House/Column.png")
        self.image = pg.transform.scale(self.image, (100, 200))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates

    def update(self, resize):
        if resize:
            self.image = pg.transform.scale(self.image, (50, 100))


class Skull(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Inside House/Crane.png")
        self.image = pg.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates

    def update(self, resize):
        if resize:
            self.image = pg.transform.scale(self.image, (50, 50))
