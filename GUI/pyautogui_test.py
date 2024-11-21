import pyautogui
import time

# カーソルを指定した座標に移動
pyautogui.moveTo(830, 400, duration=0)  # x=100, y=200の位置に1秒かけて移動

# 左クリック
pyautogui.click()

# 右クリック（オプションで）
pyautogui.click(button='right')

# ショートカットキーを送信
pyautogui.hotkey('ctrl', 'c')  # Ctrl+Cを送信

# 数値を入力
pyautogui.write('57')
57

# エンターキーを押す
pyautogui.press('enter')