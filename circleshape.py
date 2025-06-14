import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this laterbootdev run a56fface-8a77-40ee-bf17-50d76078e5ec -s
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    def collision(self, CircleShape):
        distance = self.position.distance_to(CircleShape.position)
        return distance <= self.radius + CircleShape.radius
    