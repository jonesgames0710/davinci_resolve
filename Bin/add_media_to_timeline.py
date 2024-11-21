import os
import DaVinciResolveScript as dvr
import pprint

########################設定#####################
# プロジェクト名
project_name = "Project2"
# 処理するビンの数
bin_count = 10  # Bin_001からBin_100まで
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

        # Bin_001からBin_100までのビンを処理
        for i in range(1, bin_count):  # 1から100までの範囲で処理
            bin_name = f"Bin_{i:03d}"  # Bin_001, Bin_002,...Bin_100
            timeline_name = f"Timeline_{i:03d}"  # Timeline_001, Timeline_002,...Timeline_100

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
            # ビンを現在のフォルダとして設定
            media_pool.SetCurrentFolder(bin_folder)

            # タイムラインにメディアを追加する準備
            media_items = bin_folder.GetClipList()

           

            if media_items:
                # タイムラインにメディアを追加
                media_pool.AppendToTimeline(media_items)
                print(f"'{timeline_name}' にメディアが追加されました。")
            else:
                print(f"ビン '{bin_name}' にメディアが見つかりませんでした。")
    else:
        print("ルートフォルダを取得できませんでした。")
else:
    print(f"'{project_name}' プロジェクトをロードできませんでした。")