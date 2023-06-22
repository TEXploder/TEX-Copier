import easyocr
import pyperclip
import cv2
import numpy as np
from PIL import ImageGrab
from pynput import mouse
import keyboard
import shutil

def center_text(text):
    terminal_width = shutil.get_terminal_size().columns
    spaces = (terminal_width - len(text)) // 2
    centered_text = ' ' * spaces + text
    return centered_text

def preprocess_image(image):
    # convert image into grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Application of an adaptive threshold for binarization
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # Applying morphology operations to improve text contrast
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    morph = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)
    return morph

def on_key_press(event):
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and event.name == 'c':
        print("Hold leftclick to select area to copy the text.")
        
        start_x, start_y, end_x, end_y = (0, 0, 0, 0)
        def on_click(x, y, button, pressed):
            nonlocal start_x, start_y, end_x, end_y

            if pressed:
                start_x, start_y = x, y
            else:
                end_x, end_y = x, y
                return False

        with mouse.Listener(on_click=on_click) as listener:
            listener.join()

        left = min(start_x, end_x)
        top = min(start_y, end_y)
        width = abs(start_x - end_x)
        height = abs(start_y - end_y)

        # grab selected area es screenshot
        screenshot = ImageGrab.grab(bbox=(left, top, left + width, top + height))
        screenshot.save('tex_screen.png')

        # image processing
        image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        preprocessed_image = preprocess_image(image)

        # TEX(t) recognition
        def text_recognition(image_path):
            strOut = ""
            reader = easyocr.Reader(['en', 'de'])
            output = reader.readtext(image_path)
            for item in output:
                print(item[1])
                strOut += item[1] + "\n"

            return strOut

        pyperclip.copy(text_recognition("tex_screen.png"))

        print("Selected Text was copied to clipboard!")
        print("___________________________________________")
        print("To start the selection, press ctrl + alt + c")

if __name__ == "__main__":
    print(center_text("████████╗███████╗██╗  ██╗      ██████╗ ██████╗ ██████╗ ██╗███████╗██████╗ "))
    print(center_text("╚══██╔══╝██╔════╝╚██╗██╔╝     ██╔════╝██╔═══██╗██╔══██╗██║██╔════╝██╔══██╗"))
    print(center_text("   ██║   █████╗   ╚███╔╝█████╗██║     ██║   ██║██████╔╝██║█████╗  ██████╔╝"))
    print(center_text("   ██║   ██╔══╝   ██╔██╗╚════╝██║     ██║   ██║██╔═══╝ ██║██╔══╝  ██╔══██╗"))
    print(center_text("   ██║   ███████╗██╔╝ ██╗     ╚██████╗╚██████╔╝██║     ██║███████╗██║  ██║"))
    print(center_text("   ╚═╝   ╚══════╝╚═╝  ╚═╝      ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝"))
    print(center_text("_________________________________ V 1.0 _________________________________"))
    while True:
        print("To start the selection, press ctrl + alt + c")
        keyboard.on_press(on_key_press)
        keyboard.wait()
