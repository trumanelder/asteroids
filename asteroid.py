import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            split_one_rotation = self.velocity.rotate(angle)
            split_two_rotation = self.velocity.rotate(-angle)
            radius = self.radius - ASTEROID_MIN_RADIUS
            split_one = Asteroid(self.position.x, self.position.y, radius)
            split_two = Asteroid(self.position.x, self.position.y, radius)
            split_one.velocity = split_one_rotation * 1.2
            split_two.velocity = split_two_rotation * 1.2