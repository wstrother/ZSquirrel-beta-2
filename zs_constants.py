class Settings:
    FRAME_RATE = 60
    SCREEN_SIZE = 800, 600
    APP_START = "start.json"
    DEFAULT_STYLE = "default_style.json"

    DEFAULT_FONT_SIZE = 16
    TEXT_CUTOFF = 100
    FONT_COLOR = 255, 255, 255
    FONT_HIGHLIGHT = 0, 255, 0

    HUD_CACHE_SIZE = 60
    HUD_FRAME_RULE = 10


class ControllerInputs:
    CONTROLLER_FRAME_DEPTH = 300
    INIT_DELAY = 30
    HELD_DELAY = 15
    UDLR = "up", "down", "left", "right"
    AXES = "x_axis", "y_axis"
    STICK_DEAD_ZONE = .1
    AXIS_MIN = .9


class Resources:
    JSON = "json"
    TMX = "tmx"
    ENVIRONMENTS = JSON, "environments"

    RESOURCES = "resources"
    IMAGES = RESOURCES, "images"
    SOUNDS = RESOURCES, "sounds"
    STYLES = RESOURCES, "styles"
    TILEMAPS = RESOURCES, "tilemaps"

    IMAGE_EXT = "gif", "png", "jpg", "svg", "bmp", "ico"
    SOUND_EXT = ".wav", ".mp3", ".ogg", ".flac"


class ApiConstants:
    # object method prefixes
    SET_ = "set_"   # set_attr()
    ON_ = "on_"     # on_event()


class Zson:
    # json bool keywords
    FALSE_KEYWORD = "false"
    TRUE_KEYWORD = "true"
    NONE_KEYWORD = "null"


class ZsData:
    # built in keywords
    CONTEXT = "context"
    NAME = "name"
    CLASS = "class"
    ENVIRONMENT = "environment"
    GAME = "game"
    GROUP = "group"
    PARENT_LAYER = "parent_layer"

    # default class_dict
    LAYER = "Layer"
    SPRITE = "Sprite"
    ENTITY = "Entity"

    # section names
    GROUPS = "groups"
    SPRITES = "sprites"
    LAYERS = "layers"
