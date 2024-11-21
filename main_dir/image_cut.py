from PIL import Image
import os

# 出力ディレクトリ
base_output_dir = r"H:\japanHD\mi.ke.sun1108+jiji"

# 切り取るJPEGファイルのディレクトリを再帰的に探索
for root, dirs, files in os.walk(base_output_dir):
    
    for file_name in files:
        
        if file_name.lower().endswith((".jpg", ".jpeg")):  # JPEGファイルに対して処理を行う
            file_path = os.path.join(root, file_name)
            print(f"Processing file: {file_path}")
            
            # 画像を開く
            try:
                img = Image.open(file_path)
            except Exception as e:
                print(f"Failed to open {file_path}: {e}")
                continue

            
            
            # 現在のサイズを取得
            width, height = img.size
            print(f"Image size: {width}x{height}")
            
            if width>1000:
                # 画像の左端から1000px幅に切り取る
                left = 0
                top = 0
                right = width
                bottom = height - 80
 
                # 切り取り処理
                cropped_img = img.crop((left, top, right, bottom))
                
                # 上書き保存
                cropped_img.save(file_path)
                
                print(f"{file_path} を切り取り、1000x720 にしました。")