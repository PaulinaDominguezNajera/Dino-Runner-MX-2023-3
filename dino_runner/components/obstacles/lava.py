from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LAVA

class Lava(Obstacle):
    Y_POS_LAVA = 390

    def __init__(self):
        self.image = LAVA
        super().__init__(self.image)
        self.rect.y = self.Y_POS_LAVA