'''
deliver_add_folder.py
still_image.py

'''
#########################設定#####################
# プロジェクト名
project_name = "javhub"
# 出力ディレクトリ
#base_output_dir = "/Users/radmanesh/Desktop/davinci_render"  # 出力先のフォルダを指定
base_output_dir=r"H:\javhub3"
#フォルダパス  フォルダ番号を除いたパス　番号は001のゼロ埋めで統一
#folder_path="/Users/radmanesh/Desktop/davimp4/mu-"
folder_path=r"H:\base_movies\javhub\mu-"
# 新規で作成するフォルダーの名前
new_folder_name = "Render_javhub3"  # 新しいフォルダの名前
#toomany_importとzero_importを書き出すフォルダパス
text_path="H:\javhub3"
#レンダリング開始位置
markln=270
#レンダリング終了位置
markout=270
#ファイル名の接頭辞 
filePrefix="javhub3"
#ズーム設定
zoomx=1.127 # 水平方向のズーム
zoomy=1.127 # 垂直方向のズーム
# 位置を変更
pan=70 # 水平方向
tilt=-43 # 垂直方向

#「座標」を入力
cpan='57.62'
#「座標」を入力
ctilt='44.40'
#ソフトネス　ソフト１をクリック
################################################


'''
2024/12/11 "D:\javhub2" markln=270 markout=270 target_size_mb = 1800 一回目のoverの再書き出し分
2024/12/20 "D:\javhub3" markln=270 markout=270 target_size_mb = 1750 さらに拡大してモザイクを削除　変更前数値　zoomx=1.058 zoomy=1.058 pan=30 tilt=-18 
'''


