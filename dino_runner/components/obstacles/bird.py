import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    Y_POS_BIRD = 100
    X_POS_BIRD = 1000 

    def __init__(self):
        self.image = BIRD[0]
        super().__init__(self.image)
        self.rect.y = random.choice(self.Y_POS_BIRD)
        self.step_index = 0
        

    def update(self, game_speed, player):
        self.fly() 
        super().update(game_speed, player)

    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.bird_rect.x = self.image.get_rect()
        self.bird_rect.y = self.X_POS_BIRD
        self.step_index += 1




