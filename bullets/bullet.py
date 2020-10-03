from .body import Body

DEFAULT_EFFECTS = {"health": -0.1}


class Bullet(Body):
    def __init__(self, pos, radius, color, effects=None):
        super().__init__(pos=pos, radius=radius, color=color)
        if effects is None:
            effects = DEFAULT_EFFECTS

        self.effects = effects

    def hit_player(self, player):
        if self.is_overlapping(player):
            for key, value in self.effects.items():
                player.attributes[key] += value
