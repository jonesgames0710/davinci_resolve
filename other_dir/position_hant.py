import pyautogui
import time

# 現在のマウス位置をリアルタイムで表示
while True:
    x, y = pyautogui.position()
    print(f"Mouse position: ({x}, {y})")
    time.sleep(1)  # 1秒ごとに表示