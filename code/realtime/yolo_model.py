from ultralytics import YOLO

def detect_objects(image):
    # Загрузить модель YOLOv8
    model = YOLO('best.pt')

    # Обработать изображение
    results = model(image)

    # Получить координаты рамок
    boxes = results.xyxy[0].numpy()

    return boxes
