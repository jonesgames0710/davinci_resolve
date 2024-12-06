'''
add_bin.py
作業手順１
指定された数のビンをマスタービンに追加
'''

import DaVinciResolveScript as dvr
import os
import sys
# WIN フォルダのパスを取得し、Python パスに追加
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import config.config_10musume_mosaic_sita as config

########################設定#####################
# プロジェクト名
#project_name = "erito"
#ビンの数の範囲
bin_count=34
start_bin=1
################################################
# Resolve APIに接続
resolve = dvr.scriptapp("Resolve")
project_manager = resolve.GetProjectManager()

# プロジェクトを取得
project = project_manager.LoadProject(config.project_name)

if project:
    print(f"'{config.project_name}' プロジェクトがロードされました。")

    # メディアプールオブジェクトを取得
    media_pool = project.GetMediaPool()
    root_folder = media_pool.GetRootFolder()

    if root_folder:
        print("ルートフォルダが正常に取得されました。")

        # Bin_001からBin_100までのビンを作成
        for i in range(start_bin, bin_count+1):  # 1から100までの範囲でビンを作成
            bin_name = f"Bin_{i:03d}"  # Bin_001, Bin_002,...Bin_100

            # 新規ビンを作成
            new_bin = media_pool.AddSubFolder(root_folder, bin_name)

            if new_bin:
                print(f"ビン '{bin_name}' が正常に作成されました。\n\n")
            else:
                print(f"ビン '{bin_name}' の作成に失敗しました。\n\n")
    else:
        print("ルートフォルダを取得できませんでした。\n\n")
else:
    print(f"'{config.project_name}' プロジェクトをロードできませんでした。\n\n")
