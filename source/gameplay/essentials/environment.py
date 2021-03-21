from ..components.transporters.springs.gravity_spring import Grav_Spring
from ..components.platforms.block import Block
from ..components.platforms.mobile import Mobile
from ..components.hazards.spike import Spike
from ..characters.cube import Cube
from .base import Base
from .background import Bg
from ..utils.constants import *
from ...graphics.images_loader import BASE, BLOCK, GRAV_SPRING, MOBILE_RECTANGLE, SPIKE

class Environment:
    
    def __init__(self):
        self.base = Base(WIN_HEIGHT - BASE.get_height())
        self.top = Base(BASE.get_height())
        self.background = Bg(0)
        self.spikes = [Spike(800, WIN_HEIGHT - BASE.get_height() - SPIKE.get_height(), 0)]
        self.blocks = [Block(1200, WIN_HEIGHT - BASE.get_height() - BLOCK.get_height(), 0)]
        self.mobiles = [Mobile(1550, WIN_HEIGHT - BASE.get_height() - MOBILE_RECTANGLE.get_height(), 0)]
        self.spikes = [Grav_Spring(800, WIN_HEIGHT - BASE.get_height() - GRAV_SPRING.get_height(), 0)]
        self.cube = Cube(200, 200)


    def map_setup(self):
        self.blocks.append(Block(800, WIN_HEIGHT - BASE.get_height() - BLOCK.get_height(), 0))
        self.blocks.append(Block(1050, WIN_HEIGHT - BASE.get_height() - BLOCK.get_height(), 0))
        self.blocks.append(Block(1050, WIN_HEIGHT - BASE.get_height() - BLOCK.get_height() - 75, 0))
        self.mobiles.append(Mobile(3900, WIN_HEIGHT - BASE.get_height() - MOBILE_RECTANGLE.get_height(), 0))
        self.spikes.append(Grav_Spring(1200, BASE.get_height()- GRAV_SPRING.get_height()-15, 180))
