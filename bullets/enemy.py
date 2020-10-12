from .actor import Actor

class Enemy(Actor):
    def __init__(maxhealth, patterns, pcb1, pcb2, pcb3 )
        self.health = maxhealth
        self.maxhealth = maxhealth
        self.phase = 0
        self.status = "Alive"
        self.damage = 0
  ## pcbs are the phase change boundaries (i.e. maxhealth>current_health>pcb1 is 1st (base) phase, pcb1>current_health>pcb2 is 2nd phase, etc. etc. etc.)
        self.pcb1 = pcb1
        self.pcb2 = pcb2
        self.pcb3 = pcb3
  ## so what i was thinking here is that damage done to the boss is incremented per interval, and then reset every time the boss is updated - this way, everytime boss is updated,
  ## damage done between updates is incremented to the health and phase, and then the damage is reset to zero for the new interval after having been incremented in the update
  ## for the previous interval
    def update(damage)
        self.health -= damage
        self.damage = 0
        if  pcb1 < self.health <= maxhealth:
            self.phase = 0
        elif  pcb2 < self.health <= pcb1:
            self.phase = 1
        elif  pcb3 < self.health <= pcb2:
            self.phase = 2
        elif  0 < self.health <= pcb3:
            self.phase = 3
         
