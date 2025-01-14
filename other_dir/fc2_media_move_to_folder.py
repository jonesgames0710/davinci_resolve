'''
FC2のファイルにある7桁の番号を検出して新規にフォルダを作成して同じ7桁のファイル名を同じフォルダにいれる
'''

import os
import re

# 対象のディレクトリ
source_dir = r"D:\\ダウンロード\\fc2\\fc2"

# 新規フォルダのベース名
folder_base_name = "mu-"

# ファイル名から7桁の数字を抽出する正規表現
pattern = re.compile(r"\d{7}")

# フォルダ作成とファイル移動処理
def organize_videos():
    if not os.path.exists(source_dir):
        print("指定されたディレクトリが存在しません。")
        return

    # 動画ファイルをループ
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)

        # ファイルかどうかを確認
        if os.path.isfile(file_path):
            # ファイル名から7桁の数字を抽出
            match = pattern.search(file_name)
            if match:
                number = match.group()
                
                # 新しいフォルダ名
                folder_name = f"{folder_base_name}{number}"
                folder_path = os.path.join(source_dir, folder_name)

                # フォルダが存在しない場合は作成
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # ファイルをフォルダに移動
                new_file_path = os.path.join(folder_path, file_name)
                os.rename(file_path, new_file_path)
                print(f"{file_name} を {folder_name} に移動しました。")

if __name__ == "__main__":
    organize_videos()
