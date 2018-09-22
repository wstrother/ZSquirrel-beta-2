import pygame

from zs2.game import Screen
from zs2.resources import Image
from zs_constants import Settings


class PygameScreen(Screen):
    def __init__(self):
        self._screen = pygame.display.set_mode(Settings.SCREEN_SIZE)

    def refresh(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.flip()
        self._screen.fill((0, 0, 0))

    def render_graphics(self, image, *args):
        render_graphics(self._screen, image, *args)


def render_graphics(screen, image, *args):
    if type(image) is Image:
        position = args[0]
        screen.blit(image.pygame_surface, position)

    else:
        render_geometry(screen, image, *args)


def render_geometry(screen, method, *args):
    if method == "rect":
        args = list(args)
        args[1] = args[1].pygame_rect

        pygame.draw.rect(screen, *args)

    if method == "line":
        pygame.draw.line(screen, *args)

    if method == "circle":
        pygame.draw.circle(screen, *args)
