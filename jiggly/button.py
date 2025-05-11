from .dynamic import DynamicValue, ConstantProcess
from .handler import ButtonHandler
from .type import DPGID, Incident
import dearpygui.dearpygui as dpg



class JigglyButton: 
    def __init__(self, 
                size: float, 
                pos: tuple[float, float], 
                theme: None | DPGID = None, 
                font: None | DPGID = None, 
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
        self.handler = ButtonHandler(
            self.item, 
            {
                Incident.HOVER_ON: 
                    lambda: self.dy_size[ConstantProcess](.3, 10.), 
                Incident.HOVER_OFF: 
                    lambda: self.dy_size[ConstantProcess](.3, -10.), 
                Incident.CLICK_ON_AC: 
                    lambda: self.dy_size[ConstantProcess](.3, 15.), 
                Incident.CLICK_OFF_AC: 
                    lambda: self.dy_size[ConstantProcess](.3, -30.), 
                Incident.CLICK_ON_DE: 
                    lambda: self.dy_size[ConstantProcess](.3, 30.), 
                Incident.CLICK_OFF_DE: 
                    lambda: self.dy_size[ConstantProcess](.3, -15.), 
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