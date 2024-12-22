import cv2
import numpy as np

def draw_boxes_on_screen(image, boxes):
    # Преобразовать изображение в массив numpy
    image_np = np.array(image)

    # Рисовать рамки вокруг найденных объектов
    for box in boxes:
        x1, y1, x2, y2, conf, cls = box
        cv2.rectangle(image_np, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

    # Отобразить изображение с рамками
    cv2.imshow('Detected Objects', image_np)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
