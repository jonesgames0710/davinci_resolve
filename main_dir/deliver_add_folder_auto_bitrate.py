'''
deliver.py
指定したビンのタイムラインをレンダキューに追加してレンダーする。レンダリングの開始位置終了位置を設定できる。
作業手順:6
'''

import DaVinciResolveScript as dvr
import os
import sys
# WIN フォルダのパスを取得し、Python パスに追加
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import config.config_uncensored_leaked as config




########################設定#####################
# プロジェクト名
#project_name = "erito"
#ビンの数の範囲
bin_count=2
start_bin=1
# 出力ディレクトリ
#base_output_dir = "/Users/radmanesh/Desktop/davinci_render"  # 出力先のフォルダを指定
#base_output_dir="H:\erito"
# 新規で作成するフォルダーの名前
#new_folder_name = "RenderOutput"  # 新しいフォルダの名前
#レンダリング開始位置
#markln=20
#レンダリング終了位置
#markout=20
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
            
            # デリバーページに移行
            test = resolve.OpenPage("deliver")
            if timeline:
                print("移行が正常に行われました。\n\n")

            # 新規フォルダーを作成するパス（base_output_dirの中にフォルダー名を生成）
            new_folder_path = os.path.join(config.base_output_dir, f"{config.new_folder_name}-{i:03d}")
            
            #トップ画像用フォルダーを作成するパス（base_output_dirの中にフォルダー名を生成）
            header_folder_path=os.path.join(new_folder_path,f"header-{i:03d}")
            
            # 新規フォルダーを作成
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
                os.makedirs(header_folder_path)
                print(f"新規フォルダ '{new_folder_path}' が作成されました。")

            # 出力ファイルのパスを設定（ビン名を使用）
            output_path = os.path.join(new_folder_path, f"{bin_name}.mp4")

              # タイムラインの開始フレームと終了フレームを取得して確認
            start_frame = timeline.GetStartFrame()
            end_frame = timeline.GetEndFrame()

            #終了フレームからカットするフレーム数をマイナスしてセットするフレームを変数に代入
            markout_set=end_frame-config.markout

            print(f"マークアウト：{config.markout}")
            print(f"マークアウトセット：{markout_set}")

                    # 動画の秒数を計算（フレーム数 ÷ フレームレート）
            fps = timeline.GetSetting("timelineFrameRate")
            duration_seconds = (end_frame - start_frame) / fps

            # 目標ファイルサイズに収めるためのビットレート計算（kbps）
            target_size_mb = 1900  # 目標サイズ 1.9GB (1900 MB)
            bitrate_kbps = (target_size_mb * 8192) / duration_seconds  # 8 bits/byte * 1024 kb/MB



            # レンダリング設定を行う
            project.SetRenderSettings({
                "TargetDir": new_folder_path,  # 出力ディレクトリ（新規フォルダ）
                "CustomName": "jd"+bin_name,        # ファイル名をビン名に設定
                "FormatWidth": 1280,           # 出力解像度（幅）
                "FormatHeight": 720,            # 出力解像度（高さ）
                "VideoQuality": int(bitrate_kbps),  # 計算されたビットレート
                #"MarkIn":config.markln,
                #"MarkOut":markout_set,         
            })

            print(f"タイムラインの開始フレーム: {start_frame}, 終了フレーム: {end_frame}")
            print(f"タイムラインの開始フレーム: {start_frame}, 終了フレーム: {end_frame}")
            print(f"ビットレート（kbps）: {int(bitrate_kbps)}")
            # レンダーキューに追加
            project.AddRenderJob()

        # 全てのジョブがキューに追加されたのでレンダリング開始
        #startrem = project.StartRendering()
        #if startrem:
            #print("レンダーが行われます。\n\n")

        
            

else:
    print(f"'{config.project_name}' プロジェクトをロードできませんでした。")