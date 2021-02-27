import pygame
import pygame.mixer


class SoundManager:

    def __init__(self):
        try:
            self.shield_hit_sound = pygame.mixer.Sound("assets/Sounds/shield_hit.mp3")
            self.shield_hit_sound.set_volume(0.25)

            self.swoosh_sound = pygame.mixer.Sound("assets/Sounds/swoosh.mp3")
            self.swoosh_sound.set_volume(0.25)

            self.sword_slice_sound = pygame.mixer.Sound("assets/Sounds/sword_slice.mp3")
            self.sword_slice_sound.set_volume(0.25)
        except pygame.error:
            pass

    def shield_hit(self):
        try:
            self.shield_hit_sound.play()
        except Exception as e:
            print(e)

    def swoosh(self):
        try:
            self.swoosh_sound.play()
        except Exception as e:
            print(e)

    def slice(self):
        try:
            self.sword_slice_sound.play()
        except Exception as e:
            print(e)