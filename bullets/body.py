import pygame

# base class for objects with {hitboxes}
# ## method
# * is_overlapping (input in another body, output bool indicating overlap)
# * draw/render
# * maybe. update? have a general physics engine built in this class?


class Body:
    def __init__(self, pos, radius, color, img=None, angle=0):
        self.x, self.y = pos
        self.radius = radius
        self.color = color

        self.angle = angle

        if img is not None:
            # Resize asset to fit in circle
            w, h = img.get_size()
            if h > w:
                new_h = radius * 2.1
                new_w = w * new_h / h
            else:
                new_w = radius * 2.1
                new_h = h * new_w / h

            self.img = pygame.transform.scale(img, (round(new_w), round(new_h)))
        else:
            self.img = None

    def render(self, screen):
        if self.img is None:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        else:
            # For debug
            # TODO: delete me or add a DEBUG flag or something
            # pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

            w, h = self.img.get_size()
            rot_image = pygame.transform.rotate(self.img, self.angle)
            screen.blit(rot_image, (self.x - w // 2, self.y - h // 2))

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
