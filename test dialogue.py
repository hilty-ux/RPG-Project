import pygame


screen = pygame.display.set_mode((1000, 1000))


class Dialog:

    def __init__(self):

        self.police = pygame.font.Font("assets/Police/advanced_pixel-7.ttf", 50)

        self.current_time = pygame.time.get_ticks()
        self.delay = pygame.time.get_ticks()

        self.sound = pygame.mixer.Sound("assets/Sound/writing.wav")
        self.sound.set_volume(0.1)

        self.sentence = "Hello traveller ! What do you want today ?"
        self.index = 0

        self.mc = MultipleChoice()

    def show(self):

        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.delay > 100:
            self.delay = self.current_time
            if self.index < len(self.sentence):
                self.index += 1
                self.sound.play()

        actual_sentence = ""
        for i in range(0, self.index):
            actual_sentence += self.sentence[i]

        sen_to_show = self.police.render(actual_sentence, True, (0, 0, 0))
        sen_to_show_rect = sen_to_show.get_rect()
        sen_to_show_rect.left = 50
        sen_to_show_rect.y = 550

        pygame.draw.rect(screen, (0, 200, 100), [25, 525, 950, 450])
        screen.blit(sen_to_show, sen_to_show_rect)

        if self.index == len(self.sentence):
            self.mc.show()


class MultipleChoice:

    def __init__(self):

        self.police = pygame.font.Font("assets/Police/advanced_pixel-7.ttf", 70)

        self.choice1 = self.police.render("Rice", True, (0, 0, 0))
        self.choice2 = self.police.render("Corn", True, (0, 0, 0))
        self.ch1_rect = self.choice1.get_rect()
        self.ch2_rect = self.choice2.get_rect()
        self.ch1_rect.left = 50
        self.ch1_rect.y = 600
        self.ch2_rect.left = 50
        self.ch2_rect.y = 700

        self.actual_choice = 1
        self.buy_1 = self.police.render("You bought one rice", True, (0, 0, 0))
        self.buy_2 = self.police.render("You bought one corn", True, (0, 0, 0))
        self.chosen = 0

    def show(self):

        if self.chosen == 0:
            if self.actual_choice == 1:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (40, 600, self.choice1.get_width() + 20, self.choice1.get_height() + 10))
            else:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (40, 700, self.choice2.get_width() + 20, self.choice2.get_height() + 10))
            screen.blit(self.choice1, self.ch1_rect)
            screen.blit(self.choice2, self.ch2_rect)
        else:
            if self.chosen == 1:
                rect = self.buy_1.get_rect()
                rect.center = 500, 800
                screen.blit(self.buy_1, rect)
            elif self.chosen == 2:
                rect = self.buy_2.get_rect()
                rect.center = 500, 800
                screen.blit(self.buy_2, rect)

    def switch(self, direction):
        if direction == "down" and self.actual_choice == 1:
            self.actual_choice = 2
        elif direction == "up" and self.actual_choice == 2:
            self.actual_choice = 1

    def confirm(self):
        if self.actual_choice == 1:
            self.chosen = 1
        else:
            self.chosen = 2
        self.actual_choice = 0


pygame.init()
pygame.mixer.init()
dia = Dialog()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            dia.sound.play()
            if event.key == pygame.K_SPACE:
                dia.index = len(dia.sentence)

            if event.key == pygame.K_DOWN:
                dia.mc.switch("down")
            if event.key == pygame.K_UP:
                dia.mc.switch("up")

            if event.key == 13:
                dia.mc.confirm()

    dia.show()
    pygame.display.flip()

pygame.quit()

