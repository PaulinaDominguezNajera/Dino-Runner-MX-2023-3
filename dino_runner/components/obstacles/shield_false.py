from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SHIELD_FALSE

class ShieldFalse(Obstacle):
    Y_POS_SHIELD = 125

    def __init__(self):
        self.image = SHIELD_FALSE
        super().__init__(self.image)
        self.rect.y = self.Y_POS_SHIELD