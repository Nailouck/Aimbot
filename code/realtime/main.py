from screenshot import take_screenshot
from yolo_model import detect_objects
from draw_boxes import draw_boxes_on_screen
from move_cursor import move_cursor_to_center

def main():
    # Сделать скриншот экрана
    screenshot = take_screenshot()

    # Обработать скриншот с помощью YOLOv8
    boxes = detect_objects(screenshot)

    # Нарисовать рамки вокруг найденных объектов
    draw_boxes_on_screen(screenshot, boxes)

    # Навести курсор в центр первого найденного объекта
    if boxes:
        move_cursor_to_center(boxes[0])

if __name__ == "__main__":
    main()
