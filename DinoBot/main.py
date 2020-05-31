from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PIL import ImageGrab
import pyautogui
import time

pyautogui.FAILSAFE = True


def play():
    size = pyautogui.size()
    if size.width == 1366 and size.height == 768:
        img = ImageGrab.grab().convert('L')
        data = img.load()
        for i in range(157, 180):
            for j in range(390, 465):
                if data[i, j] == 172:
                    pyautogui.keyDown('up')


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.implicitly_wait(100)
    driver.maximize_window()
    driver.get('chrome://dino/')
    time.sleep(2)
    pyautogui.press('up')
    time.sleep(2)
    while True:
        play()


if __name__ == '__main__':
    main()
    time.sleep(10)
