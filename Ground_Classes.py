import pygame as pg


class Grass(pg.sprite.Sprite):  # herbe standard

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-Slice.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class BasicRoad(pg.sprite.Sprite):  # coin en haut à gauche

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile71.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class RoadLeft(pg.sprite.Sprite):  # route avec le bord à gauche

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile14.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class RoadRight(pg.sprite.Sprite):  # route avec le bord à droite

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile48.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class RoadTop(pg.sprite.Sprite):  # route avec le bord en haut

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile25.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class RoadBot(pg.sprite.Sprite):  # route avec le bord en bas

    def __init__(self, coordinates):

        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile52.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class RoadTopLeftFull(pg.sprite.Sprite):  # coin en haut à gauche

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile19.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class RoadTopLeftEmpty(pg.sprite.Sprite):  # coin en haut à gauche

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile71.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class RoadBotRightEmpty(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile51.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class RoadBotRightFull(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile62.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class RoadTopRightFull(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile60.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class RoadBotLeftFull(pg.sprite.Sprite):  # coin en haut à gauche

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile61.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class RoadBotLeftEmpty(pg.sprite.Sprite):  # coin en haut à gauche

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile58.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class RoadTopRightEmpty(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile56.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class InsideGround(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Inside House/Sol.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates


class InsideWall(pg.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()

        self.image = pg.image.load("assets/Inside House/Mur.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates
