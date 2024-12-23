'''
動画ファイルを新規でフォルダ（mu-001）を作って移動させる
'''


import os
import shutil

# 動画ファイルがあるフォルダパス
source_folder = r"D:\ダウンロード\1pondo_all\1pondo_omni"

# フォルダ内のファイルを取得
files = [f for f in os.listdir(source_folder) if f.endswith('.mp4')]

# 連番用のカウント
counter = 1

for file_name in files:
    # フォルダ名を作成 (例: mu-001)
    folder_name = f"mu-{counter:03}"
    new_folder_path = os.path.join(source_folder, folder_name)
    
    # フォルダ作成
    os.makedirs(new_folder_path, exist_ok=True)
    
    # ファイルの元のパスと移動先パス
    source_path = os.path.join(source_folder, file_name)
    destination_path = os.path.join(new_folder_path, file_name)
    
    # ファイルを新規フォルダに移動
    shutil.move(source_path, destination_path)
    
    # カウンタを1増やす
    counter += 1

print("ファイルの移動が完了しました！")
