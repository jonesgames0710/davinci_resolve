import pyautogui

# マウスを特定の位置に移動してクリック
pyautogui.moveTo(100, 100, duration=1)
pyautogui.click()

# テキストを入力
pyautogui.write("Hello, World!", interval=0.1)
