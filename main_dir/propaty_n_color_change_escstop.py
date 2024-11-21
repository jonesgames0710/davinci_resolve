'''
指定したビンのタイムラインを取得してサイズなどのプロパティを変更する。クリップは結合しなくても変更できる。
カラーグレーディングをpyautofuiモジュールでウィンドウを追加してエフェクトのブラーを適応させる
作業手順5-2
'''

import DaVinciResolveScript as dvr
import pyautogui
import sys
import os
import keyboard
import threading

# WIN フォルダのパスを取得し、Python パスに追加
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import config.config_japanhd2 as config

########################設定#####################
bin_count = 204
start_bin = 204
secound_auto = 3
################################################

# 停止フラグ
stop_flag = False

# キーボード入力を監視するスレッド
def monitor_keyboard():
    global stop_flag
    while not stop_flag:
        if keyboard.is_pressed("esc"):
            print("ESCキーが押されたためスクリプトを停止します。")
            stop_flag = True
            break

# キーボード監視スレッドの開始
keyboard_thread = threading.Thread(target=monitor_keyboard)
keyboard_thread.start()

resolve = dvr.scriptapp("Resolve")
project_manager = resolve.GetProjectManager()
project = project_manager.LoadProject(config.project_name)

try:
    if project:
        print(f"'{config.project_name}' プロジェクトがロードされました。")

        media_pool = project.GetMediaPool()
        root_folder = media_pool.GetRootFolder()

        if root_folder:
            print("ルートフォルダが正常に取得されました。")
            sub_folders = root_folder.GetSubFolders()

            for i in range(start_bin, bin_count + 1):
                if stop_flag:
                    sys.exit("スクリプトを停止しました。")

                bin_name = f"Bin_{i:03d}"
                bin_folder = None
                for folder in sub_folders.values():
                    if folder.GetName() == bin_name:
                        print(f"ビン '{bin_name}' が見つかりました。")
                        bin_folder = folder
                        break

                if not bin_folder:
                    print(f"ビン '{bin_name}' が見つかりませんでした。")
                    continue

                timeline = project.GetTimelineByIndex(i)
                if not timeline:
                    print(f"タイムライン '{bin_name}' が見つかりませんでした。")
                    continue
                else:
                    print("タイムラインが正常に取得されました。")

                project.SetCurrentTimeline(timeline)
                track_count = timeline.GetTrackCount("video")
                for track_index in range(1, track_count + 1):
                    if stop_flag:
                        sys.exit("スクリプトを停止しました。")

                    clips = timeline.GetItemListInTrack("video", track_index)
                    for clip in clips:
                        if stop_flag:
                            sys.exit("スクリプトを停止しました。")

                        clip.SetProperty("ZoomX", config.zoomx)
                        clip.SetProperty("ZoomY", config.zoomy)
                        clip.SetProperty("Pan", config.pan)
                        clip.SetProperty("Tilt", config.tilt)
                        print(f"クリップ '{clip.GetName()}' のズームと位置が変更されました。\n\n")

                        color_page = resolve.OpenPage('color')
                        if color_page:
                            print("カラーに移動しました")
                        else:
                            print("カラーに移動できません")

                        # pyautoguiでカーソル操作を自動化
                        pyautogui.moveTo(8059, 2414, duration=secound_auto)
                        pyautogui.click()
                        pyautogui.moveTo(8929, 2424, duration=secound_auto)
                        pyautogui.click()
                        pyautogui.write(config.cpan)
                        pyautogui.moveTo(9158, 2424, duration=secound_auto)
                        pyautogui.click()
                        pyautogui.write(config.ctilt)
                        pyautogui.moveTo(8950, 2575, duration=secound_auto)
                        pyautogui.click()
                        pyautogui.write('0')
                        pyautogui.press('\t')
                        pyautogui.press('\t')
                        pyautogui.write('0')
                        pyautogui.press('\t')
                        pyautogui.press('\t')
                        pyautogui.write('0')
                        pyautogui.press('\t')
                        pyautogui.press('\t')
                        pyautogui.write('0')
                        pyautogui.moveTo(9447, 1261, duration=secound_auto)
                        pyautogui.dragTo(8689, 1479, button='left', duration=secound_auto)
                        pyautogui.moveTo(9888, 1359, duration=secound_auto)
                        pyautogui.click()
                        pyautogui.write('0.7')
                        pyautogui.press('return')

                        back_edit = resolve.OpenPage('edit')
                        if back_edit:
                            print("エディットに戻りました")
                        else:
                            print("エディットに戻れません")

except Exception as e:
    print(f"エラーが発生しました: {e}")
