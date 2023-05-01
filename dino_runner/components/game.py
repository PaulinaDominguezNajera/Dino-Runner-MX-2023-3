import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, CLOUD_2
from dino_runner.components.dinosaur import Dinosaur

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.cloud_speed = 11
        self.x_pos_cloud = 700
        self.y_pos_cloud = 70
        self.cloud_2_speed = 11
        self.x_pos_cloud_2 = 300
        self.y_pos_cloud_2 = 45
        self.player = Dinosaur()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = image_width
        self.x_pos_cloud -= self.cloud_speed

        self.screen.blit(CLOUD_2, (self.x_pos_cloud_2, self.y_pos_cloud_2))
        self.screen.blit(CLOUD_2, (image_width + self.x_pos_cloud_2, self.y_pos_cloud_2))
        if self.x_pos_cloud_2 <= -image_width:
            self.screen.blit(CLOUD_2, (image_width + self.x_pos_cloud_2, self.y_pos_cloud_2))
            self.x_pos_cloud_2 = image_width
        self.x_pos_cloud_2 -= self.cloud_2_speed

