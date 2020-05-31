import pyautogui
import time
from PIL import ImageGrab

__name__ = '__draw__'
pyautogui.FAILSAFE = True


def main():
    time.sleep(3)
    size = pyautogui.size()
    if size.width == 1366 and size.height == 768:
        img = ImageGrab.grab().convert('L')
        data = img.load()
        for i in range(157, 180):
            for j in range(390, 465):
                data[i, j] = 172
        img.show()


if __name__ == '__draw__':
    main()
