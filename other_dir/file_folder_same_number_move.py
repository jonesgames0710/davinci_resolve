'''
フォルダ番号とファイル番号が一致するものを選定してファイルをフォルダに移動させる
'''

import os
import shutil
import re

# フォルダパスを指定
base_path = r"D:\ダウンロード\bukkake\bukkake_640"

# フォルダ名とファイル名のパターン
folder_pattern = re.compile(r"bukkake_640-(\d+)")
file_pattern = re.compile(r"ulTimeline_(\d+)_\w\.mp4")  # 最後のアルファベットを無視

# ベースパス内のフォルダとファイルを取得
folders = []
files = []

for item in os.listdir(base_path):
    item_path = os.path.join(base_path, item)
    if os.path.isdir(item_path):
        match = folder_pattern.match(item)
        if match:
            folders.append((int(match.group(1)), item_path))
    elif os.path.isfile(item_path):
        match = file_pattern.match(item)
        if match:
            files.append((int(match.group(1)), item_path))

# 番号の一致するファイルをフォルダに移動
for file_number, file_path in files:
    for folder_number, folder_path in folders:
        if file_number == folder_number:
            try:
                shutil.move(file_path, folder_path)
                print(f"Moved: {file_path} -> {folder_path}")
            except Exception as e:
                print
