from .dynamic import CosineProcess, DampProcess, DynamicValue
from .handler import ButtonHandler
from .type import DPGID, Incident
import dearpygui.dearpygui as dpg



class AnimeConfig: 
    def __init__(self, 
                hover_delay: float = .1, 
                switch_delay: float = .1, 
                jig_delay: float = .5, 
                hover_buffer: float = 10., 
                press_buffer: float = 5., 
                open_buffer: float = 60., 
            ):
        HD = hover_delay
        SD = switch_delay
        JD = jig_delay
        HB = hover_buffer
        PB = press_buffer
        OB = open_buffer + press_buffer
        self.ani_config = {
            Incident.HOVER_ON: (HD, HB), 
            Incident.HOVER_OFF: (HD, -HB), 
            Incident.CLICK_ON_AC: (SD, PB), 
            Incident.CLICK_OFF_AC: (JD, -OB), 
            Incident.CLICK_ON_DE: (SD, OB), 
            Incident.CLICK_OFF_DE: (JD, -PB), 
        }

class JigglyButton: 
    def __init__(self, 
                size: float, 
                pos: tuple[float, float], 
                theme: None | DPGID = None, 
                font: None | DPGID = None, 
                ani: AnimeConfig = AnimeConfig(), 
                **kwargs
            ): 
        """创建一个Q弹的按钮

        Args:
            size (float): 按钮大小
            pos (tuple[float, float]): 按钮位置
            theme (None | DPGID, optional): 按钮主题, 默认为None. 
            font (None | DPGID, optional): 按钮字体, 默认为None.
        """
        self.center = pos
        self.item = dpg.add_button(
            width = int(size),       # 按钮宽度
            height = int(size),      # 按钮高度（与宽度相同形成方形）
            pos = (
                int(pos[0] - size / 2), 
                int(pos[1] - size / 2),
            ), 
            **kwargs
        )
        if theme is not None: 
            dpg.bind_item_theme(self.item, theme)
        if font is not None: 
            dpg.set_item_font(self.item, font)
        
        self.dy_size = DynamicValue(size)
        def make_callback(inc): 
            if inc in [Incident.CLICK_OFF_AC, Incident.CLICK_OFF_DE]: 
                return lambda: self.dy_size[
                    DampProcess
                ](*ani.ani_config[inc])
            else: 
                return lambda: self.dy_size[
                    CosineProcess
                ](*ani.ani_config[inc])
        self.handler = ButtonHandler(
            self.item, 
            {
                inc: make_callback(inc)
                for inc in Incident
            }
        )
    
    def set_size(self, size: float): 
        dpg.set_item_width(self.item, size)
        dpg.set_item_height(self.item, size)
        dpg.set_item_pos(self.item, (
            int(self.center[0] - size / 2), 
            int(self.center[1] - size / 2),
        ))
    
    def __call__(self): 
        self.set_size(self.dy_size.value)
        self.handler()