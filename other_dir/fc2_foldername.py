'''
D:\ダウンロード\fc2\fc2フォルダ内の全てのフォルダのフォルダ名をmu-連番に変更。連番は001から始まる（mu-001のつぎはmu-002）。
ただし番号の順番はフォルダサイズの大きい順となる。
'''

import os

# 対象のディレクトリ
source_dir = r"D:\\ダウンロード\\fc2\\fc2"

# 新しいフォルダ名のベース
folder_base_name = "mu-"

# フォルダ名を連番に変更する
# サイズの大きい順にソート

def rename_folders_by_size():
    if not os.path.exists(source_dir):
        print("指定されたディレクトリが存在しません。")
        return

    # フォルダごとのサイズを計算
    folder_sizes = []

    for folder_name in os.listdir(source_dir):
        folder_path = os.path.join(source_dir, folder_name)

        if os.path.isdir(folder_path):
            # フォルダのサイズを取得
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    if os.path.isfile(file_path):
                        total_size += os.path.getsize(file_path)
            folder_sizes.append((folder_name, total_size))

    # サイズの大きい順にソート
    folder_sizes.sort(key=lambda x: x[1], reverse=True)

    # フォルダ名を連番でリネーム
    counter = 1
    for folder_name, _ in folder_sizes:
        old_folder_path = os.path.join(source_dir, folder_name)
        new_folder_name = f"{folder_base_name}{counter:03d}"
        new_folder_path = os.path.join(source_dir, new_folder_name)

        # 名前を変更
        os.rename(old_folder_path, new_folder_path)
        print(f"{folder_name} を {new_folder_name} にリネームしました。")

        counter += 1

if __name__ == "__main__":
    rename_folders_by_size()
