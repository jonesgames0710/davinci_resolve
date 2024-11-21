import os
import DaVinciResolveScript as dvr
import pprint

# Resolve APIに接続
resolve = dvr.scriptapp("Resolve")
project_manager = resolve.GetProjectManager()

# プロジェクト「Project2」を取得
project_name = "Project2"
project = project_manager.LoadProject(project_name)

if project:
    print(f"'{project_name}' プロジェクトがロードされました。")

    # メディアプールオブジェクトのインスタンスを作成
    media_pool = project.GetMediaPool()
    root_folder = media_pool.GetRootFolder()

    if root_folder:
        print("ルートフォルダが正常に取得されました。")
        
        # フォルダのパス
        base_folder = "/Users/radmanesh/Desktop/davimp4"

        # "mu-"で始まるフォルダを探す
        mu_folders = [f for f in os.listdir(base_folder) if f.startswith("mu-") and os.path.isdir(os.path.join(base_folder, f))]
        mu_folders = sorted(mu_folders)

        pprint.pprint(mu_folders)

        # ビンの名前順にソートされたリストを作成
        bins = sorted([f"Bin_{i:03d}" for i in range(1, 101)])

        pprint.pprint(bins)

        # 各フォルダの中のmp4ファイルをビンに追加し、タイムラインに入れる
        for mu_folder, bin_name in zip(sorted(mu_folders), bins):
            mu_folder_path = os.path.join(base_folder, mu_folder)
            print(f"★★★★★フォルダパス：{mu_folder_path}")

            # mp4ファイルを探す
            mp4_files = [os.path.join(mu_folder_path, f) for f in os.listdir(mu_folder_path) if f.endswith(".mp4")]

            if mp4_files:
                # サブフォルダを取得
                sub_folders = root_folder.GetSubFolders()
                pprint.pprint(sub_folders)

                # Bin_001 から Bin_100 のビンに対応するフォルダを取得
                bin_folder = sub_folders[bins.index(bin_name) + 1]  # ビンのインデックスに基づいてサブフォルダを取得
                print(bins.index(bin_name)+ 1)
                pprint.pprint(bin_folder)
                folder_name = bin_folder.GetName()  # フォルダの名前を取得
                print(f"フォルダ名: {folder_name}")

                # mp4ファイルをビンに追加
                print(f"'{mu_folder}' のメディアを '{bin_name}' に追加しています...")
                try:
                    media_pool.ImportMediaIntoFolder(bin_folder, mp4_files)
                    print(f"'{mu_folder}' のメディアが '{bin_name}' に追加されました。")
                except TypeError as e:
                    print(f"Error importing media to folder: {e}")

                # ビンに対応するタイムライン名を作成
                timeline_name = bin_name.replace("Bin_", "Timeline_")
                timeline = project.GetTimelineByName(timeline_name)

                if timeline:
                    # タイムラインにメディアを追加
                    media_items = bin_folder.GetClipList()
                    media_pool.AppendToTimeline([media_item for media_item in media_items])
                    print(f"'{timeline_name}' にメディアが追加されました。")
                else:
                    print(f"'{timeline_name}' タイムラインが見つかりませんでした。")
    else:
        print("マスタービンにアクセスできませんでした。")
else:
    print(f"'{project_name}' プロジェクトをロードできませんでした。")