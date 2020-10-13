from .body import Body


class Actor(Body):
    def __init__(self, pos, radius, color, img=None):
        super().__init__(pos=pos, radius=radius, color=color, img=img)

        self._speed = 2

    def is_offscreen(self, w, h, fully=False):
        return super().is_offscreen(w, h, fully=fully)
