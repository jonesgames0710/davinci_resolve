import pywinctl as pwc
import time
import pyautogui

# ウィンドウタイトルに'DaVinci Resolve'を含むウィンドウを探す
windows = pwc.getWindowsWithTitle('Project2')

if windows:
    window = windows[0]  # 最初に見つかったウィンドウ
    print(f"'{window.title}' ウィンドウが見つかりました。")
    
    # ウィンドウを前面に移動
    window.activate()
    
    # ウィンドウサイズや位置を変更する
    window.resize(1280, 720)  # 幅1280、高さ720に変更
    window.move(100, 100)     # 位置をx=100, y=100に移動

else:
    print("DaVinci Resolve のウィンドウが見つかりませんでした。")

    # DaVinci Resolveのウィンドウを取得
window = pwc.getAllTitles()  # タイトルにDaVinci Resolveを含むウィンドウを探す

for i in window:
    print(i)

# 少し待つ
time.sleep(2)
'''
# マウスを特定の位置に移動してクリック（この座標は実際の環境で確認する必要があります）
pyautogui.moveTo(100, 200)  # 例としてX=100, Y=200に移動
pyautogui.click()

# マウスでドラッグしてサイズを変更（例: 右下隅をつかんで縮小）
pyautogui.moveTo(500, 500)  # 縮小したい場所に移動
pyautogui.dragTo(300, 300, duration=1)  # 指定した位置までドラッグ
'''
