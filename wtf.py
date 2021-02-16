import pyautogui

pyautogui.hotkey('win', 'r')
pyautogui.write('cmd')
pyautogui.press('enter')
pyautogui.moveTo(500, 500)
pyautogui.click()
pyautogui.write('shutdown /r')
pyautogui.press('enter')