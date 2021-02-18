import pygame

import Player
import text
import Decoration_Classes as Dc
import Ground_Classes as Gr
import Ennemies as En


class Game:

    def __init__(self, screen):

        self.screen = screen
        self.beginning = True
        self.running = True
        self.inside_house = False

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self.tree = pygame.image.load("assets/Trees/Nature Tree 100w.png")
        self.slab = pygame.image.load("assets/Road/Slab Autumn 100w.png")
        self.grass = pygame.image.load("assets/Grass/Grass Autumn 100w.png")
        self.rock = pygame.image.load("assets/Road/rock 100w.png")

        self.second_grass = pygame.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-Slice.png")
        self.second_grass = pygame.transform.scale(self.second_grass, (100, 100))
        self.second_tree = pygame.image.load(
            "assets/Assets rpg pack/rpg-pack/props n decorations/generic-rpg-tree01.png")
        self.second_tree = pygame.transform.scale(self.second_tree, (53 * 3, 74 * 3))
        self.fern = pygame.image.load("assets/Assets rpg pack/rpg-pack/props n decorations/generic-rpg-grass01.png")
        self.fern = pygame.transform.scale(self.fern, (13 * 3, 7 * 3))
        self.second_road_left = pygame.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile14.png")
        self.second_road_right = pygame.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile48.png")
        self.second_road_right = pygame.transform.scale(self.second_road_right, (100, 100))
        self.second_road_left = pygame.transform.scale(self.second_road_left, (100, 100))
        self.road_corner_top_left = pygame.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile19.png")
        self.road_corner_top_left = pygame.transform.scale(self.road_corner_top_left, (100, 100))
        self.third_tree = pygame.image.load(
            "assets/Assets rpg pack/rpg-pack/props n decorations/generic-rpg-tree02.png")
        self.third_tree = pygame.transform.scale(self.third_tree, (54 * 3, 74 * 3))
        self.road_corner_bottom_right_empty = pygame.image.load(
            "assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile51.png")
        self.road_corner_bottom_right_empty = pygame.transform.scale(self.road_corner_bottom_right_empty, (100, 100))
        self.road_top = pygame.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile25.png")
        self.road_top = pygame.transform.scale(self.road_top, (100, 100))
        self.road_bot = pygame.image.load("assets/Assets rpg pack/rpg-pack/tiles/generic-rpg-tile52.png")
        self.road_bot = pygame.transform.scale(self.road_bot, (100, 100))
        self.lake = pygame.image.load("assets/Assets rpg pack/rpg-pack/props n decorations/generic-rpg-mini-lake.png")
        self.lake = pygame.transform.scale(self.lake, (200, 200))

        # crée les maps, sous formes de listes de listes contenant pour chaque chiffre une information sur le bloc,
        # il y a différentes listes pour représenter différentes "couches", d'abord le sol, puis les objets decoratifs
        self.map_ground = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 4, 6, 6, 6, 6, 6, 8, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 5, 7, 7, 7, 7, 9, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # pour rendre le mouvement plus fluide, la classe du joueur est deux fois plus importantes que celle de
        # l'environnement, pour que le joueur se déplace de demi-cases mais que l'environnement soit constitué de
        # cases à part entière
        self.map_player = [
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
         [0, 0, 0, 0, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
         [0, 3, 3, 0, 0, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
         [0, 3, 3, 3, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
         [0, 3, 3, 3, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 3, 3, 3, 1, 1, 1, 1, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 3, 3, 0, 1, 1, 1, 1, 0, 0, 0, 9, 8, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.map_others = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0],
                           [0, 6, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
                           [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0],
                           [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 2, 0, 4, 0, 0, 0, 2, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
                           [0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0],
                           [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 6, 0, 0],
                           [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.map_hostile = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 2, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 2, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 2, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # initialise les variables relatives au joueur ; sa direction de départ, ses statuts ainsi que sa classe
        self.pl = Player.Player(self.screen, self.map_player)
        self.direction = "right"
        self.moving = False
        self.attacking = False

        # crée un dictionnaire de touches préssées ou non
        self.pressed = {}
        # initialise les variables de temps
        self.clock = pygame.time.Clock()
        self.current_time = pygame.time.get_ticks()
        self.delay_movement = pygame.time.get_ticks()

        # initialises la classe de texte
        self.txt = text.PopUp(self.screen)

        # pour faciliter l'écriture de la fonction pour transformer les listes (maps) en groupe de sprites,
        # création de multiples fonctions lambda pour ajouter un bloc spécifique avec des coordonnées spécifiques
        # à un groupe spécifique (il y a un groupe à part pour les arbres pour les afficher au dessus du joueur
        # et non pas en dessous comme pour les hautes herbes ou le lac
        self.decorative_group_tree = pygame.sprite.Group()
        self.decorative_group_others = pygame.sprite.Group()
        self.house_group = pygame.sprite.Group()
        self.add_red_tree = lambda x, y: self.decorative_group_tree.add(Dc.RedTree((x, y)))
        self.add_blue_tree = lambda x, y: self.decorative_group_tree.add(Dc.BlueTree((x, y)))
        self.add_fern = lambda x, y: self.decorative_group_others.add(Dc.Fern((x, y)))
        self.add_lake = lambda x, y: self.decorative_group_others.add(Dc.Lake((x, y)))
        self.add_house = lambda x, y: self.house_group.add(Dc.House((x, y)))
        self.add_rock = lambda x, y: self.decorative_group_others.add(Dc.Rock((x, y)))
        self.add_barrier = lambda x, y: self.decorative_group_others.add(Dc.Barrier((x, y)))

        self.ground_group = pygame.sprite.Group()
        self.add_grass = lambda x, y: self.ground_group.add(Gr.Grass((x, y)))
        self.add_road_left = lambda x, y: self.ground_group.add(Gr.RoadLeft((x, y)))
        self.add_road_right = lambda x, y: self.ground_group.add(Gr.RoadRight((x, y)))
        self.add_road_bot = lambda x, y: self.ground_group.add(Gr.RoadBot((x, y)))
        self.add_road_top = lambda x, y: self.ground_group.add(Gr.RoadTop((x, y)))
        self.add_road_top_left_corner_full = lambda x, y: self.ground_group.add(Gr.RoadTopLeftFull((x, y)))
        self.add_road_bot_left_corner_empty = lambda x, y: self.ground_group.add(Gr.RoadBotRightEmpty((x, y)))
        self.add_road_bot_right_corner_full = lambda x, y: self.ground_group.add(Gr.RoadBotRightFull((x, y)))
        self.add_road_top_right_corner_full = lambda x, y: self.ground_group.add(Gr.RoadTopRightFull((x, y)))

        # partie du monstre
        self.mon = En.Monster(self.screen, self.map_hostile)
        self.monster_group = pygame.sprite.Group()
        self.monster_group.add(self.mon)

        # seconde map (intérieur maison)

        self.inside_house_map = [[0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0]]

        self.inside_house_map_player = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.flou = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        self.flou.fill((255, 255, 255))
        self.flou.set_alpha(200)

    def show_map(self):

        # va analyser la map pour ajouter à un groupe tous les sols avec leurs coordonnées correspondantes
        # si dans la map il y a un 0 par exemple, cela ajoutera un bloc d'herbe
        # au coordonnées [][index*100], [index*100][]
        for row in range(len(self.map_ground)):
            for cell in range(len(self.map_ground[row])):
                if self.map_ground[row][cell] == 0:
                    self.add_grass(cell * 100, row * 100)
                elif self.map_ground[row][cell] == 1:
                    self.add_road_left(cell * 100, row * 100)
                elif self.map_ground[row][cell] == 2:
                    self.add_road_right(cell * 100, row * 100)
                elif self.map_ground[row][cell] == 4:
                    self.add_road_top_left_corner_full(cell * 100, row * 100)
                elif self.map_ground[row][cell] == 5:
                    self.add_road_bot_left_corner_empty(cell * 100, row * 100)
                elif self.map_ground[row][cell] == 6:
                    self.add_road_top(cell * 100, row * 100)
                elif self.map_ground[row][cell] == 7:
                    self.add_road_bot(cell * 100, row * 100)
                elif self.map_ground[row][cell] == 8:
                    self.add_road_top_right_corner_full(cell * 100, row * 100)
                elif self.map_ground[row][cell] == 9:
                    self.add_road_bot_right_corner_full(cell * 100, row * 100)

    def show_decorative(self):

        # va analyser la map pour mettre dans un groupe tous les objets décoratifs renseignés sur la liste
        # avec les coordonnées correspondantes
        for row in range(len(self.map_others)):
            for cell in range(len(self.map_others[row])):
                if self.map_others[row][cell] == 1:
                    self.add_blue_tree(cell * 100, row * 100)
                elif self.map_others[row][cell] == 2:
                    self.add_fern(cell * 100, row * 100)
                elif self.map_others[row][cell] == 3:
                    self.add_red_tree(cell * 100, row * 100)
                elif self.map_others[row][cell] == 4:
                    self.add_lake(cell * 100, row * 100)
                elif self.map_others[row][cell] == 5:
                    self.add_house(cell * 100, row * 100)
                elif self.map_others[row][cell] == 6:
                    self.add_rock(cell * 100, row * 100)
                elif self.map_others[row][cell] == 7:
                    self.add_barrier(cell * 100, row * 100)
                else:
                    pass

    def find_collision(self):

        for sprite in self.monster_group:
            if self.pl.rect.colliderect(sprite.rect):
                sprite.kill()

    def main_loop(self):

        # barre de chargement
        self.show_decorative()
        pygame.draw.rect(self.screen, (0, 255, 0), [self.screen.get_width() // 4, self.screen.get_height() // 2,
                                                    self.screen.get_width() // 4, 25])
        pygame.display.flip()
        self.show_map()
        pygame.draw.rect(self.screen, (0, 255, 0), [self.screen.get_width() // 2, self.screen.get_height() // 2,
                                                    self.screen.get_width() // 4, 25])
        pygame.display.flip()

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    self.pressed[event.key] = True
                    self.moving = True
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if event.type == pygame.KEYUP:
                    self.pressed[event.key] = False
                    self.moving = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and not self.attacking:
                        self.attacking = True

            # limite le mouvement du joueur à 1 toutes les 50 ms
            if self.current_time - self.delay_movement > 50:
                # reset le délai
                self.delay_movement = self.current_time
                # si le joueur n'est pas en train d'attaquer, le fait bouger
                if not self.attacking:
                    if self.pressed.get(pygame.K_z):
                        self.pl.move("up", self.inside_house_map_player, self.inside_house)
                        self.direction = "back"
                    if self.pressed.get(pygame.K_s):
                        self.pl.move("down", self.inside_house_map_player, self.inside_house)
                        self.direction = "front"
                    if self.pressed.get(pygame.K_q):
                        self.pl.move("left", self.inside_house_map_player, self.inside_house)
                        self.direction = "left"
                    if self.pressed.get(pygame.K_d):
                        self.pl.move("right", self.inside_house_map_player, self.inside_house)
                        self.direction = "right"

            # dessine/met à jour tous les composants du jeu (sol, joueur, décoration...)
            self.ground_group.draw(self.screen)
            self.decorative_group_others.draw(self.screen)
            if self.pl.current_pos[1] > 11:
                self.house_group.draw(self.screen)
                if self.map_player[self.pl.current_pos[1]][self.pl.current_pos[0]] == 9 or\
                        self.map_player[self.pl.current_pos[1]][self.pl.current_pos[0]] == 8:
                    pygame.draw.polygon(self.screen, (88, 41, 0), [(780, 688), (835, 689), (835, 751), (779, 752)])
            self.monster_group.draw(self.screen)
            self.monster_group.update(self.pl.current_pos)
            self.pl.update(self.inside_house)
            self.pl.move_animation(self.direction, self.moving)
            if self.pl.current_pos[1] <= 11:
                self.house_group.draw(self.screen)
            self.decorative_group_tree.draw(self.screen)
            # anime le joueur si il est en train d'attaquer
            if self.attacking:
                self.pl.attack(self.direction)
                if self.pl.index_animation_att == 2:
                    if 35 > self.pl.current_pos[0] > 25 and \
                            0 < self.pl.current_pos[1] < 10:
                        self.find_collision()
                if self.pl.attack(self.direction) == "end":
                    self.attacking = False
                    self.pl.index_animation_att = 0

            if self.map_player[self.pl.current_pos[1]][self.pl.current_pos[0]] == 8:
                self.inside_house = True

            if self.inside_house:
                self.screen.blit(self.flou, (0, 0))
                pygame.draw.rect(self.screen, (0, 0, 0), [250, 250, 800, 450])
                self.pl.update(self.inside_house)
                if self.inside_house_map_player[self.pl.inside_pos[1]-1][self.pl.inside_pos[0]-1] == 9:
                    self.inside_house = False
                    self.pl.current_pos = [30, 2]
                    self.pl.inside_pos = [8, 8]

            if len(self.monster_group) == 0:
                self.running = False

            pygame.mouse.set_visible(False)  # rends invisible la souris
            self.current_time = pygame.time.get_ticks()  # met à jour le temps
            pygame.display.flip()  # met à jour l'écran
            self.clock.tick(60)  # met les FPS à 60


# si raspberry => pygame.display.set_mode((1900, 1000))
# si windows => pygame.display.set_mode((0, 0), pygame.FULLSCREEN
# si mac => qui a un mac ?
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.init()

game = Game(screen)
game.main_loop()

pygame.quit()
