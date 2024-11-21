'''
clip_join.py
作業手順4
タイムライン上のクリップを結合する。
'''
import DaVinciResolveScript as dvr
import pprint
import os
import sys
# WIN フォルダのパスを取得し、Python パスに追加
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import config.config_avidolz as config

########################設定#####################
# プロジェクト名
#project_name = "japanHD2"
#ビンの数の範囲
bin_count=186
start_bin=1
################################################

# Resolve APIに接続
resolve = dvr.scriptapp("Resolve")
project_manager = resolve.GetProjectManager()

# プロジェクトを取得
project = project_manager.LoadProject(config.project_name)

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
        for i in range(start_bin, bin_count+1):  # 1から10までの範囲で処理
            bin_name = f"Bin_{i:03d}"  # Bin_001, Bin_002,...Bin_010
            

            # 該当するビンを探す
            bin_folder = None
            for folder in sub_folders.values():
                if folder.GetName() == bin_name:
                    print(f"ビン '{bin_name}' が見つかりました。")
                    bin_folder = folder
                    break

            # ビン名から番号部分を抽出して整数に変換
            bin_num = int(bin_name.split('_')[1])
            print(f"ビン番号（整数）は {bin_num} です。")

            


            if not bin_folder:
                print(f"ビン '{bin_name}' が見つかりませんでした。")
                continue

            # ビンを現在のフォルダとして設定
            media_pool.SetCurrentFolder(bin_folder)

            num=project.GetTimelineCount()
            print(num)

            #タイムラインの
            
            # タイムラインを取得 タイムラインはビンが100からでもタイムラインのインデックスは1から始まるのでビンの作成、動画のインポート、タイムラインの作成は途中からはできない。途中からはビン番号とタイムラインインデックスが違う値になる。
            timeline = project.GetTimelineByIndex(bin_num)

            # タイムラインが存在するか確認
            if not timeline:
                print(f"タイムライン '{bin_name}' が取得できませんでした。")

            if timeline:
                 print("タイムラインが正常に取得されました。")
            
                 # タイムライン内のクリップを取得
            timeline_clips = timeline.GetItemsInTrack('video', 1)  # トラック1のビデオクリップを取得
            print(f"タイムライン上のクリップ数: {len(timeline_clips)}")

            if timeline_clips:
                # クリップをコンパウンドクリップとして結合する
                new_compound_clip = timeline.CreateCompoundClip(timeline_clips, {"name": "Compound Clip 1"})
            
            if new_compound_clip:
                print("クリップが正常にコンパウンドクリップに結合されました。\n\n")
            else:
                print("コンパウンドクリップの作成に失敗しました。\n\n")
            
        else:
            print("タイムライン上にクリップが見つかりませんでした。\n\n")
    else:
        print("タイムラインを取得できませんでした。\n\n")
else:
    print(f"'{config.project_name}' プロジェクトをロードできませんでした。\n\n")