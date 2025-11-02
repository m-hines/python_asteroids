import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = 0
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    def update(self, dt):
        self.position += (self.velocity * dt)
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SHOOT_SPEED * dt
