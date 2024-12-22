import pyautogui

def move_cursor_to_center(box):
    x1, y1, x2, y2, conf, cls = box
    center_x = ((x1 + x2) / 9) * 10
    center_y = (y1 + y2) / 2
    pyautogui.moveTo(center_x, center_y)
