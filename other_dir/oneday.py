import os
import shutil

# 対象フォルダのパス
source_folder = r"H:\Lubed\movie"

# フォルダの連番初期値
folder_prefix = "mu-"
start_number = 1

# フォルダ内のすべてのmp4ファイルを取得
mp4_files = [f for f in os.listdir(source_folder) if f.endswith('.mp4')]

if not mp4_files:
    print("mp4ファイルが見つかりません。")
else:
    for index, file_name in enumerate(mp4_files, start=start_number):
        # 新しいフォルダ名を生成
        new_folder_name = f"{folder_prefix}{index:03}"  # 連番は3桁でゼロ埋め
        new_folder_path = os.path.join(source_folder, new_folder_name)
        
        # フォルダを作成
        os.makedirs(new_folder_path, exist_ok=True)
        
        # ファイルを移動
        source_file_path = os.path.join(source_folder, file_name)
        destination_file_path = os.path.join(new_folder_path, file_name)
        shutil.move(source_file_path, destination_file_path)
        
        print(f"{file_name} を {new_folder_name} フォルダに移動しました。")

    print("すべてのファイルが処理されました。")
