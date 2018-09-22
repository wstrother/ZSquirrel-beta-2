import pygame

from app.get_context import get_context_classes
from app.pygame_screen import PygameScreen
from zs2.context import Context
from zs2.game import Game
from zs2.resources import load_resource
from zs_constants import Settings

pygame.init()
# pygame.mixer.quit()
# pygame.mixer.init(buffer=256)


if __name__ == "__main__":
    scr = PygameScreen()
    clock = pygame.time.Clock()
    game = Game(scr, clock, Settings.FRAME_RATE)

    env = load_resource(Settings.APP_START)
    entities, interfaces = get_context_classes()
    class_dict = {
        cls.__name__: cls for cls in entities
    }

    Context(game, class_dict, *interfaces).load_environment(env)

    game.main()
