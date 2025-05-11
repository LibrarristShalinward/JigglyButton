from enum import Enum
from typing import Callable, TypeAlias
DPGID: TypeAlias = int | str

class Incident(Enum): 
    HOVER_ON = 0
    HOVER_OFF = 1
    CLICK_ON_AC = 2
    CLICK_ON_DE = 3
    CLICK_OFF_AC = 4
    CLICK_OFF_DE = 5
Callback: TypeAlias = Callable[[], None]