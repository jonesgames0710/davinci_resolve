'''
D:\ダウンロード\fc2\fc2フォルダ内の全てのフォルダの中で復数ファイルが入っているフォルダを探してテキストとしてD:\ダウンロード\fc2\fc2に書き出すコード
'''

import os

# 対象のディレクトリ
source_dir = r"D:\\ダウンロード\\fc2\\fc2"

# 出力ファイルのパス
output_file = os.path.join(source_dir, "folders_with_multiple_files.txt")

# フォルダをチェックして、複数ファイルが入っているフォルダを探す
def find_folders_with_multiple_files():
    if not os.path.exists(source_dir):
        print("指定されたディレクトリが存在しません。")
        return

    folders_with_multiple_files = []

    # ルートディレクトリ内のフォルダをループ
    for folder_name in os.listdir(source_dir):
        folder_path = os.path.join(source_dir, folder_name)

        # フォルダかどうかを確認
        if os.path.isdir(folder_path):
            # フォルダ内のファイルを取得
            files = os.listdir(folder_path)
            if len(files) > 1:  # ファイルが複数入っているか確認
                folders_with_multiple_files.append(folder_name)

    # 結果をファイルに書き出し
    with open(output_file, "w", encoding="utf-8") as f:
        for folder in folders_with_multiple_files:
            f.write(folder + "\n")

    print(f"複数ファイルが入っているフォルダのリストを {output_file} に書き出しました。")

if __name__ == "__main__":
    find_folders_with_multiple_files()
