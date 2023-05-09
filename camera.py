import pygame

import lib

class PlayerCenterCamera(pygame.sprite.Group):
    def __init__(self, display_surface: pygame.Surface):
        super().__init__()

        self.display_surface = display_surface
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

    def center_target_camera(self, target: pygame.sprite.Sprite):
        lib.global_offset.x = target.rect.centerx - self.half_width
        lib.global_offset.y = target.rect.centery - self.half_height

    def camera_draw(self, player: pygame.sprite.Sprite):
        self.center_target_camera(player)
        
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - lib.global_offset
            self.display_surface.blit(sprite.image, offset_pos)