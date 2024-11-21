'''
propaty_change.py
指定したビンのタイムラインを取得してサイズなどのプロパティを変更する。クリップは結合しなくても変更できる。
作業手順5
'''

import DaVinciResolveScript as dvr
import pyautogui



########################設定#####################
# プロジェクト名
project_name = "Project2"
#ビンの数の範囲
bin_count=21
start_bin=1
# 出力ディレクトリ
base_output_dir = "I:\davicitest"  # 出力先のフォルダを指定
#レンダリング開始位置
markln=20
#レンダリング終了位置
markout=20
################################################

# Resolve APIに接続
resolve = dvr.scriptapp("Resolve")
project_manager = resolve.GetProjectManager()

# プロジェクトを取得
project = project_manager.LoadProject(project_name)

if project:
    print(f"'{project_name}' プロジェクトがロードされました。")

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
                    clip.SetProperty("ZoomX", 1)  # 水平方向のズームを1.5倍に変更
                    clip.SetProperty("ZoomY", 1)  # 垂直方向のズームを1.5倍に変更

                    # 位置を変更
                    clip.SetProperty("Pan", -100)  # 水平方向に-100移動
                    clip.SetProperty("Tilt", 50)   # 垂直方向に50移動
        
                    print(f"クリップ '{clip.GetName()}' のズームと位置が変更されました。\n\n")

            color_page = resolve.OpenPage('color')

            for track_index in range(1, track_count + 1):
                clips = timeline.GetItemListInTrack("video", track_index)
        
                for clip in clips:
                    print(f"クリップ '{clip.GetName()}' に対してカラーグレーディングを実行します。")

                    # カラーノードにアクセス
                    node_graph = clip.GetNodeGraph()
                    if not node_graph:
                        print(f"クリップ '{clip.GetName()}' のノードグラフが見つかりませんでした。")
                        continue  # ノードがない場合は次のクリップへ

                    node_count = node_graph.GetNumNodes()
                    if node_count == 0:
                        print(f"クリップ '{clip.GetName()}' にノードが存在しません。")
                        continue  # ノードがない場合は次のクリップへ
            
                for node_index in range(1, node_count + 1):
                    node_label = node_graph.GetNodeLabel(node_index)
                    print(f"ノード '{node_label}' を処理中...")


                    

                print(f"ノード '{node_label}' のプロパティが変更されました。")
