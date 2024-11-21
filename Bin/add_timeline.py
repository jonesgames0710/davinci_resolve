'''
ビンの数だけタイムラインを追加
'''
########################設定#####################
# プロジェクト名
project_name = "Project2"
#作成するビンの数
bin_count=201
################################################
import DaVinciResolveScript as dvr

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

        # Bin_001からBin_100までのビンにタイムラインを追加
        for i in range(1, bin_count):  # 1から100までの範囲でビンに対応するタイムラインを作成
            bin_name = f"Bin_{i:03d}"  # Bin_001, Bin_002,...Bin_100
            timeline_name = f"Timeline_{i:03d}"  # Timeline_001, Timeline_002,...Timeline_100

            # 該当するビンを探す
            sub_folders = root_folder.GetSubFolders()
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

            # タイムラインを追加
            new_timeline = media_pool.CreateEmptyTimeline(timeline_name)

            if new_timeline:
                print(f"タイムライン '{timeline_name}' が '{bin_name}' に正常に追加されました。")
            else:
                print(f"タイムライン '{timeline_name}' の作成に失敗しました。")
    else:
        print("ルートフォルダを取得できませんでした。")
else:
    print(f"'{project_name}' プロジェクトをロードできませんでした。")