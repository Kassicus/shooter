import pygame

import lib
import player
import camera
import debug

pygame.init()

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode([lib.SCREEN_WIDTH, lib.SCREEN_HEIGHT])
        pygame.display.set_caption("Untitled Shooter")

        self.running = True
        self.clock = pygame.time.Clock()
        lib.events = pygame.event.get()

        self.debug_interface = debug.DebugInterface()

        self.world_camera = camera.PlayerCenterCamera(self.screen)
        self.player = player.Player()

        self.world_camera.add(self.player)

    def start(self):
        while self.running:
            self.events()
            self.draw()
            self.update()

    def events(self):
        lib.events = pygame.event.get()

        for event in lib.events:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    self.debug_interface.toggle_active()

    def draw(self):
        self.screen.fill(lib.color.black)

        self.world_camera.camera_draw(self.player)

        if self.debug_interface.active:
            self.debug_interface.draw()
        
    def update(self):
        self.world_camera.update()

        self.debug_interface.update(self.clock, self.player)
        pygame.display.update()
        lib.delta_time = self.clock.tick(lib.frame_limit) / 1000

if __name__ == '__main__':
    game = Game()
    game.start()
    pygame.quit()