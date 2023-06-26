# TEX-Copier V1.0 by TEXploder (Beta)
This is a Python script that allows you to select an area on your screen and copy the text within that area to your clipboard. The selected text is processed using OCR (Optical Character Recognition) and then copied to the clipboard for further use.

![Logo](https://tools.tex-api.com/files/tex-copier-small-logo.png)



# Requirements
- Python 3.x
- easyocr library
- pyperclip library
- cv2 (OpenCV) library
- numpy library
- Pillow (PIL) library
- pynput library
- keyboard library



# Installation (for the Python Code)
Make sure you have Python 3.x installed on your system.
Install the required libraries by running the following command:

```pip install easyocr pyperclip opencv-python numpy Pillow pynput keyboard```

or with the requirements.txt file with following command:

```pip install -r requirements.txt```



# Installation (for the .exe file)
[Download The Exe File](https://tools.tex-api.com/files/TEX-Copier%20V1.0.exe) and just run it!

if you are wondering why the link: The .exe file is not Uploaded to github because it is 400mb and github does not like that :(



# Usage
- Run the script using Python: python tex_copier.py.
   
Or

- Run the .exe File.

Press ctrl + alt + c to start the selection process.
Left-click and hold the mouse to select an area on the screen containing the text you want to copy.
Release the mouse button to complete the selection.
The selected area will be captured as a screenshot and saved as tex_screen.png.
The captured image will be processed using OCR to extract the text.
The extracted text will be copied to your clipboard.
Paste the copied text wherever you need it.



# Note
The script uses the easyocr library for text recognition, supporting English and German languages by default. You can modify the text_recognition function to add or remove language support as needed.
Disclaimer: The TEX-Copier script is provided as-is without any warranty. Use it responsibly and respect the privacy of others when capturing and processing text from their screens.



Feel free to customize and enhance the script as per your requirements. And if you want to make it your own but on the base of mine then credit me: [TEXploder](https://www.texploder.com).
