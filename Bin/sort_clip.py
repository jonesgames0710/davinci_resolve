\
import os
import DaVinciResolveScript as dvr
import pprint
import re


########################設定#####################
# プロジェクト名
project_name = "Project2"
#ビンの数
bin_count=10
#フォルダパス  フォルダ番号を除いたパス　番号は001のゼロ埋めで統一
folder_path="/Users/radmanesh/Desktop/davimp4/mu-"
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
        for i in range(1, bin_count+1):  # 1から10までの範囲で処理
            bin_name = f"Bin_{i:03d}"  # Bin_001, Bin_002,...Bin_010
            media_folder = f"{folder_path}{i:03d}"  # mu-001, mu-002,...mu-010

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

            # ファイル名と対応するクリップを保管するためのリストを作成
            clips_with_numbers = []

            for item in media_items:
                file_name = item.GetName()
    
                # ファイル名から「e」以降の数字部分を抽出
            match = re.search(r'e(\d+)', file_name)  # 'e'に続く数字を探す正規表現
            if match:
                number = int(match.group(1))  # 数字部分を整数に変換
                clips_with_numbers.append((number, item))  # 数字と対応するクリップを保存

            # 数字部分でソート（数字が小さい順）
            sorted_clips = sorted(clips_with_numbers, key=lambda x: x[0])

            # ソート後のクリップを新しいリストとして作成    
            sorted_media_items = [clip for _, clip in sorted_clips]

            # ソートされたクリップのファイル名を確認
            for item in sorted_media_items:
                    print(f"ソートメディア：{item.GetName()}")