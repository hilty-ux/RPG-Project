import pygame
import math
import json
import pyautogui

import Decoration_Classes as Dc
import Ground_Classes as Gr


class MainDisplay:

    def __init__(self, screen):
        self.screen = screen
        self.W = self.screen.get_width()
        self.H = self.screen.get_height()

        self.stage = "build"  # "decorate" ou "collision maker" (event => bonus)

        self.mb = MenuBar(self.screen)
        self.mbd = MenuBarDecorative(self.screen)
        self.mbc = MenuBarCollision(self.screen)

        self.ground_group = pygame.sprite.Group()

        self.show_bar = True

        self.add_grass = lambda x, y: self.ground_group.add(Gr.Grass((x, y)))
        self.add_basic_road = lambda x, y: self.ground_group.add(Gr.BasicRoad((x, y)))
        self.add_road_left = lambda x, y: self.ground_group.add(Gr.RoadLeft((x, y)))
        self.add_road_right = lambda x, y: self.ground_group.add(Gr.RoadRight((x, y)))
        self.add_road_bot = lambda x, y: self.ground_group.add(Gr.RoadBot((x, y)))
        self.add_road_top = lambda x, y: self.ground_group.add(Gr.RoadTop((x, y)))
        self.add_road_top_left_corner_full = lambda x, y: self.ground_group.add(Gr.RoadTopLeftFull((x, y)))
        self.add_road_bot_left_corner_empty = lambda x, y: self.ground_group.add(Gr.RoadBotLeftEmpty((x, y)))
        self.add_road_bot_right_corner_full = lambda x, y: self.ground_group.add(Gr.RoadBotRightFull((x, y)))
        self.add_road_top_right_corner_full = lambda x, y: self.ground_group.add(Gr.RoadTopRightFull((x, y)))
        self.add_road_bot_right_corner_empty = lambda x, y: self.ground_group.add(Gr.RoadBotRightEmpty((x, y)))
        self.add_inside_wall = lambda x, y: self.ground_group.add(Gr.InsideWall((x, y)))
        self.add_inside_ground = lambda x, y: self.ground_group.add(Gr.InsideGround((x, y)))
        self.add_road_bot_left_corner_full = lambda x, y: self.ground_group.add(Gr.RoadBotLeftFull((x, y)))
        self.add_road_top_right_corner_empty = lambda x, y: self.ground_group.add(Gr.RoadTopRightEmpty((x, y)))
        self.add_road_top_left_corner_empty = lambda x, y: self.ground_group.add(Gr.RoadTopLeftEmpty((x, y)))

        self.selection_grass = [self.add_grass]
        self.selection_road = [self.add_basic_road, self.add_road_left, self.add_road_right, self.add_road_top,
                               self.add_road_bot, self.add_road_top_left_corner_full,
                               self.add_road_top_right_corner_full, self.add_road_bot_left_corner_full,
                               self.add_road_bot_right_corner_full, self.add_road_top_left_corner_empty,
                               self.add_road_top_right_corner_empty, self.add_road_bot_right_corner_empty,
                               self.add_road_bot_left_corner_empty]
        self.selection_inside = [self.add_inside_ground, self.add_inside_wall]

        self.map_ground_empty = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.map_decorative_empty = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.collision_map = [
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.trad_selection_grass = [0]
        self.trad_selection_road = [14, 1, 2, 6, 7, 4, 8, 10, 9, 13, 12, 11, 5]
        self.trad_selection_inside = [15, 16]

        with open("map storage/map.json") as m:
            self.all_maps = json.load(m)

        with open("map storage/actual_map.json") as actual_map:
            self.current_map = json.load(actual_map)

        self.big_tab = "build"

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

        self.decorative_selection = [self.add_blue_tree, self.add_red_tree, self.add_fern,
                                     self.add_lake, self.add_house, self.add_rock,
                                     self.add_barrier, self.add_stairs1, self.add_stairs2,
                                     self.add_column, self.add_skull]

        self.trad_selection_decorative = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11]

        self.collision_group = pygame.sprite.Group()
        self.add_collision_model = lambda x, y: self.collision_group.add(Gr.CollisionModel((x, y)))

        if self.current_map["actual_map_editing"] != "None":
            self.map_to_edit = self.current_map["actual_map_editing"]
            self.load_map_for_edit()

    def update_edit(self):
        with open("map storage/actual_map.json") as actual_map:
            self.current_map = json.load(actual_map)

        if self.current_map["actual_map_editing"] != "None":
            self.map_to_edit = self.current_map["actual_map_editing"]
            self.load_map_for_edit()

    def load_map_for_edit(self):
        current_map_to_edit = self.all_maps["all maps"][self.map_to_edit]
        self.map_ground_empty = current_map_to_edit["map_ground"]
        self.map_decorative_empty = current_map_to_edit["map_decorative"]
        self.collision_map = current_map_to_edit["map_collision"]

        for row in range(len(self.map_ground_empty)):
            for cell in range(len(self.map_ground_empty[row])):
                if self.map_ground_empty[row][cell] == 0:
                    self.add_grass(cell * 100, row * 100)
                elif self.map_ground_empty[row][cell] == 1:
                    self.add_road_left(cell * 100, row * 100)
                elif self.map_ground_empty[row][cell] == 2:
                    self.add_road_right(cell * 100, row * 100)
                elif self.map_ground_empty[row][cell] == 4:
                    self.add_road_top_left_corner_full(cell * 100, row * 100)
                elif self.map_ground_empty[row][cell] == 5:
                    self.add_road_bot_left_corner_empty(cell * 100, row * 100)
                elif self.map_ground_empty[row][cell] == 6:
                    self.add_road_top(cell * 100, row * 100)
                elif self.map_ground_empty[row][cell] == 7:
                    self.add_road_bot(cell * 100, row * 100)
                elif self.map_ground_empty[row][cell] == 8:
                    self.add_road_top_right_corner_full(cell * 100, row * 100)
                elif self.map_ground_empty[row][cell] == 9:
                    self.add_road_bot_right_corner_full(cell * 100, row * 100)
                elif self.map_ground_empty[row][cell] == 10:
                    self.add_road_bot_left_corner_full(cell * 100, row * 100)
                elif self.map_ground_empty[row][cell] == 11:
                    self.add_road_bot_right_corner_empty(cell * 100, row * 100)
                elif self.map_ground_empty[row][cell] == 12:
                    self.add_road_top_right_corner_empty(cell * 100, row * 100)
                elif self.map_ground_empty[row][cell] == 13:
                    self.add_road_top_left_corner_empty(cell * 100, row * 100)
                elif self.map_ground_empty[row][cell] == 14:
                    self.add_basic_road(cell * 100, row * 100)
                elif self.map_ground_empty[row][cell] == 16:
                    self.add_inside_wall(cell * 100, row * 100)
                elif self.map_ground_empty[row][cell] == 15:
                    self.add_inside_ground(cell * 100, row * 100)

        for row in range(len(self.map_decorative_empty)):
            for cell in range(len(self.map_decorative_empty[row])):
                if self.map_decorative_empty[row][cell] == 1:
                    self.add_blue_tree(cell * 100, row * 100)
                elif self.map_decorative_empty[row][cell] == 2:
                    self.add_fern(cell * 100, row * 100)
                elif self.map_decorative_empty[row][cell] == 3:
                    self.add_red_tree(cell * 100, row * 100)
                elif self.map_decorative_empty[row][cell] == 4:
                    self.add_lake(cell * 100, row * 100)
                elif self.map_decorative_empty[row][cell] == 5:
                    self.add_house(cell * 100, row * 100)
                elif self.map_decorative_empty[row][cell] == 6:
                    self.add_rock(cell * 100, row * 100)
                elif self.map_decorative_empty[row][cell] == 7:
                    self.add_barrier(cell * 100, row * 100)
                elif self.map_decorative_empty[row][cell] == 8:
                    self.add_stairs1(cell * 100, row * 100)
                elif self.map_decorative_empty[row][cell] == 9:
                    self.add_stairs2(cell * 100, row * 100)
                elif self.map_decorative_empty[row][cell] == 10:
                    self.add_column(cell * 100, row * 100)
                elif self.map_decorative_empty[row][cell] == 11:
                    self.add_skull(cell * 100, row * 100)
                else:
                    pass

        for row in range(len(self.collision_map)):
            for cell in range(len(self.collision_map[row])):
                if self.collision_map[row][cell] == 3:
                    self.add_collision_model(cell*50, row*50)

    def click(self, pos):
        # arrondi la position à la centaine du dessous
        pos_coll = [0, 0]
        pos_coll[0] = math.floor(pygame.mouse.get_pos()[0] / 50) * 50
        pos_coll[1] = math.floor(pygame.mouse.get_pos()[1] / 50) * 50

        pos[0] = math.floor(pos[0] / 100) * 100
        pos[1] = math.floor(pos[1] / 100) * 100

        if self.big_tab == "build":
            if self.mb.onglet == "grass":
                self.map_ground_empty[math.floor(pos[1] / 100)][math.floor(pos[0] / 100)] = \
                    self.trad_selection_grass[self.mb.actual_selection]
                self.selection_grass[self.mb.actual_selection](pos[0], pos[1])
            elif self.mb.onglet == "road":
                self.map_ground_empty[math.floor(pos[1] / 100)][math.floor(pos[0] / 100)] = \
                    self.trad_selection_road[self.mb.actual_selection]
                self.selection_road[self.mb.actual_selection](pos[0], pos[1])
            elif self.mb.onglet == "inside":
                self.map_ground_empty[math.floor(pos[1] / 100)][math.floor(pos[0] / 100)] = \
                    self.trad_selection_inside[self.mb.actual_selection]
                self.selection_inside[self.mb.actual_selection](pos[0], pos[1])
        elif self.big_tab == "decorative":
            self.map_decorative_empty[math.floor(pos[1] / 100)][math.floor(pos[0] / 100)] = \
                self.trad_selection_decorative[self.mbd.current_selection]
            self.decorative_selection[self.mbd.current_selection](pos[0], pos[1])
        elif self.big_tab == "collision":
            if self.collision_map[math.floor(pos_coll[1] / 50)][math.floor(pos_coll[0] / 50)] == 0:
                self.collision_map[math.floor(pos_coll[1] / 50)][math.floor(pos_coll[0] / 50)] = 3
                self.add_collision_model(pos_coll[0], pos_coll[1])
            else:
                self.collision_map[math.floor(pos_coll[1] / 50)][math.floor(pos_coll[0] / 50)] = 0
                for sprite in self.collision_group:
                    if sprite.rect.collidepoint((pos_coll[0], pos_coll[1])):
                        self.collision_group.remove(sprite)

        print(pygame.mouse.get_pos())
        print(pos_coll)

    def save_map(self):
        with open("map storage/actual_map.json") as map_:
            map_number = json.load(map_)

        preview = pyautogui.screenshot()
        preview.save(r'./map storage/New{}.png'.format(map_number["map_number"] + 1))

        name = "map{}".format(len(self.all_maps["all maps"]) + 1)
        map_package = {"map_ground": self.map_ground_empty,
                       "map_decorative": self.map_decorative_empty,
                       "map_collision": self.collision_map,
                       "path_preview": './map storage/New{}.png'.format(map_number["map_number"] + 1)
                       }

        self.all_maps["all maps"][name] = map_package

        with open("map storage/map.json", "w") as map_storage:
            json.dump(self.all_maps, map_storage)

        map_number["map_number"] += 1
        with open("map storage/actual_map.json", "w") as map_storage:
            json.dump(map_number, map_storage, indent=1)

    def main_display(self):
        if self.show_bar:
            if self.big_tab == "build":
                self.ground_group.draw(self.screen)
                self.decorative_group_others.draw(self.screen)
                self.decorative_group_tree.draw(self.screen)
                self.house_group.draw(self.screen)
                self.mb.display_bar_bot()
            elif self.big_tab == "decorative":
                self.ground_group.draw(self.screen)
                self.decorative_group_others.draw(self.screen)
                self.decorative_group_tree.draw(self.screen)
                self.house_group.draw(self.screen)
                self.mbd.main_display()
            elif self.big_tab == "collision":
                self.ground_group.draw(self.screen)
                self.decorative_group_others.draw(self.screen)
                self.decorative_group_tree.draw(self.screen)
                self.house_group.draw(self.screen)
                self.mbc.main_display()
                self.collision_group.draw(self.screen)


