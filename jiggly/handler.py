from .type import Incident, Callback, DPGID
import dearpygui.dearpygui as dpg



class ButtonHandler: 
    __BLANK_CALLBACK: Callback = lambda: None
    def __init__(self, 
                button: DPGID, 
                incident_callbacks: dict[Incident, Callback] = {}
            ): 
        self.button = button
        self.hovered = False
        self.clicked = False
        self.opened = False
        self.callbacks = {
            inc: incident_callbacks[inc] if inc in incident_callbacks.keys() else self.__BLANK_CALLBACK
            for inc in Incident
        }
    
    def __call__(self): 
        if not self.hovered and dpg.is_item_hovered(self.button): 
            self.callbacks[Incident.HOVER_ON]()
            self.hovered = True
        elif self.hovered and not dpg.is_item_hovered(self.button): 
            self.callbacks[Incident.HOVER_OFF]()
            self.hovered = False
        else: pass

        if not self.clicked and dpg.is_item_active(self.button): 
            self.callbacks[Incident.CLICK_ON_AC if self.opened else Incident.CLICK_ON_DE]()
            self.clicked = True
        elif self.clicked and not dpg.is_item_active(self.button): 
            self.callbacks[Incident.CLICK_OFF_AC if self.opened else Incident.CLICK_OFF_DE]()
            self.clicked = False
            self.opened = not self.opened
        else: pass
    def __getitem__(self, inc: Incident): 
        def decorator(callback: Callback): 
            self.callbacks[inc] = callback
            return callback
        return decorator