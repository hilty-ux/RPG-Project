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

        self.beginning = True

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
