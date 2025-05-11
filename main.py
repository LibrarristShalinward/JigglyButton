from jiggly import Button
import dearpygui.dearpygui as dpg
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(2)

# 创建上下文和主题
dpg.create_context()

font_path = r"C:\Users\LibrarristShalinward\AppData\Local\Microsoft\Windows\Fonts\MapleMono-NF-CN-Regular.ttf"

# 加载字体（需要确保路径有效）
with dpg.font_registry():
    # 参数说明：字体文件路径，字体大小，自定义字体名称
    custom_font = dpg.add_font(font_path, 40, tag = "MapleMono")

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
    button = Button(
        size = 180,
        pos = (450, 300),
        theme = button_theme,
        font = custom_font,
        label = "Center",
        tag = "center_btn"
    )

# 应用自定义主题到按钮
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











# 主循环
while True:
    button()
    dpg.render_dearpygui_frame()
dpg.cleanup_dearpygui()
dpg.destroy_context()