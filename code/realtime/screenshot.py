import pyscreenshot as ImageGrab

def take_screenshot():
    # Сделать скриншот всего экрана
    screenshot = ImageGrab.grab()
    return screenshot
