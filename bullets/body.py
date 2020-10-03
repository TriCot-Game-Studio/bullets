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

    def is_overlapping(self, body):
        dist = ((self.x - body.x) ** 2 + (self.y - body.y) ** 2) ** 0.5
        return dist < self.radius + body.radius

    def is_offscreen(self, w, h, fully=True):
        if not fully:
            flag = (
                self.x - self.radius < 0
                or self.x + self.radius > w
                or self.y - self.radius < 0
                or self.y + self.radius > h
            )
        else:
            flag = (
                self.x + self.radius < 0
                or self.x - self.radius > w
                or self.y + self.radius < 0
                or self.y - self.radius > h
            )
        return flag
