# import pyautogui
# import time
# import pytesseract
# import pyperclip
# import pandas as pd 

# k = pd.read_csv('./Database/database.csv')


# def problem_solved():
#     r=k['Question']
#     time.sleep(7) 
#     imi = pyautogui.screenshot('./Image/pre.png',region=(1188, 868, 534, 98))
#     texti = pytesseract.image_to_string("./Image/pre.png")
#     if texti == 'Subscribe to unlock.\n': 
#         pyautogui.click(x=234,  y=19, clicks=1, button='left') #press go to next question button
#     else:
#         im = pyautogui.screenshot('./Image/test1.png',region=(37,201, 1388, 90)) #take ss of the question number
#         text = pytesseract.image_to_string("./Image/test1.png")
#         text = text.split('.')[0] #extract question number
#         # print(text)
#         ans = r[int(text)-1] #fetch the answer
#         # print(ans)
#         pyautogui.click(x=1139, y=247, clicks=1, button='left') #click on the code editor region
#         time.sleep(3)
#         pyautogui.hotkey('command','a') #select the boiler plate code
#         time.sleep(1)
#         pyautogui.hotkey('command','x')  #remove the boiler plate code
#         time.sleep(1)
#         pyperclip.copy(ans) #copy answer to clipboard
#         time.sleep(1)
#         pyautogui.hotkey('command','v') #paste answer on editor region
#         time.sleep(1)
#         pyautogui.click(x=1379, y=440, clicks=1, button='left') #press submit button
#         time.sleep(7)
#         pyautogui.click(x=234,  y=19, clicks=1, button='left') #press go to next question button
# for i in range(0,100):
#     problem_solved()
#     print("Question Number Done !!!  ",i+1)
#     time.sleep(5)
# # print(pyautogui.position())





import pyautogui
import time
import pytesseract
import pyperclip
import pandas as pd
import sys
import os

# Function to handle the main logic
def problem_solved():
    try:
        k = pd.read_csv('./Database/database.csv')
        r = k['Question']
        time.sleep(7)
        imi = pyautogui.screenshot('./Image/pre.png', region=(1188, 868, 534, 98))
        texti = pytesseract.image_to_string("./Image/pre.png")
        if texti == 'Subscribe to unlock.\n':
            pyautogui.click(x=234, y=19, clicks=1, button='left')  # press go to next question button
        else:
            im = pyautogui.screenshot('./Image/test1.png', region=(37, 201, 1388, 90))  # take ss of the question number
            text = pytesseract.image_to_string("./Image/test1.png")
            text = text.split('.')[0]  # extract question number
            ans = r[int(text) - 1]  # fetch the answer
            pyautogui.click(x=1139, y=247, clicks=1, button='left')  # click on the code editor region
            time.sleep(3)
            pyautogui.hotkey('command', 'a')  # select the boiler plate code
            time.sleep(1)
            pyautogui.hotkey('command', 'x')  # remove the boiler plate code
            time.sleep(1)
            pyperclip.copy(ans)  # copy answer to clipboard
            time.sleep(1)
            pyautogui.hotkey('command', 'v')  # paste answer on editor region
            time.sleep(1)
            pyautogui.click(x=1379, y=440, clicks=1, button='left')  # press submit button
            time.sleep(7)
            pyautogui.click(x=234, y=19, clicks=1, button='left')  # press go to next question button
    except ValueError as e:
        print(f"Error encountered: {e}. Restarting...") 
        time.sleep(5)  # Optional delay before restarting
        pyautogui.click(x=234, y=19, clicks=1, button='left')
        python = sys.executable
        os.execl(python, python, * sys.argv)  # Restart the script

# Main loop
for i in range(0, 10):
    problem_solved()
    print("Question Number Done !!!  ", i + 1)
    time.sleep(5)
