import dearpygui.dearpygui as dpg
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(2)

# 创建上下文和主题
dpg.create_context()

font_path = r"C:\Users\LibrarristShalinward\AppData\Local\Microsoft\Windows\Fonts\MapleMono-NF-CN-Regular.ttf"
# font_path = "C:/Windows/Fonts/arial.ttf"

# 加载字体（需要确保路径有效）
with dpg.font_registry():
    # 参数说明：字体文件路径，字体大小，自定义字体名称
    custom_font = dpg.add_font(font_path, 40, tag = "MapleMono")
# dpg.set_global_font_scale(.5)

# 新增的窗口背景主题
with dpg.theme() as window_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (255, 255, 255, 0))

# 自定义按钮主题（蓝绿色）
with dpg.theme() as button_theme:
    with dpg.theme_component(dpg.mvButton):
        # dpg.add_theme_color(dpg.mvThemeCol_Button, (78, 164, 239, 255))  # 按钮颜色
        # dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (148, 195, 238, 255))  # 悬停颜色
        # dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (218, 226, 237, 255))  # 按下颜色
        dpg.add_theme_color(dpg.mvThemeCol_Button, (78, 164, 239, 255))  # 按钮颜色
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (78, 164, 239, 255))  # 悬停颜色
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (78, 164, 239, 255))  # 按下颜色
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 15)  # 圆角半径

# 创建主窗口
with dpg.window(label = "Center Button Demo", tag = "Primary Window"):
    # # 创建用于居中的容器
    # with dpg.group(horizontal = True):
    #     dpg.add_spacer(width = 40)  # 左侧间距
        
    #     # 垂直居中容器
    #     with dpg.group():
    #         dpg.add_spacer()  # 顶部间距
    #         button = dpg.add_button(
    #             label = "Click Me", 
    #             indent = 0, 
    #             width = 180,       # 按钮宽度
    #             height = 180,      # 按钮高度（与宽度相同形成方形）
    #             # pos = (360, 210), 
    #             tag = "center_btn"
    #         )
    #         dpg.set_item_font(button, "MapleMono")
    #         dpg.add_spacer()  # 底部间距
        
    #     dpg.add_spacer(width = 40)  # 右侧间距
    button = dpg.add_button(
        label = "Click Me", 
        indent = 0, 
        width = 160,       # 按钮宽度
        height = 160,      # 按钮高度（与宽度相同形成方形）
        pos = (370, 220), 
        tag = "center_btn"
    )
    dpg.set_item_font(button, "MapleMono")

# 应用自定义主题到按钮
dpg.bind_item_theme(button, button_theme)
dpg.bind_item_theme("Primary Window", window_theme)

# 视口设置
dpg.create_viewport(
    title = "Centered Button Example",
    width = 900,
    height = 600
)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)



class ButtonHandler: 
    def __init__(self):
        self.hovered = False
        self.clicked = False
        self.opened = False
    
    def __call__(self): 
        if not self.hovered and dpg.is_item_hovered("center_btn"): 
            self.hovered = True
        elif self.hovered and not dpg.is_item_hovered("center_btn"): 
            self.hovered = False
        else: pass

        if not self.clicked and dpg.is_item_active("center_btn"): 
            self.clicked = True
        elif self.clicked and not dpg.is_item_active("center_btn"): 
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
    
    def set_button_size(self, size: float = 180.): 
        dpg.set_item_width(button, size)
        dpg.set_item_height(button, size)
        dpg.set_item_pos(button, (450 - size / 2, 300 - size / 2))







# 主循环
bh = ButtonHandler()
while True:
    bh()
    dpg.render_dearpygui_frame()
dpg.cleanup_dearpygui()
dpg.destroy_context()