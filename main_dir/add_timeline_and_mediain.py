'''
add_timeline_and_mediain.py.py
作業手順3
ビンの数だけタイムラインを追加
'''
########################設定#####################
# プロジェクト名
#project_name = "erito"
#ビンの数の範囲
bin_count=182
start_bin=1
################################################
import DaVinciResolveScript as dvr
import pprint
import re  # 正規表現を使うためにインポート
import sys
import os
# WIN フォルダのパスを取得し、Python パスに追加
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import config.config_uncensored_leaked as config

# Resolve APIに接続
resolve = dvr.scriptapp("Resolve")
project_manager = resolve.GetProjectManager()

# プロジェクトを取得
project = project_manager.LoadProject(config.project_name)

if project:
    print(f"'{config.project_name}' プロジェクトがロードされました。")

    # メディアプールオブジェクトを取得
    media_pool = project.GetMediaPool()
    root_folder = media_pool.GetRootFolder()

    if root_folder:
        print("ルートフォルダが正常に取得されました。")

        # Bin_001からBin_100までのビンにタイムラインを追加
        for i in range(start_bin, bin_count+1):  # 1から100までの範囲でビンに対応するタイムラインを作成
            bin_name = f"Bin_{i:03d}"  # Bin_001, Bin_002,...Bin_100
            timeline_name = f"Timeline_{i:03d}"  # Timeline_001, Timeline_002,...Timeline_100

            # 該当するビンを探す
            sub_folders = root_folder.GetSubFolders()
            bin_folder = None
            for folder in sub_folders.values():
                if folder.GetName() == bin_name:
                    print(f"ビン '{bin_name}' が見つかりました。")
                    bin_folder = folder
                    break

            if not bin_folder:
                print(f"ビン '{bin_name}' が見つかりませんでした。")
                continue
                     # ビンを現在のフォルダとして設定
            media_pool.SetCurrentFolder(bin_folder)

              # タイムラインにメディアを追加する準備
            media_items = bin_folder.GetClipList()



            #pprint.pprint(media_items)
            #for item in media_items:
                #print(item.GetName())
                #clip_lists.append({"object":item,"name":item.GetName()})

            

            #for ii in clip_lists:
                #print(ii)
                #print(f"Object: {ii['object']}, Name: {ii['name']}") 

                # 配列の宣言
            clip_lists = []

            # media_items からオブジェクトと名前を取得し、リストに辞書として追加
            for item in media_items:
                clip_lists.append({"object": item, "name": item.GetName()})
#########################################eの後の数字を取得してソートする関数####################################################
            # eの後の数字を取得してソートする関数
            '''
            def extract_number(clip):
                name = clip["name"]
                match = re.search(r'e(\d+)', name)  # 'e'に続く数字を探す
                if match:
                     return int(match.group(1))  # 数字部分を整数に変換して返す
                return float('inf')  # 数字がない場合は無限大を返す（ソートの際、末尾に移動）

                #      ソートを実行（eの後の数字が小さい順に並べる）
            clip_lists_sorted = sorted(clip_lists, key=extract_number)

                # ソートされたリストを出力
            for ii in clip_lists_sorted:
                print(f"Object: {ii['object']}, Name: {ii['name']}")

                # オブジェクトのみのリストを作成
            sorted_objects = [clip["object"] for clip in clip_lists_sorted]
            '''
#########################################eの後の数字を取得してソートする関数####################################################END

#########################################.mp4 の前の数字に基づいてクリップがソートする関数####################################################

            # ファイル名から.mp4の前の数字を取得してソートする関数
            def extract_number(clip):
                name = clip["name"]
                match = re.search(r'-(\d+)\.mp4$', name)  # '.mp4' の前の数字を探す
                if match:
                    return int(match.group(1))  # 数字部分を整数に変換して返す
                return float('inf')  # 数字がない場合は無限大を返す（ソートの際、末尾に移動）

            # ソートを実行（.mp4の前の数字が小さい順に並べる）
            clip_lists_sorted = sorted(clip_lists, key=extract_number)

            # ソートされたリストを出力
            for ii in clip_lists_sorted:
                print(f"Object: {ii['object']}, Name: {ii['name']}")

            # オブジェクトのみのリストを作成
            sorted_objects = [clip["object"] for clip in clip_lists_sorted]



#########################################.mp4 の前の数字に基づいてクリップがソートする関数####################################################




            # オブジェクトのみのリストを出力
            for obj in clip_lists_sorted:
             pprint.pprint(obj["object"])

         
            # タイムラインを追加
            new_timeline = media_pool.CreateTimelineFromClips(timeline_name,sorted_objects)

            if new_timeline:
                print(f"タイムライン '{timeline_name}' が '{bin_name}' に正常に追加されました。\n\n")
            else:
                print(f"タイムライン '{timeline_name}' の作成に失敗しました。\n\n")
            
    else:
        print("ルートフォルダを取得できませんでした。\n\n")
else:
    print(f"'{config.project_name}' プロジェクトをロードできませんでした。\n\n")