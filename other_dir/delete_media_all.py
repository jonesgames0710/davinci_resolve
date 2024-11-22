'''
すべてのビンの中にあるすべてのメディアファイルを削除
作業手順：削除
'''

import DaVinciResolveScript as dvr

# Resolve APIに接続
resolve = dvr.scriptapp("Resolve")
project_manager = resolve.GetProjectManager()

# プロジェクト「Project2」を取得
project_name = "Uncensored_Leaked"
project = project_manager.LoadProject(project_name)

if project:
    print(f"'{project_name}' プロジェクトがロードされました。")

    # メディアプールオブジェクトを取得
    media_pool = project.GetMediaPool()
    root_folder = media_pool.GetRootFolder()

    if root_folder:
        print("ルートフォルダが正常に取得されました。")
        
        # マスタービン内のすべてのサブフォルダ（ビン）を取得
        sub_folders = root_folder.GetSubFolderList()

        for folder in sub_folders:
            folder_name = folder.GetName()
            print(f"ビン '{folder_name}' の中のメディアを削除中...")

            # 各ビンの中のクリップを取得
            clips = folder.GetClipList()

            if clips:
                # クリップを削除
                media_pool.DeleteClips(clips)
                print(f"ビン '{folder_name}' のすべてのクリップが削除されました。\n\n")
            else:
                print(f"ビン '{folder_name}' にはクリップがありません。\n\n")
    else:
        print("マスタービンにアクセスできませんでした。\n\n")
else:
    print(f"'{project_name}' プロジェクトをロードできませんでした。\n\n")