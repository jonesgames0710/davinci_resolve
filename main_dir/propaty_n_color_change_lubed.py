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
import config.config_lubed as config



########################設定#####################
# プロジェクト名
#project_name = "erito"
#ビンの数の範囲
bin_count=267
start_bin=1
# 出力ディレクトリ
#base_output_dir = "/Users/radmanesh/Desktop/davinci_render"  # 出力先のフォルダを指定
#base_output_dir="H:\erito"
#pysutoguiの実行秒数
secound_auto=0
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

                  
        
                    print(f"クリップ '{clip.GetName()}' のズームと位置が変更されました。\n\n")


                    

