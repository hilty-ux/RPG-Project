import pygame as pg


class DisplayAth:

    def __init__(self, screen, score1, score2):

        self.screen = screen
        self.W = self.screen.get_width()
        self.H = self.screen.get_height()

        self.police_score = pg.font.Font("assets/Police/advanced_pixel-7.ttf", 50)

        self.current_score_p1 = score1
        self.current_score_p2 = score2
        self.score = self.police_score.render(f"{self.current_score_p1} - {self.current_score_p2}", True,
                                              (255, 255, 255))
        self.score_rect = self.score.get_rect()
        self.score_rect.center = self.W // 2, 25

        self.anim = AnimTime(self.screen)
        self.current_time = pg.time.get_ticks()
        self.delay = pg.time.get_ticks()
        self.delay_anim = pg.time.get_ticks()

        self.beginning = True

        self.black_screen_surf = pg.Surface((1920, 1080))
        self.black_screen_surf.fill((0, 0, 0))
        self.black_screen_surf.set_alpha(180)

        self.police_winner = pg.font.Font("assets/Police/advanced_pixel-7.ttf", 135)
        self.winner1 = self.police_winner.render("White player won !", True, (255, 255, 255))
        self.winner1_rect = self.winner1.get_rect()
        self.winner2 = self.police_winner.render("Red player won !", True, (176 , 0, 0))
        self.winner2_rect = self.winner2.get_rect()
        self.winner1_rect.center = self.W // 2 - 300, self.H // 2 - 200
        self.winner2_rect.center = self.W // 2 - 300, self.H // 2 - 200

        self.buttons_police = pg.font.Font("assets/Police/advanced_pixel-7.ttf", 100)
        self.buttons = [self.buttons_police.render("Play again", True, (255, 255, 255)),
                        self.buttons_police.render("Quit", True, (255, 255, 255))]
        self.buttons_rect = [i.get_rect() for i in self.buttons]
        self.buttons_rect[0].right = self.W // 2 - 250
        self.buttons_rect[1].left = self.W // 2 + 250
        self.buttons_rect[0].y = self.H // 2 + 250
        self.buttons_rect[1].y = self.H // 2 + 250

        self.frames_winner1 = [pg.image.load("assets/Player/Waiting/idle left1.png"),
                               pg.image.load("assets/Player/Waiting/idle left2.png"),
                               pg.image.load("assets/Player/Waiting/idle left3.png"),
                               pg.image.load("assets/Player/Waiting/idle left4.png")]
        for i in self.frames_winner1:
            self.frames_winner1[self.frames_winner1.index(i)] = \
                pg.transform.scale(i, (i.get_width()*20, i.get_height()*20))
        self.frames_winner2 = [pg.image.load("assets/Player2/Waiting/idle left1.png"),
                               pg.image.load("assets/Player2/Waiting/idle left2.png"),
                               pg.image.load("assets/Player2/Waiting/idle left3.png"),
                               pg.image.load("assets/Player2/Waiting/idle left4.png")]
        for i in self.frames_winner2:
            self.frames_winner2[self.frames_winner2.index(i)] = \
                pg.transform.scale(i, (i.get_width() * 20, i.get_height() * 20))

        self.index_anim = 0
        self.rect = self.frames_winner1[self.index_anim].get_rect()
        self.rect.center = self.W // 2 + 400, self.H // 2 - 100

    def animation(self, winner):
        self.current_time = pg.time.get_ticks()
        if self.current_time - self.delay_anim > 100:
            if self.index_anim < 3:
                self.index_anim += 1
            else:
                self.index_anim = 0
            self.delay_anim = self.current_time

        if winner == 1:
            self.screen.blit(self.frames_winner1[self.index_anim], self.rect)
        else:
            self.screen.blit(self.frames_winner2[self.index_anim], self.rect)

    def main_display(self):
        self.current_time = pg.time.get_ticks()

        self.screen.blit(self.score, self.score_rect)
        if self.current_time - self.delay > 3500:
            self.beginning = False

        if self.beginning:
            self.anim.display()
            return 0
        else:
            return "FIGHT"

    def display_end_screen(self, selection, winner):
        self.screen.blit(self.black_screen_surf, (0, 0))

        if selection == 0:
            pg.draw.rect(self.screen, (255, 0, 0), [self.W//2-275-self.buttons[0].get_width(), self.H // 2 + 250,
                                                    self.buttons[0].get_width()+50, self.buttons[0].get_height()])
        else:
            pg.draw.rect(self.screen, (255, 0, 0), [self.W//2+225, self.H//2+250,
                                                    self.buttons[1].get_width()+50, self.buttons[1].get_height()])

        if winner == 1:
            self.screen.blit(self.winner1, self.winner1_rect)
        else:
            self.screen.blit(self.winner2, self.winner2_rect)
        self.animation(winner)
        for i in range(2):
            self.screen.blit(self.buttons[i], self.buttons_rect[i])


class AnimTime:

    def __init__(self, screen):
        self.screen = screen
        self.W = self.screen.get_width()
        self.H = self.screen.get_height()

        self.police = pg.font.Font("assets/Police/advanced_pixel-7.ttf", 150)
        self.get_ready_for_battle = self.police.render("Get Ready For Battle !", True, (255, 255, 255))
        self.grfb_rect = self.get_ready_for_battle.get_rect()
        self.grfb_rect.center = self.W // 2, 200

        self.surf = pg.Surface((1920, 1080))
        self.surf.fill((0, 0, 0))
        self.actual_alpha = 222
        self.surf.set_alpha(self.actual_alpha)

        self.current_time = pg.time.get_ticks()
        self.delay = pg.time.get_ticks()
        self.delay_anim = pg.time.get_ticks()

        self.police_numbers = pg.font.Font("assets/Police/advanced_pixel-7.ttf", 450)
        self.numbers = [self.police_numbers.render("0", True, (255, 255, 255)),
                        self.police_numbers.render("1", True, (255, 255, 255)),
                        self.police_numbers.render("2", True, (255, 255, 255)),
                        self.police_numbers.render("3", True, (255, 255, 255))]
        self.numbers_rect = [i.get_rect() for i in self.numbers]
        self.actual_number = 3
        for i in range(4):
            self.numbers_rect[i].center = self.W // 2, self.H // 2

    def smooth(self):
        self.current_time = pg.time.get_ticks()
        if self.current_time - self.delay_anim > 40:
            self.delay_anim = self.current_time
            self.numbers[self.actual_number] = pg.transform.scale(self.numbers[self.actual_number],
                                                                  (round(self.numbers[self.actual_number].get_width() // 1.4),
                                                                   round
                                                                   (self.numbers[
                                                                       self.actual_number].get_height() // 1.4)))
            self.numbers_rect[self.actual_number] = self.numbers[self.actual_number].get_rect()
            self.numbers_rect[self.actual_number].center = self.W // 2, self.H // 2

    def display(self):
        self.current_time = pg.time.get_ticks()
        self.screen.blit(self.surf, (0, 0))
        self.screen.blit(self.get_ready_for_battle, self.grfb_rect)
        self.screen.blit(self.numbers[self.actual_number], self.numbers_rect[self.actual_number])

        if self.current_time - self.delay > 1000:
            self.actual_alpha -= 74
            self.surf.set_alpha(self.actual_alpha)
            self.actual_number -= 1
            self.delay = self.current_time

        self.smooth()
