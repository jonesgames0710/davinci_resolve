import os
import shutil

# フォルダのパスを指定
base_path = r"H:\元動画\javhub\mike203"
output_file = os.path.join(base_path, "empty.txt")
empty_folder_destination = "H:\元動画\javhub\動画空フォルダ"

# 動画ファイルの拡張子リスト
video_extensions = {'.mp4', '.mkv', '.avi', '.mov'}

# 空フォルダリストを保持
empty_folders = []

# 動画空フォルダが存在しない場合は作成
if not os.path.exists(empty_folder_destination):
    os.makedirs(empty_folder_destination)

# サブフォルダを走査
for foldername, subfolders, filenames in os.walk(base_path):
    # 基本パスそのものは除外する
    if foldername == base_path:
        continue
    
    # 動画ファイルがあるか確認
    has_video = any(file.lower().endswith(tuple(video_extensions)) for file in filenames)
    
    # 動画ファイルがない場合、フォルダ名とパスを追加
    if not has_video:
        folder_name_only = os.path.basename(foldername)  # フォルダ名のみを取得
        empty_folders.append(f"{folder_name_only} - {foldername}")
        
        # 動画空フォルダに移動
        destination_path = os.path.join(empty_folder_destination, folder_name_only)
        shutil.move(foldername, destination_path)
        print(f"フォルダ '{foldername}' が '{destination_path}' に移動されました。")

# 結果をempty.txtに書き出す
with open(output_file, 'w', encoding='utf-8') as f:
    for folder in empty_folders:
        f.write(folder + '\n')

print(f"動画ファイルが入っていないフォルダの一覧が {output_file} に出力され、{empty_folder_destination} に移動されました。")
