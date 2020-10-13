from .actor import Actor


class Enemy(Actor):
    def __init__(self, pos, radius, color, max_health, pcb1, pcb2, pcb3):
        super().__init__(pos=pos, radius=radius, color=color)
        self.health = max_health
        self.max_health = max_health
        self.phase = 0
        self.damage = 0
        self.pcb1 = pcb1
        self.pcb2 = pcb2
        self.pcb3 = pcb3
        # pcbs are health thresholds for phase change

    @property
    def is_alive(self):
        return self.health > 0

    def update(self, damage):
        # so what i was thinking here is that damage
        # done to the boss is incremented per interval,
        # and then reset every time the boss is updated -
        # this way, everytime boss is updated,
        # damage done between updates is incremented to
        # the health and phase, and then the damage is reset
        # to zero for the new interval after having been
        # incremented in the update for the previous interval
        self.health -= damage
        self.damage = 0
        if self.pcb1 < self.health <= self.max_health:
            self.phase = 0
        elif self.pcb2 < self.health <= self.pcb1:
            self.phase = 1
        elif self.pcb3 < self.health <= self.pcb2:
            self.phase = 2
        elif 0 < self.health <= self.pcb3:
            self.phase = 3
