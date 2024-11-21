import os
import DaVinciResolveScript as dvr
import pprint

# Resolve APIに接続
resolve = dvr.scriptapp("Resolve")
project_manager = resolve.GetProjectManager()

# プロジェクト「Project2」を取得（add_bin_timeline.pyで指定されたプロジェクト名を確認）
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
        base_folder = "V:\JapanHD"

        # "mu-"で始まるフォルダを探す
        mu_folders = [f for f in os.listdir(base_folder) if f.startswith("mu-") and os.path.isdir(os.path.join(base_folder, f))]

        #pprint.pprint(mu_folders)
        mu_folders=sorted(mu_folders)
        #pprint.pprint(mu_folders)
        # ビンの名前順にソートされたリストを作成
        bins = sorted([f"Bin_{i:03d}" for i in range(1, 101)])

        #print(bins)

        # 各フォルダの中のmp4ファイルをビンに追加し、タイムラインに入れる
        for mu_folder, bin_name in zip(sorted(mu_folders), bins):
            mu_folder_path = os.path.join(base_folder, mu_folder)
            
            # mp4ファイルを探す
            mp4_files = [os.path.join(mu_folder_path, f) for f in os.listdir(mu_folder_path) if f.endswith(".mp4")]

            pprint.pprint(f"取得したファイル名：{mp4_files}")

            if mp4_files:
                # サブフォルダを取得
                sub_folders = root_folder.GetSubFolders()

                #pprint.pprint(sub_folders)
                for folder in sub_folders.values():
                    folder_name = folder.GetName()  # フォルダ名が取得できるか確認
                   # print(folder_name)

                

                bin_folder = None
                for folder in sub_folders.values():
                    pprint.pprint(folder)
                    if folder.GetName() == bin_name:
                        print(folder.GetName())
                        bin_folder = folder
                        pprint.pprint(bin_folder)
                        break

                if not bin_folder:
                    print(f"ビン '{bin_name}' が見つかりませんでした。")
                    continue
                
                mp4_file = '/Users/radmanesh/Desktop/davimp4/mu-001/sde125-koq1.mp4'
                print(f"mp4ファイル: {mp4_file}")
                print(f"ビンフォルダ: {bin_folder}")
                # mp4ファイルをビンに追加
                print(mp4_files)
                media_pool.ImportMedia([mp4_files])
                print(f"'{mu_folder}' のメディアが '{bin_name}' に追加されました。")

                # ビンに対応するタイムライン名を作成
                timeline_name = bin_name.replace("Bin_", "Timeline_")
                print(f"タイムライン名：{timeline_name}")
                # プロジェクト内のタイムラインの数を取得
                timeline_count = project.GetTimelineCount()

                timeline_name = bin_name.replace("Bin_", "Timeline_")
                timeline = None

                # タイムラインをすべて取得して、名前を確認
                for i in range(1, timeline_count + 1):
                    tl = project.GetTimelineByIndex(i)
                    if tl.GetName() == timeline_name:
                        timeline = tl
                        break

                if timeline:
                    print(f"'{timeline_name}' タイムラインが見つかりました。")
                else:
                    print(f"'{timeline_name}' タイムラインが見つかりませんでした。")

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