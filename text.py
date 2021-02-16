import pygame


class PopUp:

    def __init__(self, screen):
        self.screen = screen
        self.text_box = pygame.image.load("assets/Assets rpg pack/rpg-pack/UI/generic-rpg-ui-text-box.png")
        self.rect_txt_box = self.text_box.get_rect()

        self.sentence1 = CreateText("Hello !", 50, (1, 1))

    def update(self, coordinates):

        self.rect_txt_box.left, self.rect_txt_box.bottom = coordinates
        self.sentence1.rect.left, self.sentence1.rect.bottom = coordinates[0] + 10, coordinates[1] - 10

        self.screen.blit(self.text_box, self.rect_txt_box)
        self.screen.blit(self.sentence1.text, self.sentence1.rect)


class CreateText:

    def __init__(self, text, size, coordinates):
        self.police = pygame.font.Font("assets/Police/advanced_pixel-7.ttf", size)

        self.text = self.police.render(text, True, (0, 0, 0))
        self.rect = self.text.get_rect()

        self.rect.left, self.rect.bottom = coordinates