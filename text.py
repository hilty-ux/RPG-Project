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

        self.rect.center = coordinates


class SavingAnim(pygame.sprite.Sprite):

    def __init__(self, coordinates):
        super().__init__()
        self.image = pygame.Surface((200, 100))
        self.image.fill((255, 255, 255))

        self.saving_text = CreateText("Saving...", 50, (100, 25))
        self.image.blit(self.saving_text.text, self.saving_text.rect)

        self.delay = pygame.time.get_ticks()
        self.delay_percentage = pygame.time.get_ticks()
        self.percent = 0

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates

    def update(self):

        time = pygame.time.get_ticks()
        if time - self.delay > 1000:
            self.kill()

        if time - self.delay_percentage > 100:
            self.percent += 10
            self.delay_percentage = time

        pygame.draw.rect(self.image, (0, 0, 0), (0, 50, 100, 50))
        pygame.draw.rect(self.image, (0, 255, 0), [0, 50, self.percent*10, 50])

