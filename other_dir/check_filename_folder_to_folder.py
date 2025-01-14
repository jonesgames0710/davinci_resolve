'''
このスクリプトは、2つのディレクトリ階層（H:\base_movies\avz と F:\BIG_AVidoz）内に存在する全ファイル名を取得し、
それらを比較して「一方には存在するが、もう一方には存在しない」ファイル名を抽出するプログラムです。
さらに、特定の文字列（head）で始まるファイル名だけを対象にするフィルタリング機能を備えています。
'''

import os

def get_all_files(dir_path):
    """
    指定ディレクトリ以下のすべてのファイル名（basenameのみ）を取得する関数。
    """
    files = []
    for root, dirs, filenames in os.walk(dir_path):
        for f in filenames:
            # 拡張子がmp4のみを追加
            if f.lower().endswith('.mp4'):
                files.append(f)
    return files

def main():
    # 比較条件となる文字列（頭文字）
    head = ""  # 空文字("")なら全ファイル比較

    # ディレクトリの指定
    base_dir = r"K:\superma_fullpack"
    big_dir = r"X:\zremen2"
    output_file = os.path.join(base_dir, "missing_files.txt")

    # base_dir配下のファイル取得
    base_files = set(get_all_files(base_dir))

    # big_dir配下のファイル取得
    big_files = get_all_files(big_dir)

    # headが指定されている場合はフィルタリング
    if head:
        big_files = [f for f in big_files if f.startswith(head)]

    # base_dirに存在しないファイルを抽出
    missing_files = [f for f in big_files if f not in base_files]

    # missing_filesがあれば書き出し
    if missing_files:
        with open(output_file, 'w', encoding='utf-8') as f:
            for mf in missing_files:
                f.write(mf + '\n')
    else:
        print("missing fileはありません。")

if __name__ == "__main__":
    main()
