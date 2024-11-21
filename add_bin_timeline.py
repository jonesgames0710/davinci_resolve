import sys
import os
import DaVinciResolveScript as dvr


# Resolve APIに接続
resolve = dvr.scriptapp("Resolve")
project_manager = resolve.GetProjectManager()

# プロジェクト「Project2」を取得
project_name = "Project2"
project = project_manager.LoadProject(project_name)

if project:
    print(f"'{project_name}' プロジェクトがロードされました。")

    # タイムラインにアクセス（マスタービン）
    #　メディアプールオブジェクトのインスタンスを作成してメディアプールの操作をできるようにする
    media_pool= project.GetMediaPool()
    # メディアプールのルートフォルダオブジェクトを取得し、root_folderに格納する
    # ルートフォルダはメディアプール内の最上位のフォルダで、そこからサブフォルダやクリップにアクセスできる
    root_folder=media_pool.GetRootFolder()

        #タイムラインの設定
    timeline_settings = { }

    if root_folder:
        # 100個のビンを連番で作成
        for i in range(1, 101):
            bin_name = f"Bin_{i:03d}"  # 連番でビンの名前を作成 (例: Bin_001, Bin_002, ...)
            project.GetMediaPool().AddSubFolder(root_folder, bin_name)
            print(f"'{bin_name}' を作成しました。")

            
                
                # タイムライン名を連番で作成
            timeline_name = f"Timeline_{i:03d}"

                # 指定した名前で空のタイムラインをメディアプールに作成し、そのタイムラインオブジェクトを取得する
                # タイムラインは最初は空で、クリップやトラックは含まれていない
            timeline=media_pool.CreateEmptyTimeline(timeline_name)

            if timeline:
                print(f"'{timeline_name}':タイムラインを'{bin_name}'に作成しました")
            else:
                print(f"'{timeline_name}'タイムラインの作成に失敗しました")
         

          

    else:
        print("マスタービンにアクセスできませんでした。")
else:
    print(f"'{project_name}' プロジェクトをロードできませんでした。")
