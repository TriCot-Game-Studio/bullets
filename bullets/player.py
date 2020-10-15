import math
import pygame
from .actor import Actor
from .bullet import Bullet


class Player(Actor):
    def __init__(self, pos, radius, color, img=None, bullet_img=None):
        super().__init__(pos=pos, radius=radius, color=color, img=img)
        self.attributes = {"health": 1, "speed": 1, "confused": 0}

        self._speed = 10

        self.bullets = []
        self.bullet_speed = 20
        self.max_bullets = 40
        self.is_shooting = False
        self.shoot_cool_down = 10
        self.t_since_last_shot = 0
        self.bullet_img = bullet_img

        self.kill_counter = 0

        # TODO: should this be in base Body class for other Body objects?
        self.dx = 0
        self.dy = 0

    @property
    def is_alive(self):
        return self.attributes["health"] > 0

    @property
    def speed(self):
        return self._speed * self.attributes["speed"]

    @speed.setter
    def speed(self, x):
        self._speed = x

    @property
    def health(self):
        return self.attributes["health"] * 100

    @health.setter
    def health(self, x):
        self.attributes["health"] += x / 100

    def _update_shot_bullets(self):
        for i, bullet in enumerate(self.bullets):
            bullet.update()

    def _prune_dead_bullets(self):
        self.bullets = [b for b in self.bullets if not b.dead]

    def _shoot(self):
        if self.t_since_last_shot > self.shoot_cool_down:
            self.t_since_last_shot = 0
            bullet = Bullet(
                (self.x, self.y),
                radius=10,
                color=(255, 0, 0),
                bounces=False,
                dx=self.bullet_speed * math.cos(math.radians(self.angle)),
                dy=-self.bullet_speed * math.sin(math.radians(self.angle)),
                img=self.bullet_img,
                angle=self.angle,
            )

            self.bullets.append(bullet)
            if len(self.bullets) > self.max_bullets:
                self.bullets.pop(0)

    def update(self, w, h):
        if self.attributes["confused"] > 0:
            self.attributes["confused"] -= 1

        if self.is_shooting:
            self._shoot()

        self._prune_dead_bullets()
        self._update_shot_bullets()
        self.t_since_last_shot += 1

        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        if self.is_offscreen(w, h):
            if self.x < self.radius:
                self.x = self.radius
            elif self.x > w - self.radius:
                self.x = w - self.radius

            if self.y < self.radius:
                self.y = self.radius
            elif self.y > h - self.radius:
                self.y = h - self.radius

        # update angle for pointing asset/shooting
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # SOH CAH TOA
        opposite = self.y - mouse_y
        adjacent = self.x - mouse_x
        self.angle = 180 - math.degrees(math.atan2(opposite, adjacent))

    def render(self, screen):
        for bullet in self.bullets:
            bullet.render(screen=screen)
        super().render(screen=screen)
