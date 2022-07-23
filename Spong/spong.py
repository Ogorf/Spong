import pygame
import numpy as np

# local imports
from . import objects
from . import utils


class Spong:
    def __init__(self):
        self.fps = 60
        self.objects = []
        self.name = 'Spong_dep'
        self.window_width = 900
        self.window_height = 600
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self._setup()


    def _setup(self):
        pygame.init()
        pygame.display.set_caption(self.name)
        ball = objects.Ball(center=np.array([100., 100.]),
                            color=utils.red,
                            direction=np.array([2.,1.]),
                            velocity=0.05,
                            radius=40)
        self.objects.append(ball)


    def tick(self, dt: float):
        for obj in self.objects:
            obj.tick(dt)


    def draw(self):
        self.window.fill(utils.black)
        for obj in self.objects:
            obj.draw(self.window)
        pygame.display.update()


    def game_loop(self):
        clock = pygame.time.Clock()

        while True:
            dt = clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.tick(dt)
            self.draw()
