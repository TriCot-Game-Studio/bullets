import pygame

# base class for objects with {hitboxes}
# ## method
# * is_overlapping (input in another body, output bool indicating overlap)
# * draw/render
# * maybe. update? have a general physics engine built in this class?


class Body:
    def __init__(self, pos, radius, color):
        self.x, self.y = pos
        self.radius = radius
        self.color = color

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def is_overlapping(self):
        pass
