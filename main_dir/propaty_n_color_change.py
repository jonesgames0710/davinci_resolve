'''
指定したビンのタイムラインを取得してサイズなどのプロパティを変更する。クリップは結合しなくても変更できる。
カラーグレーディングをpyautofuiモジュールでウィンドウを追加してエフェクトのブラーを適応させる
作業手順5-2
'''

import DaVinciResolveScript as dvr
import pyautogui
import sys
import os
# WIN フォルダのパスを取得し、Python パスに追加
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import config.config_10musume_mosaic_ue as config



########################設定#####################
# プロジェクト名
#project_name = "erito"
#ビンの数の範囲
bin_count=148
start_bin=81
# 出力ディレクトリ
#base_output_dir = "/Users/radmanesh/Desktop/davinci_render"  # 出力先のフォルダを指定
#base_output_dir="H:\erito"
#pysutoguiの実行秒数
secound_auto=0.4
################################################

# Resolve APIに接続
resolve = dvr.scriptapp("Resolve")
project_manager = resolve.GetProjectManager()

# プロジェクトを取得
project = project_manager.LoadProject(config.project_name)


try:
    # ここに操
    print("ここまでOK")
except Exception as e:
    print(f"エラーが発生しました: {e}")

if project:
    print(f"'{config.project_name}' プロジェクトがロードされました。")

    # メディアプールオブジェクトを取得
    media_pool = project.GetMediaPool()
    root_folder = media_pool.GetRootFolder()

    if root_folder:
        print("ルートフォルダが正常に取得されました。")

        # サブフォルダを取得
        sub_folders = root_folder.GetSubFolders()

        # Bin_001からBin_010までを処理
        for i in range(start_bin, bin_count + 1):  # 1から10までの範囲で処理
            bin_name = f"Bin_{i:03d}"  # Bin_001, Bin_002,...Bin_010

            # 該当するビンを探す
            bin_folder = None
            for folder in sub_folders.values():
                if folder.GetName() == bin_name:
                    print(f"ビン '{bin_name}' が見つかりました。")
                    bin_folder = folder
                    break

            if not bin_folder:
                print(f"ビン '{bin_name}' が見つかりませんでした。")
                continue

            # タイムラインを取得※タイムライン生成時に生成順に割り振られるインデックス番号で取得する。
            timeline = project.GetTimelineByIndex(i)  # iでタイムラインを取得

            if not timeline:
                print(f"タイムライン '{bin_name}' が見つかりませんでした。")
                continue
            if timeline:
                 print("タイムラインが正常に取得されました。")
                

             # タイムラインを現在のタイムラインとして設定　※設定する位置がレンダリング設定をする位置より前にないとうまくいかない
            project.SetCurrentTimeline(timeline)

            # タイムライン内の全クリップを取得 
            track_count = timeline.GetTrackCount("video")
            for track_index in range(1, track_count + 1):
                #指定されたビデオトラック (track_index) 内のすべてのクリップ（アイテム）を取得します。 "video"という引数は、ビデオトラックからクリップを取得することを指定しています。
                clips = timeline.GetItemListInTrack("video", track_index)

                for clip in clips:
                # ズームを変更
                    clip.SetProperty("ZoomX", config.zoomx)  # 水平方向のズーム
                    clip.SetProperty("ZoomY", config.zoomy)  # 垂直方向のズーム

                    # 位置を変更
                    clip.SetProperty("Pan", config.pan)  # 水平方向
                    clip.SetProperty("Tilt", config.tilt)   # 垂直方向
        
                    print(f"クリップ '{clip.GetName()}' のズームと位置が変更されました。\n\n")

                    color_page = resolve.OpenPage('color')

                    if color_page:
                        print("カラーに移動しました")
                    else:
                        print("カラーに移動できません")

                    '''
                    ここの部分にpyautoguiでカーソル操作を自動化
                    '''
                    
                    #ウィンドウの四角形をクリック
                    #50 794
                    pyautogui.moveTo(8059,2414,duration=secound_auto)
                    pyautogui.click()


                     #変形「サイズ」をクリック
                    #480 795
                    pyautogui.moveTo(8936,2368,duration=secound_auto)
                    pyautogui.click()

                    #「サイズ」を入力
                    
                    pyautogui.write(config.size)

                    #変形「アスペクト」をクリック
                    
                    pyautogui.moveTo(9158,2379,duration=secound_auto)
                    pyautogui.click()
                    #「アスペクト」を入力
                    
                    pyautogui.write(config.aspect)

                    #変形「パン」をクリック
                    
                    pyautogui.moveTo(8929,2424,duration=secound_auto)
                    pyautogui.click()

                    #「座標」を入力
                    
                    pyautogui.write(config.cpan)

                    #変形「ティルト」をクリック
                   
                    pyautogui.moveTo(9158,2424,duration=secound_auto)
                    pyautogui.click()
                    #「座標」を入力
                    #44.50
                    pyautogui.write(config.ctilt)

                    #ソフトネス　ソフト１をクリック
                    #490 883
                    pyautogui.moveTo(8950,2575,duration=secound_auto)
                    pyautogui.click()

                    #「0」を入力
                    pyautogui.write('0')
                    pyautogui.press('\t')
                    pyautogui.press('\t')

                    #ソフトネス　ソフト２をクリック
                    #604 883
                    #pyautogui.moveTo(604,883,duration=secound_auto)
                    #pyautogui.click()

                    #「0」を入力
                    pyautogui.write('0')
                    pyautogui.press('\t')
                    pyautogui.press('\t')

                    #ソフトネス　ソフト３をクリック
                    #490 910
                    #pyautogui.moveTo(490,910,duration=secound_auto)
                    #pyautogui.click()

                    #「0」を入力
                    pyautogui.write('0')
                    pyautogui.press('\t')
                    pyautogui.press('\t')


                    #ソフトネス　ソフト４をクリック
                    #610 910
                    #pyautogui.moveTo(610,910,duration=secound_auto)
                    #pyautogui.click()

                    #「0」を入力
                    pyautogui.write('0')

                    #エフェクトのブラー(ガウス)からノードまでドラッグ
                    #950 180から660 260
                    pyautogui.moveTo(9447,1261,duration=secound_auto)
                    pyautogui.dragTo(8689,1479,button='left',duration=secound_auto)


                    #ブラー(ガウス)の強度をクリック
                    #1190 156
                    pyautogui.moveTo(9888,1359,duration=secound_auto)
                    pyautogui.click()

                    #「0,7」を入力
                    pyautogui.write('0.7')
                    pyautogui.press('return')
                    

                    back_edit=resolve.OpenPage('edit')
                    
                    if back_edit:
                        print("エディットに戻りました")
                    else:
                        print('エディットに戻れません')

                    

