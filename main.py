import pygame
from sys import platform
import json

# importe tous les autres fichiers
import Player
import Player2
import text
import Decoration_Classes as Dc
import Ground_Classes as Gr
import Ennemies as En
import Map_Editor as Me
import map_loader as ml
import Sound_manager as Sm
import Display_ath as D_ath


class Game:

    """La classe Game est la classe qui va gérer tout le jeu, du menu au gameplay en passant
    par le map editor/loader, la fonction main_loop() est le corps du jeu."""

    def __init__(self, screen):

        # variables de bases définissant les stade du jeu
        self.screen = screen
        self.game = True
        self.fighting = False
        self.menu = True
        self.running = False
        self.end_screen = False
        self.map_editor = False
        self.map_loader = False
        self.inside_house = False
        self.inside_house2 = False
        self.blocking = False
        self.blocking2 = False
        self.hit = False
        self.hit2 = False
        self.winner = None

        # crée les maps, sous formes de listes de listes contenant pour chaque chiffre une information sur le bloc,
        # il y a différentes listes pour représenter différentes "couches", d'abord le sol, puis les objets decoratifs
        self.map_ground_default = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 4, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # pour rendre le mouvement plus fluide, la classe du joueur est deux fois plus importantes que celle de
        # l'environnement, pour que le joueur se déplace de demi-cases mais que l'environnement soit constitué de
        # cases à part entière
        self.map_player_default = [
         [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0],
         [0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
         [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
         [0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.map_others_default = [[0, 1, 0, 3, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [2, 2, 1, 0, 0, 3, 2, 0, 0, 0, 0, 0, 2, 0, 0, 3, 0, 0, 0, 0],
                                   [0, 3, 2, 0, 0, 0, 0, 6, 0, 2, 3, 0, 0, 2, 0, 0, 0, 0, 2, 0],
                                   [0, 0, 0, 5, 0, 2, 2, 0, 0, 0, 0, 0, 0, 6, 0, 2, 0, 2, 0, 0],
                                   [0, 4, 0, 0, 0, 4, 0, 2, 0, 2, 0, 0, 0, 1, 0, 0, 2, 2, 6, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0],
                                   [0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 3, 0, 2, 0],
                                   [0, 0, 0, 0, 0, 0, 2, 0, 0, 3, 0, 0, 6, 0, 2, 0, 0, 0, 0, 0],
                                   [0, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0],
                                   [0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # initialise les variables relatives au joueur ; sa direction de départ, ses statuts ainsi que sa classe
        self.pl = Player.Player(self.screen, self.map_player_default)
        self.pl2 = Player2.Player(self.screen, self.map_player_default)
        self.direction = "right"
        self.direction2 = "right"
        self.moving = [False, False, False, False]
        self.moving2 = [False, False, False, False]
        self.attacking = False
        self.attacking2 = False
        self.score1 = 0
        self.score2 = 0

        # crée un dictionnaire de touches préssées ou non
        self.pressed = {}
        # initialise les variables de temps
        self.clock = pygame.time.Clock()
        self.current_time = pygame.time.get_ticks()
        self.delay_movement = pygame.time.get_ticks()
        self.delay_movement2 = pygame.time.get_ticks()

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
        self.add_stairs1 = lambda x, y: self.decorative_group_others.add(Dc.CaveStair((x, y)))
        self.add_stairs2 = lambda x, y: self.decorative_group_others.add(Dc.CaveStair2((x, y)))
        self.add_column = lambda x, y: self.decorative_group_others.add(Dc.Column((x, y)))
        self.add_skull = lambda x, y: self.decorative_group_others.add(Dc.Skull((x, y)))

        self.ground_group = pygame.sprite.Group()
        self.add_grass = lambda x, y: self.ground_group.add(Gr.Grass((x, y)))
        self.add_basic_road = lambda x, y: self.ground_group.add(Gr.BasicRoad((x, y)))
        self.add_road_left = lambda x, y: self.ground_group.add(Gr.RoadLeft((x, y)))
        self.add_road_right = lambda x, y: self.ground_group.add(Gr.RoadRight((x, y)))
        self.add_road_bot = lambda x, y: self.ground_group.add(Gr.RoadBot((x, y)))
        self.add_road_top = lambda x, y: self.ground_group.add(Gr.RoadTop((x, y)))
        self.add_road_top_left_corner_full = lambda x, y: self.ground_group.add(Gr.RoadTopLeftFull((x, y)))
        self.add_road_bot_left_corner_empty = lambda x, y: self.ground_group.add(Gr.RoadBotRightEmpty((x, y)))
        self.add_road_bot_right_corner_full = lambda x, y: self.ground_group.add(Gr.RoadBotRightFull((x, y)))
        self.add_road_top_right_corner_full = lambda x, y: self.ground_group.add(Gr.RoadTopRightFull((x, y)))
        self.add_road_bot_left_corner_full = lambda x, y: self.ground_group.add(Gr.RoadBotLeftFull((x, y)))
        self.add_road_top_left_corner_empty = lambda x, y: self.ground_group.add(Gr.RoadTopLeftEmpty((x, y)))
        self.add_road_top_right_corner_empty = lambda x, y: self.ground_group.add(Gr.RoadTopRightEmpty((x, y)))
        self.add_road_bot_right_corner_empty = lambda x, y: self.ground_group.add(Gr.RoadBotRightEmpty((x, y)))
        self.add_ground_inside_wall = lambda x, y: self.ground_group.add(Gr.InsideWall((x, y)))
        self.add_ground_inside_ground = lambda x, y: self.ground_group.add(Gr.InsideGround((x, y)))

        self.inside_house_group_decorative = pygame.sprite.Group()
        self.add_stairs = lambda x, y: self.inside_house_group_decorative.add(Dc.CaveStair((x, y)))
        self.add_second_stairs = lambda x, y: self.inside_house_group_decorative.add(Dc.CaveStair2((x, y)))
        self.add_column = lambda x, y: self.inside_house_group_decorative.add(Dc.Column((x, y)))
        self.add_skull = lambda x, y: self.inside_house_group_decorative.add(Dc.Skull((x, y)))

        self.inside_house_group_ground = pygame.sprite.Group()
        self.add_ground = lambda x, y: self.inside_house_group_ground.add(Gr.InsideGround((x, y)))
        self.add_wall = lambda x, y: self.inside_house_group_ground.add(Gr.InsideWall((x, y)))

        # seconde map (intérieur maison)

        self.inside_house_map_ground_n_walls = [[1, 1, 1, 1, 1, 1, 1, 1],
                                                [0, 0, 0, 0, 0, 0, 0, 0],
                                                [0, 0, 0, 0, 0, 0, 0, 0],
                                                [0, 0, 0, 0, 0, 0, 0, 0],
                                                [0, 0, 0, 0, 0, 0, 0, 0],
                                                [0, 0, 0, 0, 0, 0, 0, 0]]

        self.inside_house_map_decorative = [[3, 0, 0, 0, 0, 0, 0, 3],
                                            [0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 1, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0],
                                            [4, 0, 0, 0, 0, 0, 0, 0]]

        self.inside_house_map_player = [[3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
                                        [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.flou = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        self.flou.fill((255, 255, 255))
        self.flou.set_alpha(200)

        self.W = self.screen.get_width()
        self.H = self.screen.get_height()

        # menu
        self.button_list = [text.CreateText("Play", 75, (self.W // 2, self.H // 2 - 150)),
                            text.CreateText("Map Editor", 75, (self.W // 2, self.H // 2 - 50)),
                            text.CreateText("Load Map", 75, (self.W // 2, self.H // 2 + 50)),
                            text.CreateText("Quit", 75, (self.W // 2, self.H // 2 + 150))]
        self.actual_selection = 0

        # map editor
        self.MapEditor = Me.MainDisplay(self.screen)
        self.group_pop_up_saving = pygame.sprite.Group()
        self.add_pop_up_saving = lambda: self.group_pop_up_saving.add(text.SavingAnim((25, 25)))

        # map loader
        self.MapLoader = ml.MainDisplay(self.screen)

        # LOADING MAP
        with open("map storage/actual_map.json") as m:
            self.chosen_map = json.load(m)

        self.chosen_map = self.chosen_map["actual_map"]

        if self.chosen_map != "basic":
            with open("map storage/map.json") as map_:
                self.total_maps = json.load(map_)

            self.total_maps = self.total_maps["all maps"][self.chosen_map]
            self.map_player = self.total_maps["map_collision"]
            self.map_ground = self.total_maps["map_ground"]
            self.map_others = self.total_maps["map_decorative"]
        else:
            self.map_ground = self.map_ground_default
            self.map_player = self.map_player_default
            self.map_others = self.map_others_default

        # réinitialise la classe du joueur pour mettre à jour certains paramètres
        self.pl = Player.Player(self.screen, self.map_player)
        self.pl2 = Player2.Player(self.screen, self.map_player)

        self.sound_dict = Sm.SoundManager()

        self.DisplayAth = D_ath.DisplayAth(self.screen, self.score1, self.score2)

        self.actual_selection_end_screen = 0

    def update_map(self, basic):

        """Cette fonction sert à mettre à jour la map si jamais l'utilisateur a chargé une autre map que celle
        de base, pour ce faire, tous les groupes de sprites (images) sont vidés pour être reremplis avec la nouvelle
        map."""
        self.ground_group.empty()
        self.decorative_group_tree.empty()
        self.decorative_group_others.empty()
        self.house_group.empty()

        if basic == "basic":
            with open("map storage/actual_map.json") as actual_map:
                current_map = json.load(actual_map)

            current_map["actual_map"] = "basic"

            with open("map storage/actual_map.json", "w") as actual_map:
                json.dump(current_map, actual_map, indent=2)

        # LOADING MAP
        with open("map storage/actual_map.json") as m:
            self.chosen_map = json.load(m)

        self.chosen_map = self.chosen_map["actual_map"]

        if self.chosen_map != "basic":
            with open("map storage/map.json") as map_:
                self.total_maps = json.load(map_)

            self.total_maps = self.total_maps["all maps"][self.chosen_map]
            self.map_ground = self.total_maps["map_ground"]
            self.map_player = self.total_maps["map_collision"]
            self.map_others = self.total_maps["map_decorative"]

            self.show_map()
            self.show_decorative()
        else:
            self.map_ground = self.map_ground_default
            self.map_player = self.map_player_default
            self.map_others = self.map_others_default

            self.show_map()
            self.show_decorative()

        self.pl = Player.Player(self.screen, self.map_player)
        self.pl2 = Player2.Player(self.screen, self.map_player)

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
                elif self.map_ground[row][cell] == 10:
                    self.add_road_bot_left_corner_full(cell * 100, row * 100)
                elif self.map_ground[row][cell] == 11:
                    self.add_road_bot_right_corner_empty(cell * 100, row * 100)
                elif self.map_ground[row][cell] == 12:
                    self.add_road_top_right_corner_empty(cell * 100, row * 100)
                elif self.map_ground[row][cell] == 13:
                    self.add_road_top_left_corner_empty(cell * 100, row * 100)
                elif self.map_ground[row][cell] == 14:
                    self.add_basic_road(cell * 100, row * 100)
                elif self.map_ground[row][cell] == 16:
                    self.add_ground_inside_wall(cell * 100, row * 100)
                elif self.map_ground[row][cell] == 15:
                    self.add_ground_inside_ground(cell * 100, row * 100)

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
                elif self.map_others[row][cell] == 8:
                    self.add_stairs1(cell * 100, row * 100)
                elif self.map_others[row][cell] == 9:
                    self.add_stairs2(cell * 100, row * 100)
                elif self.map_others[row][cell] == 10:
                    self.add_column(cell * 100, row * 100)
                elif self.map_others[row][cell] == 11:
                    self.add_skull(cell * 100, row * 100)
                else:
                    pass

    def show_inside_house(self):

        for row in range(len(self.inside_house_map_decorative)):
            for cell in range(len(self.inside_house_map_decorative[row])):
                if self.inside_house_map_decorative[row][cell] == 2:
                    self.add_stairs(cell*100+250, row*100+250)
                elif self.inside_house_map_decorative[row][cell] == 1:
                    self.add_second_stairs(cell*100+250, row*100+250)
                elif self.inside_house_map_decorative[row][cell] == 3:
                    self.add_column(cell*100+250, row*100+150)
                elif self.inside_house_map_decorative[row][cell] == 4:
                    self.add_skull(cell*100+250+20, row*100+150+20)

        for row in range(len(self.inside_house_map_ground_n_walls)):
            for cell in range(len(self.inside_house_map_ground_n_walls[row])):
                if self.inside_house_map_ground_n_walls[row][cell] == 0:
                    self.add_ground(cell*100+250, row*100+150)
                elif self.inside_house_map_ground_n_walls[row][cell] == 1:
                    self.add_wall(cell*100+250, row*100+150)

    def find_last(self, group):
        last = None
        for sprites in group:

            last = sprites
        return last

    def find_first(self, group):
        for sprites in group:
            return sprites

    def reset_game(self):
        self.pl = Player.Player(self.screen, self.map_player_default)
        self.pl2 = Player2.Player(self.screen, self.map_player_default)
        self.DisplayAth = D_ath.DisplayAth(self.screen, self.score1, self.score2)
        self.fighting = False

    def reset_entirely(self):
        self.score1 = 0
        self.score2 = 0
        self.pl = Player.Player(self.screen, self.map_player_default)
        self.pl2 = Player2.Player(self.screen, self.map_player_default)
        self.DisplayAth = D_ath.DisplayAth(self.screen, self.score1, self.score2)
        self.fighting = False

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

        self.show_inside_house()

        while self.game:

            while self.menu:

                if ml.update_map:
                    self.update_map("else")
                    ml.update_map = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.menu = False
                        self.game = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP and self.actual_selection > 0:
                            self.actual_selection -= 1
                        if event.key == pygame.K_DOWN and self.actual_selection < 3:
                            self.actual_selection += 1
                        if event.key == 13:
                            if self.actual_selection == 0:
                                self.menu = False
                                self.running = True
                                self.DisplayAth = D_ath.DisplayAth(self.screen, self.score1, self.score2)
                                self.reset_entirely()
                            elif self.actual_selection == 1:
                                self.menu = False
                                self.map_editor = True
                                self.MapEditor.update_edit()
                            elif self.actual_selection == 2:
                                self.menu = False
                                self.map_loader = True
                                # met a jour les maps disponibles
                                self.MapLoader = ml.MainDisplay(self.screen)
                            elif self.actual_selection == 3:
                                self.menu = False
                                self.game = False
                                close_map_editor()

                self.ground_group.draw(self.screen)
                self.decorative_group_others.draw(self.screen)
                self.house_group.draw(self.screen)
                self.decorative_group_tree.draw(self.screen)
                self.screen.blit(self.flou, (0, 0))

                rect_choice = pygame.Rect(100, 100, 350, 70)
                rect_choice.center = self.button_list[self.actual_selection].rect.center
                pygame.draw.rect(self.screen, (255, 0, 0), rect_choice)

                for i in self.button_list:
                    self.screen.blit(i.text, i.rect)

                pygame.mouse.set_visible(False)
                pygame.display.flip()

            while self.map_editor:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game = False
                        self.map_editor = False
                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_ESCAPE:
                            self.map_editor = False
                            self.menu = True
                        if self.MapEditor.big_tab == "build":
                            if event.key == pygame.K_LEFT and self.MapEditor.mb.actual_selection > 0:
                                self.MapEditor.mb.actual_selection -= 1
                            if event.key == pygame.K_RIGHT and self.MapEditor.mb.onglet == "grass" and\
                                    self.MapEditor.mb.actual_selection < 0:
                                self.MapEditor.mb.actual_selection += 1
                            if event.key == pygame.K_RIGHT and self.MapEditor.mb.onglet == "road" and\
                                    self.MapEditor.mb.actual_selection < 12:
                                self.MapEditor.mb.actual_selection += 1
                            if event.key == pygame.K_RIGHT and self.MapEditor.mb.onglet == "inside" and\
                                    self.MapEditor.mb.actual_selection < 1:
                                self.MapEditor.mb.actual_selection += 1
                            if event.key == pygame.K_DOWN and self.MapEditor.mb.onglet != "inside":
                                self.MapEditor.mb.onglet = \
                                    self.MapEditor.mb.all_onglets[self.MapEditor.mb.all_onglets.index(self.MapEditor.mb.onglet)+1]
                                self.MapEditor.mb.actual_selection = 0
                            if event.key == pygame.K_UP and self.MapEditor.mb.onglet != "grass":
                                self.MapEditor.mb.onglet = \
                                    self.MapEditor.mb.all_onglets[self.MapEditor.mb.all_onglets.index(self.MapEditor.mb.onglet)-1]
                                self.MapEditor.mb.actual_selection = 0
                        elif self.MapEditor.big_tab == "decorative":
                            if event.key == pygame.K_LEFT and self.MapEditor.mbd.current_selection > 0:
                                self.MapEditor.mbd.current_selection -= 1
                            if event.key == pygame.K_RIGHT and self.MapEditor.mbd.current_selection < 11:
                                self.MapEditor.mbd.current_selection += 1
                        if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                            self.add_pop_up_saving()
                            self.MapEditor.show_bar = False
                            self.MapEditor.main_display()
                            self.MapEditor.save_map()
                            self.MapEditor.show_bar = True
                        if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                            self.MapEditor.cancel()

                        if event.key == pygame.K_b and self.MapEditor.big_tab != "build":
                            self.MapEditor.big_tab = "build"
                        if event.key == pygame.K_d and self.MapEditor.big_tab != "decorative":
                            self.MapEditor.big_tab = "decorative"
                        if event.key == pygame.K_c and self.MapEditor.big_tab != "collision":
                            self.MapEditor.big_tab = "collision"

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            # transforme le tuple en liste pour pouvoir le modifier
                            self.MapEditor.click([event.pos[0], event.pos[1]])

                self.screen.fill((0, 0, 0))

                self.MapEditor.main_display()
                self.group_pop_up_saving.draw(self.screen)
                self.group_pop_up_saving.update()

                pygame.mouse.set_visible(True)
                pygame.display.flip()

            while self.map_loader:

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        self.map_loader = False
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.map_loader = False
                            self.menu = True

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 4:
                            try:
                                if self.find_first(self.MapLoader.maps_group).rect.y < 25:
                                    self.MapLoader.maps_group.update("down", False, pygame.mouse.get_pos())
                            except AttributeError:
                                pass
                        if event.button == 5:
                            try:
                                if self.find_last(self.MapLoader.maps_group).rect.y > self.H - 300:
                                    self.MapLoader.maps_group.update("up", False, pygame.mouse.get_pos())
                            except AttributeError:
                                pass
                        if event.button == 1:
                            self.MapLoader.maps_group.update(None, True, pygame.mouse.get_pos())
                            if self.MapLoader.button_restore_default_surf_rect.collidepoint(event.pos):
                                self.update_map("basic")

                self.MapLoader.maps_group.update(None, False, pygame.mouse.get_pos())
                self.MapLoader.display()
                pygame.mouse.set_visible(True)
                pygame.display.flip()

            while self.running:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        self.game = False
                    if event.type == pygame.KEYDOWN:
                        self.pressed[event.key] = True
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
                            self.menu = True

                        if event.key == pygame.K_z:
                            self.moving[0] = True
                        if event.key == pygame.K_s:
                            self.moving[1] = True
                        if event.key == pygame.K_d:
                            self.moving[2] = True
                        if event.key == pygame.K_q:
                            self.moving[3] = True

                        if event.key == pygame.K_UP:
                            self.moving2[0] = True
                        if event.key == pygame.K_DOWN:
                            self.moving2[1] = True
                        if event.key == pygame.K_LEFT:
                            self.moving2[2] = True
                        if event.key == pygame.K_RIGHT:
                            self.moving2[3] = True

                        if event.key == pygame.K_e and not self.attacking:
                            self.attacking = True
                        if event.key == pygame.K_RCTRL and not self.attacking2:
                            self.attacking2 = True

                    if event.type == pygame.KEYUP:
                        self.pressed[event.key] = False

                        if event.key == pygame.K_z:
                            self.moving[0] = False
                        if event.key == pygame.K_s:
                            self.moving[1] = False
                        if event.key == pygame.K_d:
                            self.moving[2] = False
                        if event.key == pygame.K_q:
                            self.moving[3] = False

                        if event.key == pygame.K_UP:
                            self.moving2[0] = False
                        if event.key == pygame.K_DOWN:
                            self.moving2[1] = False
                        if event.key == pygame.K_LEFT:
                            self.moving2[2] = False
                        if event.key == pygame.K_RIGHT:
                            self.moving2[3] = False

                # limite le mouvement du joueur à 1 toutes les 50 ms
                if self.current_time - self.delay_movement > 50 and self.fighting:
                    # reset le délai
                    self.delay_movement = self.current_time
                    # si le joueur n'est pas en train d'attaquer, le fait bouger
                    if not self.attacking:
                        if not self.blocking:
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
                        if self.pressed.get(pygame.K_a):
                            self.blocking = True
                        else:
                            self.blocking = False

                if self.current_time - self.delay_movement2 > 50 and self.fighting:
                    # reset le délai
                    self.delay_movement2 = self.current_time
                    # si le joueur n'est pas en train d'attaquer, le fait bouger
                    if not self.attacking2:
                        if not self.blocking2:
                            if self.pressed.get(pygame.K_UP):
                                self.pl2.move("up", self.inside_house_map_player, self.inside_house)
                                self.direction2 = "back"
                            if self.pressed.get(pygame.K_DOWN):
                                self.pl2.move("down", self.inside_house_map_player, self.inside_house)
                                self.direction2 = "front"
                            if self.pressed.get(pygame.K_LEFT):
                                self.pl2.move("left", self.inside_house_map_player, self.inside_house)
                                self.direction2 = "left"
                            if self.pressed.get(pygame.K_RIGHT):
                                self.pl2.move("right", self.inside_house_map_player, self.inside_house)
                                self.direction2 = "right"
                        if self.pressed.get(pygame.K_KP0):
                            self.blocking2 = True
                        else:
                            self.blocking2 = False

                # dessine/met à jour tous les composants du jeu (sol, joueur, décoration...)
                self.ground_group.draw(self.screen)
                self.decorative_group_others.draw(self.screen)

                self.pl.update(self.inside_house)
                self.pl.move_animation(self.direction, self.moving, self.blocking)
                self.pl2.update(self.inside_house)
                self.pl2.move_animation(self.direction2, self.moving2, self.blocking2)
                if 10 > self.pl.current_pos[0] > 5:
                    if self.pl.current_pos[1] <= 10 and self.pl2.current_pos[1] <= 10:
                        self.house_group.draw(self.screen)
                    elif self.pl.current_pos[1] <= 10 and self.pl2.current_pos[1] >= 10:
                        self.house_group.draw(self.screen)
                        self.pl2.update(self.inside_house)
                    elif self.pl.current_pos[1] >= 11 and self.pl2.current_pos[1] <= 11:
                        self.house_group.draw(self.screen)
                        self.pl.update(self.inside_house)
                    else:
                        self.house_group.draw(self.screen)
                        self.pl.update(self.inside_house)
                        self.pl2.update(self.inside_house)
                else:
                    self.house_group.draw(self.screen)
                self.decorative_group_tree.draw(self.screen)
                # anime le joueur si il est en train d'attaquer
                if self.attacking:
                    self.pl.attack(self.direction)

                    # crée un effet butoir sur le bouclier adverse
                    if self.pl.rect.colliderect(self.pl2.rect) and self.blocking2:
                        self.attacking = False
                        self.hit = False
                        self.pl.index_animation_att = 0
                        self.sound_dict.shield_hit()

                    if self.pl.rect.colliderect(self.pl2.rect) and not self.blocking2 and not self.hit:
                        self.hit = True
                        self.pl2.life -= 10
                        self.sound_dict.slice()
                    if self.pl.attack(self.direction) == "end":
                        if not self.hit:
                            self.sound_dict.swoosh()
                        self.hit = False
                        self.attacking = False
                        self.pl.index_animation_att = 0

                if self.attacking2:
                    self.pl2.attack(self.direction2)
                    # crée un effet butoir sur le bouclier adverse
                    if self.pl.rect.colliderect(self.pl2.rect) and self.blocking:
                        self.attacking2 = False
                        self.hit2 = False
                        self.pl2.index_animation_att = 0
                        self.sound_dict.shield_hit()

                    if self.pl.rect.colliderect(self.pl2.rect) and not self.blocking and not self.hit2:
                        self.hit2 = True
                        self.pl.life -= 10
                        self.sound_dict.slice()
                    if self.pl2.attack(self.direction2) == "end":
                        if not self.hit2:
                            self.sound_dict.swoosh()
                        self.hit2 = False
                        self.attacking2 = False
                        self.pl2.index_animation_att = 0

                if self.map_player[self.pl.current_pos[1]][self.pl.current_pos[0]] == 8 and not self.inside_house:
                    self.inside_house = False
                    self.direction = "right"

                if self.map_player[self.pl2.current_pos[1]][self.pl2.current_pos[0]] == 8 and not self.inside_house2:
                    self.inside_house2 = False
                    self.direction2 = "right"

                # feature d'entrée dans la maison, fonctionnelle mais abandonnée
                """if self.inside_house:
                    self.screen.blit(self.flou, (0, 0))
                    self.inside_house_group_ground.draw(self.screen)
                    self.inside_house_group_decorative.draw(self.screen)
                    self.pl.update(self.inside_house)
                    index = [0, 0]
                    if self.pl.inside_pos[0] - 1 < 0:
                        index[0] = 0
                    else:
                        index[0] = self.pl.inside_pos[0] - 1
                    if self.pl.inside_pos[1] - 1 < 0:
                        index[1] = 0
                    else:
                        index[1] = self.pl.inside_pos[1] - 1

                    if self.inside_house_map_player[index[1]][index[0]] == 9:
                        self.inside_house = False
                        self.pl.current_pos = [30, 2]
                        self.pl.inside_pos = [8, 8]

                if self.inside_house2:
                    self.screen.blit(self.flou, (0, 0))
                    self.inside_house_group_ground.draw(self.screen)
                    self.inside_house_group_decorative.draw(self.screen)
                    self.pl.update(self.inside_house)
                    index = [0, 0]
                    if self.pl2.inside_pos[0] - 1 < 0:
                        index[0] = 0
                    else:
                        index[0] = self.pl.inside_pos[0] - 1
                    if self.pl2.inside_pos[1] - 1 < 0:
                        index[1] = 0
                    else:
                        index[1] = self.pl2.inside_pos[1] - 1

                    if self.inside_house_map_player[index[1]][index[0]] == 9:
                        self.inside_house2 = False
                        self.pl2.current_pos = [30, 2]
                        self.pl2.inside_pos = [8, 8]"""
                self.pl.life_bar()
                self.pl2.life_bar()
                self.DisplayAth.main_display()
                if self.DisplayAth.main_display() == "FIGHT":
                    self.fighting = True

                # condition de victoire :
                if self.pl.life == 0:
                    self.score2 += 1
                    self.reset_game()
                elif self.pl2.life == 0:
                    self.score1 += 1
                    self.reset_game()

                if self.score1 == 3:
                    self.winner = 1
                    self.running = False
                    self.end_screen = True
                elif self.score2 == 3:
                    self.winner = 2
                    self.running = False
                    self.end_screen = True

                pygame.mouse.set_visible(False)  # rends invisible la souris
                self.current_time = pygame.time.get_ticks()  # met à jour le temps
                pygame.display.flip()  # met à jour l'écran
                self.clock.tick(60)  # met les FPS à 60

            while self.end_screen:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game = False
                        self.end_screen = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT and self.actual_selection_end_screen == 1:
                            self.actual_selection_end_screen = 0
                        if event.key == pygame.K_RIGHT and self.actual_selection_end_screen == 0:
                            self.actual_selection_end_screen = 1
                        if event.key == 13:
                            if self.actual_selection_end_screen == 0:
                                self.reset_entirely()
                                self.end_screen = False
                                self.running = True
                            else:
                                self.menu = True
                                self.end_screen = False
                            self.winner = None

                self.ground_group.draw(self.screen)
                self.decorative_group_others.draw(self.screen)
                self.decorative_group_tree.draw(self.screen)
                self.house_group.draw(self.screen)
                self.DisplayAth.display_end_screen(self.actual_selection_end_screen, self.winner)
                pygame.display.flip()


def close_map_editor():
    with open("map storage/actual_map.json") as actual_map:
        current_map = json.load(actual_map)

    current_map["actual_map_editing"] = "None"

    with open("map storage/actual_map.json", "w") as actual_map:
        json.dump(current_map, actual_map, indent=2)


# si raspberry => pygame.display.set_mode((1900, 1000))
# si windows => pygame.display.set_mode((0, 0), pygame.FULLSCREEN
# si mac => qui a un mac ?

# trouve l'OS de l'ordinateur, puis change la taille de l'écran en fonction
if platform == "win32":
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((1900, 1000))
pygame.init()
pygame.mixer.init()

game = Game(screen)
game.main_loop()

pygame.mixer.quit()
pygame.quit()
