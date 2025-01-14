'''
フォルダ内の全てのフォルダの中に2つ以上ファイルがあるフォルダを移動するコード
'''

import os
import shutil

# 対象のディレクトリ
source_dir = r"D:\\ダウンロード\\fc2\\fc2"
uper2_dir = os.path.join(source_dir, "..", "uper2")

# uper2 フォルダを作成
if not os.path.exists(uper2_dir):
    os.makedirs(uper2_dir)

# フォルダを移動する処理
def move_folders_with_multiple_files():
    if not os.path.exists(source_dir):
        print("指定されたディレクトリが存在しません。")
        return

    # ルートディレクトリ内のフォルダをループ
    for folder_name in os.listdir(source_dir):
        folder_path = os.path.join(source_dir, folder_name)

        # フォルダかどうかを確認
        if os.path.isdir(folder_path):
            # フォルダ内のファイルを取得
            files = os.listdir(folder_path)
            if len(files) >= 2:  # ファイルが2つ以上入っているか確認
                new_folder_path = os.path.join(uper2_dir, folder_name)
                shutil.move(folder_path, new_folder_path)  # フォルダを移動
                print(f"{folder_name} を {uper2_dir} に移動しました。")

if __name__ == "__main__":
    move_folders_with_multiple_files()
