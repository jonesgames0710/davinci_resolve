
'''
overの移動用スクリプト

特定のフォルダ内を検索
指定した文字列（例: "over"）を含むフォルダを探し、そのフォルダ名から番号を抽出します。

抽出した番号で別フォルダを検索
抽出した番号と一致するフォルダ名を別のフォルダ内で検索します。

該当フォルダを移動
条件に一致するフォルダを指定した移動先フォルダに移動します。


search_stringが空のときは検索先フォルダの全てのフォルダ名の番号をリストする。（保留用）


'''

import os
import shutil

# === 設定部分（変数） ===
# リストを作成する検索先フォルダ
source_folder = r"H:\javhub\UP\rurunakasotokita+aa\保留"
# 検索する文字列
search_string = ""
# リストを使ってフォルダ名を検索するフォルダ（移動するフォルダがある場所）
search_folder = r"H:\javhub3"
# リストに当てはまったフォルダ名の移動先フォルダ
destination_folder = r"H:\javhub3\rurunakasotokita+aa"

# === メインロジック ===

def extract_number_from_folder(folder_name):
    """
    フォルダ名から番号を抽出する関数。
    例: "Render_avidolz-111over" -> 111
    """
    return ''.join(filter(str.isdigit, folder_name))

# 1. リストを作成する
matching_numbers = []
for folder in os.listdir(source_folder):
    folder_path = os.path.join(source_folder, folder)
    if os.path.isdir(folder_path):
        if search_string:  # search_string が指定されている場合
            if search_string in folder:
                number = extract_number_from_folder(folder)
                if number:
                    matching_numbers.append(number)
        else:  # search_string が空の場合
            number = extract_number_from_folder(folder)
            if number:
                matching_numbers.append(number)

# 2. リストに該当するフォルダを検索して移動
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for folder in os.listdir(search_folder):
    folder_path = os.path.join(search_folder, folder)
    if os.path.isdir(folder_path):
        for number in matching_numbers:
            if number in folder:
                print(f"Moving folder: {folder}")
                shutil.move(folder_path, destination_folder)
                break

print("Operation completed.")
