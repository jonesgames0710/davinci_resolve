'''
delete_drx.py
drxファイル削除用スクリプト
指定したフォルダパスの中のフォルダ全てに適応される。
'''
import os

# スチルをエクスポートした後、drxファイルを削除
folder_path = r"H:\japanHD"

# os.walkを使用してすべてのサブディレクトリを再帰的に処理
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith(".drx"):
            file_path = os.path.join(root, file_name)
            os.remove(file_path)
            print(f"{file_path} を削除しました。")