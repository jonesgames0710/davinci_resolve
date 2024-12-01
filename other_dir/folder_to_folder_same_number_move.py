'''
タイムライン名のフォルダをフォルダからフォルダに移動する
'''
import os
import shutil
import re

# ベースフォルダパス
base_path = r"H:\uncensoredleaked"

# フォルダ名とフォルダ番号のパターン
source_folder_pattern = re.compile(r"Timeline_(\d+)_\w")  # 移動元フォルダ
destination_folder_pattern = re.compile(r"Render_Uncensored_Leaked-(\d+)")  # 移動先フォルダ

# ベースパス内のフォルダを取得
source_folders = []
destination_folders = []

for item in os.listdir(base_path):
    item_path = os.path.join(base_path, item)
    if os.path.isdir(item_path):
        # 移動元フォルダを取得
        source_match = source_folder_pattern.match(item)
        if source_match:
            source_folders.append((int(source_match.group(1)), item_path))
        else:
            print(f"Source folder does not match: {item}")
        # 移動先フォルダを取得
        destination_match = destination_folder_pattern.match(item)
        if destination_match:
            destination_folders.append((int(destination_match.group(1)), item_path))
        else:
            print(f"Destination folder does not match: {item}")
    else:
        print(f"Not a directory: {item}")

# フォルダ番号が一致するものを移動
for source_number, source_path in source_folders:
    for dest_number, dest_path in destination_folders:
        if source_number == dest_number:
            try:
                shutil.move(source_path, dest_path)
                print(f"Moved: {source_path} -> {dest_path}")
            except Exception as e:
                print(f"Error moving {source_path} -> {dest_path}: {e}")
