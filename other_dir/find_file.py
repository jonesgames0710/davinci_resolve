import os
import pandas as pd

# フォルダパスの設定
folder1 = r"K:\ガチリーク2"
folder2 = r"K:\Uncensored_Leaked"
output_file = os.path.join(folder2, "mp4_file_comparison.xlsx")

# 指定フォルダ内のすべての .mp4 ファイル名を取得する関数
def get_mp4_files(folder_path):
    mp4_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.mp4'):
                mp4_files.append(file)
    return mp4_files

# フォルダごとに .mp4 ファイル名を取得
files_in_folder1 = get_mp4_files(folder1)
files_in_folder2 = get_mp4_files(folder2)

# リストの長さを揃えるために空白を追加
max_length = max(len(files_in_folder1), len(files_in_folder2))
files_in_folder1 += [""] * (max_length - len(files_in_folder1))
files_in_folder2 += [""] * (max_length - len(files_in_folder2))

# 共通のファイル名を探す
common_files = set(files_in_folder1).intersection(set(files_in_folder2))

# データフレームを作成
df = pd.DataFrame({
    "ガチリーク2のmp4ファイル": files_in_folder1,
    "Uncensored_Leakedのmp4ファイル": files_in_folder2
})

# 共通ファイルリストの列を追加
df_common = pd.DataFrame({"共通のmp4ファイル": list(common_files)})

# Excelファイルに書き出し
with pd.ExcelWriter(output_file) as writer:
    df.to_excel(writer, sheet_name="すべてのmp4ファイル", index=False)
    df_common.to_excel(writer, sheet_name="共通のmp4ファイル", index=False)

print(f"結果が {output_file} に書き出されました。")
