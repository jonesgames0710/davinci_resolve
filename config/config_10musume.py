'''
deliver_add_folder.py
still_image.py

'''
#########################設定#####################
# プロジェクト名
project_name = "10musume"
# 出力ディレクトリ
#base_output_dir = "/Users/radmanesh/Desktop/davinci_render"  # 出力先のフォルダを指定
base_output_dir=r"D:\ダウンロード\10musume_all\10musume"
#フォルダパス  フォルダ番号を除いたパス　番号は001のゼロ埋めで統一
#folder_path="/Users/radmanesh/Desktop/davimp4/mu-"
folder_path=r"D:\ダウンロード\10musume_all\10musume_base\mu-"
# 新規で作成するフォルダーの名前
new_folder_name = "Render_10musume"  # 新しいフォルダの名前
#toomany_importとzero_importを書き出すフォルダパス
text_path=r"D:\ダウンロード\10musume_all\10musume"
#レンダリング開始位置
markln=1200
#レンダリング終了位置
markout=270
#ファイル名の接頭辞 
filePrefix="10musume"
#ズーム設定
zoomx=1.025 # 水平方向のズーム
zoomy=1.025 # 垂直方向のズーム
# 位置を変更
pan=8 # 水平方向
tilt=-4.5 # 垂直方向

#「座標」を入力
cpan='57.34'
#「座標」を入力
ctilt='44.48'
#ソフトネス　ソフト１をクリック
################################################

