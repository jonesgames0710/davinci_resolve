
'''
指定されたビンに指定したフォルダからすべてのメディアファイルを取り込む
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

    # メディアプールオブジェクトのインスタンスを作成
    media_pool = project.GetMediaPool()
    root_folder = media_pool.GetRootFolder()

    if root_folder:
        print("ルートフォルダが正常に取得されました。")
        
        # "Bin_001" のビンを探す
        sub_folders = root_folder.GetSubFolderList()
        bin_folder = None

        for folder in sub_folders:
            if folder.GetName() == "Bin_001":
                bin_folder = folder
                print(f"ビン '{folder.GetName()}' が見つかりました。")
                break
        
        if not bin_folder:
            print("ビン 'Bin_001' が見つかりませんでした。")
            exit()

        # 取り込むメディアファイルが入っているフォルダ
        media_folder_path = "/Users/radmanesh/Desktop/davimp4/mu-001"

        # フォルダ内のすべての .mp4 ファイルを取得
        media_files = [os.path.join(media_folder_path, f) for f in os.listdir(media_folder_path) if f.endswith(".mp4")]

        if not media_files:
            print("メディアファイルが見つかりませんでした。")
            exit()

        print(f"次のメディアファイルが見つかりました: {media_files}")

        # メディアファイルをビンにインポート
        media_pool.ImportMedia(media_files)
        print(f"{len(media_files)} 件のメディアファイルがビン 'Bin_001' に追加されました。")
    else:
        print("マスタービンにアクセスできませんでした。")
else:
    print(f"'{project_name}' プロジェクトをロードできませんでした。")