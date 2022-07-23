import numpy as np
import pygame

# local imports
from . import utils


class Object:
    def __init__(self, constructor: np.ndarray):
        self.constructor = constructor

    def tick(self, dt: float):
        pass

    def draw(self, window: pygame.display):
        pass


class Ball(Object):
    def __init__(self,
                 center: np.ndarray,
                 radius: float,
                 color: tuple[int, int, int],
                 velocity: float,
                 direction: np.ndarray):
        Object.__init__(self, constructor=center)
        self.radius = radius
        self.color = color
        self.velocity = velocity
        self.direction = direction


    def draw(self, window: pygame.display):
        pygame.draw.circle(surface=window, color=self.color, center=self.constructor, radius=self.radius)


    def tick(self, dt: float):
        self.move(dt)


    def move(self, dt: float):
        self.constructor = utils.move_point(point=self.constructor,
                                            direction=self.direction,
                                            velocity=self.velocity,
                                            dt=dt)