class MenuBarCollision:

    def __init__(self, screen):
        self.screen = screen
        self.W = self.screen.get_width()
        self.H = self.screen.get_height()

        self.bar_bot = pygame.Surface((self.W - 300, 110))
        self.bar_bot.fill((255, 255, 255))
        self.bar_bot.set_alpha(200)

        self.surf_line = pygame.Surface((1920, 1080))
        self.surf_line.set_alpha(50)

        self.police_onglet = pygame.font.Font("assets/Police/advanced_pixel-7.ttf", 40)
        self.big_tabs = [self.police_onglet.render("Build", True, (0, 0, 0)),
                         self.police_onglet.render("Decorate", True, (0, 0, 0)),
                         self.police_onglet.render("Collision", True, (0, 0, 0))]
        for i in range(3):
            self.big_tabs[i] = pygame.transform.rotate(self.big_tabs[i], 90)
        self.big_tabs_rect = [i.get_rect() for i in self.big_tabs]
        for i in range(3):
            self.big_tabs_rect[i].y = 5
            self.big_tabs_rect[i].left = 10 + i * 25
            self.bar_bot.blit(self.big_tabs[i], self.big_tabs_rect[i])

        self.current_selection = 0

    def main_display(self):
        self.screen.blit(self.surf_line, (0, 0))
        for i in range(38):
            pygame.draw.line(self.surf_line, (255, 255, 255), (50 + i * 50, 0), (50 + i * 50, 1080))
        for i in range(22):
            pygame.draw.line(self.surf_line, (255, 255, 255), (0, 50 + i * 50), (1920, 50 + i * 50))

        self.screen.blit(self.bar_bot, (0, self.H - 110))
        pygame.draw.rect(self.bar_bot, (0, 255, 0), [75, 0, 25, 107])
        self.bar_bot.blit(self.big_tabs[2], self.big_tabs_rect[2])


