# LeapHigher - A Harmless Auto-clicker

LeapHigher is a Python script designed to automate the process of solving coding questions on a specific website or platform. It utilizes various libraries such as PyAutoGUI, Pytesseract, PyPerclip, and Pandas to capture screenshots, extract text from images, and interact with the user interface.

## Prerequisites

Before running the script, ensure that you have the following prerequisites installed:

- Python 3.x
- PyAutoGUI
- Pytesseract
- PyPerclip
- Pandas

You can install the required libraries using pip:

```
pip install pyautogui pytesseract pyperclip pandas
```

Additionally, you need to have the Tesseract OCR engine installed on your system for Pytesseract to work correctly.

## Usage

1. Clone the repository or download the project files:

```
git clone https://github.com/Eeman1113/LeapHigher.git
```

2. Place the CSV file containing the questions and answers in the `Database` folder with the name `database.csv`.

3. Ensure that the script is configured to work with your specific screen resolution and the coordinates of the web browser window.

4. Run the `main.py` script:

```
python main.py
```

The script will perform the following actions:

1. Read the questions and answers from the `database.csv` file.
2. Capture a screenshot of the question number region on the screen.
3. Extract the question number from the screenshot using Pytesseract.
4. Fetch the corresponding answer from the `database.csv` file.
5. Simulate clicking and typing actions to enter the answer in the code editor region.
6. Submit the answer and proceed to the next question.
7. Repeat the process for the specified number of iterations.

## Notes

- This script is designed to work on 13-inch MacBooks using the Arc browser.
- The coordinates used in the script (`pyautogui.click` and `pyautogui.screenshot` functions) are specific to the screen resolution and browser window position on the author's machine. You may need to adjust these coordinates according to your setup.
- The script assumes that the questions and answers are stored in a CSV file named `database.csv` in the `Database` folder.
- Ensure that the Tesseract OCR engine is installed and configured correctly on your system for Pytesseract to work properly.

## Disclaimer

This script is intended for educational and personal use only. It should not be used for any unethical or illegal purposes. The author is not responsible for any misuse or consequences arising from the use of this script.
