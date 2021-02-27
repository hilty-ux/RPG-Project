import pygame
import pygame.mixer


class SoundManager:

    def __init__(self):
        self.shield_hit_sound = pygame.mixer.Sound("assets/Sounds/shield_hit.mp3")
        self.shield_hit_sound.set_volume(0.25)

        self.swoosh_sound = pygame.mixer.Sound("assets/Sounds/swoosh.mp3")
        self.swoosh_sound.set_volume(0.25)

        self.sword_slice_sound = pygame.mixer.Sound("assets/Sounds/sword_slice.mp3")
        self.sword_slice_sound.set_volume(0.25)

    def shield_hit(self):
        self.shield_hit_sound.play()

    def swoosh(self):
        self.swoosh_sound.play()

    def slice(self):
        self.sword_slice_sound.play()