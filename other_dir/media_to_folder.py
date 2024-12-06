'''
ダウンロードした動画をフォルだに一つづつ移動させる
'''

import os
import shutil

# 動画ファイルがあるフォルダと移動先のベースフォルダ
source_folder = r"D:\ダウンロード\10musume_all\モザイク必須元動画\上Mosaic"
destination_base_folder = r"D:\ダウンロード\10musume_all\10musume_mosaic_base_ue"

# フォルダを確認し、存在しない場合は作成
if not os.path.exists(destination_base_folder):
    os.makedirs(destination_base_folder)

# 指定されたフォルダ内の動画ファイル一覧を取得
video_files = [
    os.path.join(source_folder, f)
    for f in os.listdir(source_folder)
    if os.path.isfile(os.path.join(source_folder, f))
]

# 動画ファイルをファイルサイズでソート（大きい順）
video_files_sorted = sorted(video_files, key=lambda f: os.path.getsize(f), reverse=True)

# 移動処理
for idx, video_file in enumerate(video_files_sorted):
    folder_name = f"mu-{idx + 1:03}"  # フォルダ名をmu-001, mu-002...の形式にする
    destination_folder = os.path.join(destination_base_folder, folder_name)
    os.makedirs(destination_folder, exist_ok=True)  # フォルダを作成
    
    # 動画ファイルを移動
    destination_file_path = os.path.join(destination_folder, os.path.basename(video_file))
    shutil.move(video_file, destination_file_path)
    print(f"Moved {video_file} to {destination_file_path}")

print("すべての動画ファイルの移動が完了しました。")
