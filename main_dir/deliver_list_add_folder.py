'''
deliver_list_add_folder.py
配列で指定したビンのみをタイムラインをレンダキューに追加してレンダーする。レンダリングの開始位置終了位置を設定できる。
作業手順:6-2
'''

import DaVinciResolveScript as dvr
import os

########################設定#####################
# プロジェクト名
project_name = "erito"
#ビンの数の範囲
bin_count=10
start_bin=1
#ビンを指定して配列に代入
bin_list=["Bin_002"]
# 出力ディレクトリ
base_output_dir = "H:\erito"  # 出力先のフォルダを指定
# 新規で作成するフォルダーの名前
new_folder_name = "RenderOutput"  # 新しいフォルダの名前
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
        #bin_listの指定のビンを実行
        for list in bin_list:
            bin_name=list

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

            # bin_nameから番号を抽出してゼロ埋めされた文字列を整数に変換
            bin_number = bin_name.split("_")[-1]  # "Bin_003" -> "003"
            i = int(bin_number)  # "003" -> 3

            # タイムラインを取得※タイムライン生成時に生成順に割り振られるインデックス番号で取得する。
            timeline = project.GetTimelineByIndex(i)  # iでタイムラインを取得

            if not timeline:
                print(f"タイムライン '{bin_name}' が見つかりませんでした。")
                continue
            if timeline:
                 print("タイムラインが正常に取得されました。")

             # タイムラインを現在のタイムラインとして設定　※設定する位置がレンダリング設定をする位置より前にないとうまくいかない
            project.SetCurrentTimeline(timeline)
            
            # デリバーページに移行
            test = resolve.OpenPage("deliver")
            if timeline:
                print("移行が正常に行われました。\n\n")

            # 新規フォルダーを作成するパス（base_output_dirの中にフォルダー名を生成）
            new_folder_path = os.path.join(base_output_dir, f"{new_folder_name}-{i:03d}")
            
            #トップ画像用フォルダーを作成するパス（base_output_dirの中にフォルダー名を生成）
            header_folder_path=os.path.join(new_folder_path,f"header-{i:03d}")
            
            # 新規フォルダーを作成
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
                os.makedirs(header_folder_path)
                print(f"新規フォルダ '{new_folder_path}' が作成されました。")

            # 出力ファイルのパスを設定（ビン名を使用）
            output_path = os.path.join(new_folder_path, f"{bin_name}.mp4")

              # タイムラインの開始フレームと終了フレームを取得して確認
            start_frame = timeline.GetStartFrame()
            end_frame = timeline.GetEndFrame()

            #終了フレームからカットするフレーム数をマイナスしてセットするフレームを変数に代入
            markout_set=end_frame-markout

            print(f"マークアウト：{markout}")
            print(f"マークアウトセット：{markout_set}")



            # レンダリング設定を行う
            project.SetRenderSettings({
                "TargetDir": new_folder_path,  # 出力ディレクトリ（新規フォルダ）
                "CustomName": bin_name,        # ファイル名をビン名に設定
                "FormatWidth": 1280,           # 出力解像度（幅）
                "FormatHeight": 720,            # 出力解像度（高さ）
                #"MarkIn":markln,
                #"MarkOut":markout_set,         
            })

            print(f"タイムラインの開始フレーム: {start_frame}, 終了フレーム: {end_frame}")
            
            # レンダーキューに追加
            project.AddRenderJob()

        # 全てのジョブがキューに追加されたのでレンダリング開始
        startrem = project.StartRendering()
        if startrem:
            print("レンダーが行われます。\n\n")

        
            

else:
    print(f"'{project_name}' プロジェクトをロードできませんでした。")