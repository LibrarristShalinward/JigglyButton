from .type import DPGID
from typing import Callable
import dearpygui.dearpygui as dpg


class ButtonHandler: 
    def __init__(self, 
                button: DPGID, 
                size_setter: Callable[[float], None]
            ): 
        self.button = button
        self.hovered = False
        self.clicked = False
        self.opened = False
        self.set_button_size = size_setter
    
    def __call__(self): 
        if not self.hovered and dpg.is_item_hovered(self.button): 
            self.hovered = True
        elif self.hovered and not dpg.is_item_hovered(self.button): 
            self.hovered = False
        else: pass

        if not self.clicked and dpg.is_item_active(self.button): 
            self.clicked = True
        elif self.clicked and not dpg.is_item_active(self.button): 
            self.clicked = False
            self.opened = not self.opened
        else: pass

        if self.clicked: 
            self.set_button_size(200)
        elif self.hovered: 
            self.set_button_size(190)
        elif self.opened: 
            self.set_button_size(180)
        else: 
            self.set_button_size(160)