class MenuBarDecorative:

    def __init__(self, screen):

        self.screen = screen
        self.W = self.screen.get_width()
        self.H = self.screen.get_height()

        self.bar_bot = pygame.Surface((self.W - 300, 110))
        self.bar_bot.fill((255, 255, 255))
        self.bar_bot.set_alpha(200)

        self.decoration_group = pygame.sprite.Group()
        self.decoration_group.add(Dc.BlueTree((200, 5)))
        self.decoration_group.add(Dc.RedTree((305, 5)))
        self.decoration_group.add(Dc.Fern((410, 5)))
        self.decoration_group.add(Dc.Lake((515, 5)))
        self.decoration_group.add(Dc.House((620, 5)))
        self.decoration_group.add(Dc.Rock((725, 5)))
        self.decoration_group.add(Dc.Barrier((825, 5)))
        self.decoration_group.add(Dc.CaveStair((930, 5)))
        self.decoration_group.add(Dc.CaveStair2((1040, 5)))
        self.decoration_group.add(Dc.Column((1145, 5)))
        self.decoration_group.add(Dc.Skull((1250, 5)))
        # change la taille pour qu'ils soient assez petits ou assez grands pour etre visibles sur la barre de navigation
        self.decoration_group.update(True)

        self.police_onglet = pygame.font.Font("assets/Police/advanced_pixel-7.ttf", 40)
        self.big_tabs = [self.police_onglet.render("Build", True, (0, 0, 0)),
                         self.police_onglet.render("Decorate", True, (0, 0, 0)),
                         self.police_onglet.render("Collision", True, (0, 0, 0))]
        for i in range(3):
            self.big_tabs[i] = pygame.transform.rotate(self.big_tabs[i], 90)
        self.big_tabs_rect = [i.get_rect() for i in self.big_tabs]
        for i in range(3):
            self.big_tabs_rect[i].y = 5
            self.big_tabs_rect[i].left = 10 + i * 25
            self.bar_bot.blit(self.big_tabs[i], self.big_tabs_rect[i])

        self.current_selection = 0

    def main_display(self):

        self.screen.blit(self.bar_bot, (0, self.H - 110))
        self.decoration_group.draw(self.bar_bot)
        pygame.draw.rect(self.bar_bot, (0, 255, 0), [45, 0, 25, 107])
        pygame.draw.rect(self.screen, (0, 255, 0), [self.current_selection * 105 + 200, self.H - 5, 100, 5])
        self.bar_bot.blit(self.big_tabs[1], self.big_tabs_rect[1])


