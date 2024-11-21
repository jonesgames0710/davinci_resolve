'''
deliver.py
指定したビンのタイムラインをレンダキューに追加してレンダーする
'''

import DaVinciResolveScript as dvr
import os

########################設定#####################
# プロジェクト名
project_name = "Project2"
# ビンの数
bin_count = 10
# 出力ディレクトリ
output_dir = "/Users/radmanesh/Desktop/davinci_render"  # 出力先のフォルダを指定
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
        for i in range(1, bin_count + 1):  # 1から10までの範囲で処理
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

            # タイムラインを取得
            timeline = project.GetTimelineByIndex(i)  # iでタイムラインを取得

            if not timeline:
                print(f"タイムライン '{bin_name}' が見つかりませんでした。")
                continue
            if timeline:
                 print("タイムラインが正常に取得されました。")
            

            # デリバーページに移行
            test=resolve.OpenPage("deliver")
            if timeline:
                print("移行が正常に行われました。\n\n")
            

            # 出力ファイルのパスを設定（ビン名を使用）
            output_path = os.path.join(output_dir, f"{bin_name}.mp4")

            # レンダリング設定を行う
            project.SetRenderSettings({
                "TargetDir": output_dir,  # 出力ディレクトリ
                "CustomName": bin_name,   # ファイル名をビン名に設定
                "FormatWidth": 1280,      # 出力解像度（幅）
                "FormatHeight": 720,     # 出力解像度（高さ）
            })

            # タイムラインを現在のタイムラインとして設定
            project.SetCurrentTimeline(timeline)

            # レンダーキューに追加
            project.AddRenderJob()

        # 全てのジョブがキューに追加されたのでレンダリング開始
        startrem=project.StartRendering()
        if startrem:
            print("レンダーが行われます。\n\n")
        

else:
    print(f"'{project_name}' プロジェクトをロードできませんでした。")