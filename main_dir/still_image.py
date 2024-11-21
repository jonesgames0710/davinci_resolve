'''
still_image.py
スチルを保存してdeliver_add_folderで作成したフォルダに書き出す。
その後,base_output_dir内のフォルダのすべてのdrxファイルを削除
作業手順7
'''

import DaVinciResolveScript as dvr
import os
import pprint
import sys
# WIN フォルダのパスを取得し、Python パスに追加
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import config.config_japanhd2 as config

########################設定#####################
# プロジェクト名
#project_name = "japanHD2"
#ビンの数の範囲
bin_count=764
start_bin=704
# 出力ディレクトリ
#base_output_dir = "I:\japanHD-render"
#ファイル名の接頭辞 
#filePrefix="erito"
#ギャラリー保存のフォーマット
format="jpg";
#new_folder_name = "RenderOutput"
#保存間隔のフレーム数：5分までの値　200で6.6秒
save_interval_frame_befor = 200  
#保存間隔のフレーム数：5分以降の値
save_interval_frame_after = 2200
#フレームレート
frame_rate = 30  # 必要に応じてフレームレートを取得
################################################

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

        # サブフォルダを取得
        sub_folders = root_folder.GetSubFolders()

        # Bin_001からBin_010までを処理
        for i in range(start_bin, bin_count + 1):  # 1から10までの範囲で処理
            bin_name = f"Bin_{i:03d}"  # Bin_001, Bin_002,...Bin_010

            # 該当するビンを探す
            bin_folder = None
            for folder in sub_folders.values():
                if folder.GetName() == bin_name:
                    print(f"ビン '{bin_name}' が見つかりました。")
                    bin_folder = folder
                    break

            if not bin_folder:
                print(f"ビン '{bin_name}' が見つかりませんでした。")
                continue

            # タイムラインを取得
            timeline = project.GetTimelineByIndex(i)

            if not timeline:
                print(f"タイムライン '{bin_name}' が見つかりませんでした。")
                continue
            print("タイムラインが正常に取得されました。")

            # タイムラインを現在のタイムラインとして設定
            project.SetCurrentTimeline(timeline)
            
             # タイムラインの総フレーム数と
            total_frames = timeline.GetEndFrame()
            
            print(total_frames)
            
            frame_rate = 30  # 必要に応じてフレームレートを取得

            # タイムコードに変換
            def frames_to_timecode(total_frames, frame_rate):
                total_seconds = total_frames / frame_rate
                minutes = int(total_seconds // 60)
                seconds = int(total_seconds % 60)
                frames = int((total_seconds - (minutes * 60 + seconds)) * frame_rate)
                return f"00:{minutes:02}:{seconds:02}:{frames:02}"

            # 変数max_framesに代入
            max_timecode = frames_to_timecode(total_frames, frame_rate)
            
            print(f"最大タイムコード：{max_timecode}\n")
            
            
            
            #カウントフレーム変数
            count_frame=20
            
            stills=[]
            #カウントフレーム20からスタートしてsave_interval_frame_beforを代入、5分(9000)経過したらsave_interval_frame_after
            while total_frames>count_frame:
                print(f"カウントフレーム：{count_frame}")
                print(f"タイムコード：{frames_to_timecode(count_frame,frame_rate)}")

                if count_frame<9000:
                    count_frame+=save_interval_frame_befor
                else:
                    count_frame+=save_interval_frame_after
                
                #指定されたタイムコードをプレイヘッドの現在位置に設定
                timeline.SetCurrentTimecode(frames_to_timecode(count_frame,frame_rate))
                
                still=timeline.GrabStill()
                
                if still:
                    stills.append(still)
                    print(f"{still}が保存されました")
                
                
            else:
                print("すべての処理が終了しました。")
                
            
            
            if stills:
                print('スチルを取得しました。')
                pprint.pprint(stills)
                
            #プロジェクトオブジェクトでギャラリーオブジェクトを取得
            gralley=project.GetGallery()
            #GalleryStillAlbum オブジェクトのリストを取得
            gralley_tillAlbum=gralley.GetCurrentStillAlbum()
            
            if gralley_tillAlbum:
                print("gralley_tillAlbumは真")
            
            pprint.pprint(gralley_tillAlbum)
            
            
            #GalleryStill オブジェクトのリストを取得
            GalleryStill=gralley_tillAlbum.GetStills()
            
            if GalleryStill:
                print("GalleryStillは真")
            
            pprint.pprint(GalleryStill)
            
            # 保存先のパスdeliver_add_folder.pyで指定したもの（base_output_dirの中にフォルダー名を生成）
            folder_path = os.path.join(config.base_output_dir, f"{config.new_folder_name}-{i:03d}")
            
            save_folder_bool=gralley_tillAlbum.ExportStills(GalleryStill,folder_path,config.filePrefix,format)
            
            if save_folder_bool:
                print("アルバムの削除を行います")
                delete_album=gralley_tillAlbum.DeleteStills(GalleryStill) 
                
                if delete_album:
                    print("アルバムが削除されました。")
                
                
                
     #drxファイルの削除
     # スチルをエクスポートした後、drxファイルを削除
    # os.walkを使用してすべてのサブディレクトリを再帰的に処理
    for root, dirs, files in os.walk(config.base_output_dir):
        for file_name in files:
            if file_name.endswith(".drx"):
                file_path = os.path.join(root, file_name)
                os.remove(file_path)
                print(f"{file_path} を削除しました。")       
            
            

            
            
            
            
           
            