class MenuBar:

    def __init__(self, screen):
        self.screen = screen
        self.W = self.screen.get_width()
        self.H = self.screen.get_height()

        self.bar_bot = pygame.Surface((self.W - 300, 110))
        self.bar_bot.fill((255, 255, 255))
        self.bar_bot.set_alpha(200)
        self.clone_surf = pygame.Surface((self.W - 300, 110))
        self.clone_surf.fill((255, 255, 255))
        self.clone_surf.set_alpha(200)

        self.bar_position = "bot"
        self.actual_selection = 0

        self.onglet = "road"  # "road", "inside", "water"
        self.all_onglets = ["grass", "road", "inside"]
        self.grass_group = pygame.sprite.Group()
        self.grass_group.add(Gr.Grass((200, 5)))

        self.road_group = pygame.sprite.Group()
        self.road_group.add(Gr.BasicRoad((200, 5)))
        self.road_group.add(Gr.RoadLeft((305, 5)))
        self.road_group.add(Gr.RoadRight((410, 5)))
        self.road_group.add(Gr.RoadTop((515, 5)))
        self.road_group.add(Gr.RoadBot((620, 5)))
        self.road_group.add(Gr.RoadTopLeftFull((725, 5)))
        self.road_group.add(Gr.RoadTopRightFull((830, 5)))
        self.road_group.add(Gr.RoadBotLeftFull((935, 5)))
        self.road_group.add(Gr.RoadBotRightFull((1040, 5)))
        self.road_group.add(Gr.RoadTopLeftEmpty((1145, 5)))
        self.road_group.add(Gr.RoadTopRightEmpty((1250, 5)))
        self.road_group.add(Gr.RoadBotRightEmpty((1355, 5)))
        self.road_group.add(Gr.RoadBotLeftEmpty((1460, 5)))

        self.inside_group = pygame.sprite.Group()
        self.inside_group.add(Gr.InsideGround((200, 5)))
        self.inside_group.add(Gr.InsideWall((305, 5)))

        self.police_onglet = pygame.font.Font("assets/Police/advanced_pixel-7.ttf", 50)
        self.onglet_buttons = [self.police_onglet.render("Grass", True, (0, 0, 0)),
                               self.police_onglet.render("Road", True, (0, 0, 0)),
                               self.police_onglet.render("Others", True, (0, 0, 0))]
        self.onglet_rects = [i.get_rect() for i in self.onglet_buttons]
        self.onglet_surf = [pygame.Surface((95, 30)), pygame.Surface((95, 30)), pygame.Surface((95, 30))]
        self.onglet_surf_rect = [i.get_rect() for i in self.onglet_surf]
        for i in range(3):
            self.onglet_rects[i].center = 150, 20 + i * 35
            self.onglet_surf_rect[i].center = self.onglet_rects[i].center
            self.bar_bot.blit(self.onglet_surf[i], self.onglet_surf_rect[i])
            self.bar_bot.blit(self.onglet_buttons[i], self.onglet_rects[i])

        self.police_onglet = pygame.font.Font("assets/Police/advanced_pixel-7.ttf", 40)
        self.big_tabs = [self.police_onglet.render("Build", True, (0, 0, 0)),
                         self.police_onglet.render("Decorate", True, (0, 0, 0)),
                         self.police_onglet.render("Collision", True, (0, 0, 0))]
        for i in range(3):
            self.big_tabs[i] = pygame.transform.rotate(self.big_tabs[i], 90)
        self.big_tabs_rect = [i.get_rect() for i in self.big_tabs]
        for i in range(3):
            self.big_tabs_rect[i].y = 5
            self.big_tabs_rect[i].left = 10 + i * 25
            self.bar_bot.blit(self.big_tabs[i], self.big_tabs_rect[i])

    def display_bar_bot(self):
        self.screen.blit(self.bar_bot, (0, self.H - 110))
        if self.onglet == "grass":
            self.grass_group.draw(self.bar_bot)
            self.onglet_surf[0].fill((0, 255, 0))
            self.onglet_surf[1].fill((255, 255, 255))
            self.onglet_surf[2].fill((255, 255, 255))
        elif self.onglet == "road":
            self.road_group.draw(self.bar_bot)
            self.onglet_surf[0].fill((255, 255, 255))
            self.onglet_surf[1].fill((0, 255, 0))
            self.onglet_surf[2].fill((255, 255, 255))
        elif self.onglet == "inside":
            self.inside_group.draw(self.bar_bot)
            self.onglet_surf[0].fill((255, 255, 255))
            self.onglet_surf[1].fill((255, 255, 255))
            self.onglet_surf[2].fill((0, 255, 0))
        for i in range(3):
            self.bar_bot.blit(self.onglet_surf[i], self.onglet_surf_rect[i])
            self.bar_bot.blit(self.onglet_buttons[i], self.onglet_rects[i])
        pygame.draw.rect(self.screen, (0, 255, 0), [self.actual_selection * 105 + 200, self.H - 5, 100, 5])
        pygame.draw.rect(self.bar_bot, (0, 255, 0), [18, 0, 25, 65])
        self.bar_bot.blit(self.big_tabs[0], self.big_tabs_rect[0])