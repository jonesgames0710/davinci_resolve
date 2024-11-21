
'''
指定された数のビンに指定したフォルダからすべてのメディアファイルを取り込む
'''
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

    # メディアプールオブジェクトのインスタンスを作成してメディアプールの操作をできるようにする
    media_pool = project.GetMediaPool()
    root_folder = media_pool.GetRootFolder()

    if root_folder:
        print("ルートフォルダが正常に取得されました。")
        
        # フォルダのパス
        media_folder = "/Users/radmanesh/Desktop/davimp4/mu-001"

        # メディアファイルを探す
        media_files = [os.path.join(media_folder, f) for f in os.listdir(media_folder) if f.endswith(".mp4")]

        if media_files:
            print(f"次のメディアファイルが見つかりました: {media_files}")

            # ビンの名前を生成 (Bin_001 から Bin_100)
            bins = [f"Bin_{i:03d}" for i in range(1, 101)]

            # サブフォルダ（ビン）の取得
            sub_folders = root_folder.GetSubFolders()

            # 各ビンにメディアをインポート
            for bin_name in bins:
                bin_folder = None
                for folder in sub_folders.values():
                    if folder.GetName() == bin_name:
                        print(f"ビン '{bin_name}' が見つかりました。")
                        bin_folder = folder
                        break

                if not bin_folder:
                    print(f"ビン '{bin_name}' が見つかりません。スキップします。")
                    continue

                # ビンを現在のフォルダとして設定
                media_pool.SetCurrentFolder(bin_folder)

                # メディアをビンにインポート
                imported_items = media_pool.ImportMedia(media_files)

                if imported_items:
                    print(f"ビン '{bin_name}' にメディアが正常にインポートされました。")
                else:
                    print(f"ビン '{bin_name}' へのメディアのインポートに失敗しました。")
    else:
        print("マスタービンにアクセスできませんでした。")
else:
    print(f"'{project_name}' プロジェクトをロードできませんでした。")