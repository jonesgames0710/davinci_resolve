'''
media_import_all_folder.py
作業手順2
指定された数のビン（Bin_001からBin_100）に指定した数のフォルダ（mu_001からmu_010）からすべてのメディアファイルを取り込む
'''
import os
import DaVinciResolveScript as dvr
import pprint
from datetime import datetime
import sys
# WIN フォルダのパスを取得し、Python パスに追加
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import config.config_lubed as config



########################設定#####################
#ビンの数の範囲
bin_count=267
start_bin=1
#フォルダパス  フォルダ番号を除いたパス　番号は001のゼロ埋めで統一
#folder_path="/Users/radmanesh/Desktop/davimp4/mu-"
#folder_path="O:\erito\erito\mu-"
#動画数が3つ以上のビン番号を保存する配列の宣言
toomany_import=[]
#動画数が0のビン番号を保存する配列の宣言
zero_import=[]
#toomany_importとzero_importを書き出すフォルダパス
#text_path="O:\erito\erito"
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
        
        # サブフォルダを取得
        sub_folders = root_folder.GetSubFolders()

        # Bin_001からBin_010までを処理
        for i in range(start_bin, bin_count+1):  # 1から10までの範囲で処理
            bin_name = f"Bin_{i:03d}"  # Bin_001, Bin_002,...Bin_010
            media_folder = f"{config.folder_path}{i:03d}"  # mu-001, mu-002,...mu-010

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

            # メディアファイルを探す
            if os.path.exists(media_folder):
                media_files = [os.path.join(media_folder, f) for f in os.listdir(media_folder) if f.endswith(".mp4")]
                
                #インポートしたファイルが３以上のビン名をtoomany_import配列に追加
                if len(media_files)>2:
                    toomany_import.append(bin_name)

                if media_files:
                    print(f"次のメディアファイルが見つかりました: {media_files}")
                    # メディアをインポート
                    media_pool.ImportMedia(media_files)
                    print(f"'{media_folder}' のメディアが '{bin_name}' に追加されました。\n\n")
                else:
                    print(f"'{media_folder}' にはメディアファイルが見つかりませんでした。\n\n")
                    #zero_importにビン名を追加
                    zero_import.append(bin_name)
            else:
                print(f"'{media_folder}' フォルダが存在しません。\n\n")
    else:
        print("ルートフォルダを取得できませんでした。\n\n")
else:
    print(f"'{config.project_name}' プロジェクトをロードできませんでした。\n\n")
    
    
pprint.pprint(toomany_import)
pprint.pprint(zero_import)

# 現在の日時を取得（分まで）
now = datetime.now().strftime('%Y-%m-%d-%H-%M')


#toomany_impotの内容をテキストで書き出す
# テキストファイルに書き出す
with open(os.path.join(config.text_path,f"toomany_import_{now}.txt"), "w", encoding="utf-8") as file:
    for item in toomany_import:
        file.write(item + "\n")  # 各要素を1行ずつ書き込む
        
#zero_importの内容をテキストで書き出す 
with open(os.path.join(config.text_path,f"zero_import_{now}.txt"), "w", encoding="utf-8") as file:
    for item in zero_import:
        file.write(item + "\n")  # 各要素を1行ずつ書き込む

print("テキストファイルに書き出しました。")

