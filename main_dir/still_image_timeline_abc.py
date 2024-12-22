'''
still_image.pyを改造
タイムライン名でフォルダを作成してタイムラインのインデクスでループしてスチルを保存。
作業手順7
'''

import DaVinciResolveScript as dvr
import os
import pprint
import sys
# WIN フォルダのパスを取得し、Python パスに追加
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import config.config_bukkake_640 as config

########################設定#####################


#ギャラリー保存のフォーマット
format="jpg";

#保存間隔のフレーム数：5分までの値　200で6.6秒
save_interval_frame_befor = 600  
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
    timelinecount=project.GetTimelineCount()
    print(f"{timelinecount}")


    if root_folder:
        print("ルートフォルダが正常に取得されました。")

        # サブフォルダを取得
        sub_folders = root_folder.GetSubFolders()



         #タイムラインのインデクス番号ですべてのタイムラインをレンダーに追加する
        timelinecount=project.GetTimelineCount()

        for i in range(1,timelinecount+1):
            timeline=project.GetTimelineByIndex(i)
            print(timeline.GetName())
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

            
            
            # 保存先のパス　タイムライン名をフォルダ名にする
            folder_path = os.path.join(config.base_output_dir, f"{timeline.GetName()}")

                        # 新規フォルダーを作成
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"新規フォルダ '{folder_path}' が作成されました。")

            if not os.access(folder_path, os.W_OK):
                print(f"フォルダ '{folder_path}' に書き込み権限がありません。")

            
            save_folder_bool=gralley_tillAlbum.ExportStills(GalleryStill,folder_path,config.filePrefix,format)

            if save_folder_bool:
                print("保存成功")
            else:
                print("保存失敗")
            
            if save_folder_bool:
                print("アルバムの削除を行います")
                delete_album=gralley_tillAlbum.DeleteStills(GalleryStill) 
 
                
                if delete_album:
                    print("アルバムが削除されました。")
                
                
'''     
     #drxファイルの削除
     # スチルをエクスポートした後、drxファイルを削除
    # os.walkを使用してすべてのサブディレクトリを再帰的に処理
    for root, dirs, files in os.walk(config.base_output_dir):
        for file_name in files:
            if file_name.endswith(".drx"):
                file_path = os.path.join(root, file_name)
                os.remove(file_path)
                print(f"{file_path} を削除しました。")       
'''
            
            

            
            
            
            
           
            
