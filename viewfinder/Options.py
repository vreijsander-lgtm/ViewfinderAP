from dataclasses import dataclass
from random import choice
from typing import Dict
from Options import PerGameCommonOptions, Choice, Range, Toggle

class ProgressiveCamera(Toggle):
    """
    If this is on then the camera will be progressive
    """
    display_name = "Makes the camera progressive (Standee -> Hold)"
class Worlds(Choice):
    """
    Progressive: 1-1 and then 1-2 etc.
    Full_random: 1-1 and then 4.6 complete chaos
    off: levels won't be added to the pool and all levels will be open from the start
    """
    display_name = "Levels/worlds"
    option_Progressive = 0
    option_Full_random = 1
    option_off = 2
    default = 0
class Goals(Choice):
    """
    last_level: Beat the last level (the one with the timer)
    all_levels: Beat all levels (excluded optional levels)
    all_filters: Obtain all filters
    all_levels_inc_optional: Beat all levels (included optional levels)
    """
    display_name = "Goal"
    option_last_level = 0
    option_all_levels = 1
    option_all_filters = 2
    option_all_levels_inc_optional = 3
    default = 0
class Filters(Choice):
    """
    off: the filters won't be added to the pool
    on: the filters will be added to the pool
    """
    display_name = "Filters"
    option_off = 0
    option_on = 1
    default = 1
@dataclass
class Options(PerGameCommonOptions):
    progressive_camera: ProgressiveCamera
    world: Worlds
    goal: Goals
    filter: Filters
