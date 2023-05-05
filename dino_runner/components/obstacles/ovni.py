import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import OVNI

class Ovni(Obstacle):

    def __init__(self):
        self.image = OVNI
        super().__init__(self.image)
        self.rect.y = random.choice([100,240,260,320])