import os
import pygame
from . import tools
from .import constants as c

#ORIGINAL_CAPTION = c.ORIGINAL_CAPTION

pygame.init()
#pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
#pg.display.set_caption(c.ORIGINAL_CAPTION)
SCREEN = pygame.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()


GFX   = tools.load_all_gfx(os.path.join("graphics"))
