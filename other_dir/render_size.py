import os

# 基本のディレクトリ設定
base_dir = "I:\japanHD-render"
output_file = os.path.join(base_dir, "video_2gb.txt")

# 2GB以上の動画ファイルがあるフォルダ名を保存するリスト
video_2gb = []

# ファイルサイズのチェック (2GB = 2 * 1024 * 1024 * 1024 bytes)
size_threshold = 2 * 1024 * 1024 * 1024

# 指定されたディレクトリ内を再帰的にチェック
for root, dirs, files in os.walk(base_dir):
    for file_name in files:
        if file_name.endswith(('.mp4', '.mov', '.avi')):  # 必要なら他の動画形式を追加
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)

            if file_size >= size_threshold:
                # 動画ファイルが2GB以上なら、親フォルダ名を配列に追加
                folder_name = os.path.basename(root)
                if folder_name not in video_2gb:
                    video_2gb.append(folder_name)
                    
# 配列をアルファベット順にソート
video_2gb.sort()

# 結果をテキストファイルに書き出す
with open(output_file, 'w') as f:
    for folder in video_2gb:
        f.write(f"{folder}\n")

print(f"{len(video_2gb)} 個のフォルダが2GB以上の動画を含んでいます。結果は {output_file} に保存されました。")