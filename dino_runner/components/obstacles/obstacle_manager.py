import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.shield_false import ShieldFalse
from dino_runner.components.obstacles.lava import Lava
from dino_runner.components.obstacles.ovni import Ovni

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self,game_speed,player):
        if len(self.obstacles) == 0:
            choice = random.choice([0,1,2,3,4])
            if choice == 0:
                self.obstacles.append(Cactus())
            elif choice == 1:
                self.obstacles.append(ShieldFalse())
            elif choice == 2:
                self.obstacles.append(Lava())
            elif choice == 3:
                self.obstacles.append(Ovni())
            else:
                self.obstacles.append(Bird())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width or obstacle.hammered:
                self.obstacles.remove(obstacle)
            obstacle.update(game_speed,player)

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles = []