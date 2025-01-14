'''
deliver.py
指定したビンのタイムラインをレンダキューに追加してレンダーする。レンダリングの開始位置終了位置を設定できる。
作業手順:6
'''

import DaVinciResolveScript as dvr
import os
import sys
import time
import re
# WIN フォルダのパスを取得し、Python パスに追加
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import config.config_lubed as config


 

########################設定#####################
#ビンの数の範囲
bin_count=10
start_bin=1

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

            # タイムラインを取得※タイムライン生成時に生成順に割り振られるインデックス番号で取得する。
            timeline = project.GetTimelineByIndex(i)  # iでタイムラインを取得

            if not timeline:
                print(f"タイムライン '{bin_name}' が見つかりませんでした。")
                continue
            if timeline:
                 print("タイムラインが正常に取得されました。")

             # タイムラインを現在のタイムラインとして設定　※設定する位置がレンダリング設定をする位置より前にないとうまくいかない
            project.SetCurrentTimeline(timeline)
            
            # デリバーページに移行
            test = resolve.OpenPage("deliver")
            if timeline:
                print("移行が正常に行われました。\n\n")

            # 新規フォルダーを作成するパス（base_output_dirの中にフォルダー名を生成）
            new_folder_path = os.path.join(config.base_output_dir, f"{config.new_folder_name}-{i:03d}")
            
            #トップ画像用フォルダーを作成するパス（base_output_dirの中にフォルダー名を生成）
            header_folder_path=os.path.join(new_folder_path,f"header-{i:03d}")
            
            # 新規フォルダーを作成
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
                os.makedirs(header_folder_path)
                print(f"新規フォルダ '{new_folder_path}' が作成されました。")

            # 出力ファイルのパスを設定（ビン名を使用）
            output_path = os.path.join(new_folder_path, f"{bin_name}.mp4")

              # タイムラインの開始フレームと終了フレームを取得して確認
            start_frame = timeline.GetStartFrame()
            end_frame = timeline.GetEndFrame()

            #終了フレームからカットするフレーム数をマイナスしてセットするフレームを変数に代入
            markout_set=end_frame-config.markout

            print(f"マークアウト：{config.markout}")
            print(f"マークアウトセット：{markout_set}")

                    # 動画の秒数を計算（フレーム数 ÷ フレームレート）
            fps = timeline.GetSetting("timelineFrameRate")
            duration_seconds = (end_frame - start_frame) / fps

            # 目標ファイルサイズに収めるためのビットレート計算（kbps）
            target_size_mb = 1750  # 目標サイズ 1.9GB (1900 MB)
            bitrate_kbps = (target_size_mb * 8192) / duration_seconds  # 8 bits/byte * 1024 kb/MB



            # レンダリング設定を行う
            project.SetRenderSettings({
                "TargetDir": new_folder_path,  # 出力ディレクトリ（新規フォルダ）
                "CustomName": "lu"+bin_name,        # ファイル名をビン名に設定
                "FormatWidth": 1980,           # 出力解像度（幅）
                "FormatHeight": 1080,            # 出力解像度（高さ）
                "VideoQuality": int(bitrate_kbps),  # 計算されたビットレート
                "MarkIn":config.markln,
                #"MarkOut":markout_set,         
            })

            print(f"タイムラインの開始フレーム: {start_frame}, 終了フレーム: {end_frame}")
            print(f"タイムラインの開始フレーム: {start_frame}, 終了フレーム: {end_frame}")
            print(f"ビットレート（kbps）: {int(bitrate_kbps)}")
            # レンダーキューに追加
            project.AddRenderJob()

        # 全てのジョブがキューに追加されたのでレンダリング開始
        startrem = project.StartRendering()
        if startrem:
           print("レンダーが行われます。\n\n")

            # レンダージョブのリストを取得

        render_jobs = project.GetRenderJobList()

        #失敗リスト変数
        errorlist=[]

        for render in render_jobs:
            print(f"{render}")

        '''
        実装のポイント
        StartRendering(): 各ジョブを個別に開始します。
        IsRenderingInProgress(): レンダリング中の状態をポーリングして監視します。
        失敗時の処理: ステータスに「失敗」というキーワードが含まれているかを確認し、失敗した場合はStopRendering()を呼び出して次のジョブに進みます。
        時間間隔の設定: 進行状況を監視する間隔（例: 5秒）はtime.sleep()で調整します。


        render_jobs = project.GetRenderJobList()
        ↓
        ジョブ {'JobId': 'af46cdc9-f7f7-4ee7-bf40-a374d919c9fc', 'RenderJobName': 'Job 1', 'TimelineName': 'Timeline_001', 'TargetDir': 'D:\\rendertest\\render-001',
          'IsExportVideo': True, 'IsExportAudio': True, 'FormatWidth': 1280, 'FormatHeight': 720, 'FrameRate': '29.97', 'PixelAspectRatio': 1.0, 'MarkIn': 0, 'MarkOut': 154380,
            'AudioBitDepth': 24, 'AudioSampleRate': 48000, 'ExportAlpha': False, 'OutputFilename': 'sprmBin_001.mov', 'RenderMode': 'Single clip',
          'PresetName': 'Custom', 'VideoFormat': 'QuickTime', 'VideoCodec': 'H.264 NVIDIA', 'AudioCodec': 'lpcm', 'EncodingProfile': 'Auto', 'MultiPassEncode': False, 'NetworkOptimization': False}
        '''

        render_jobs = project.GetRenderJobList()

        #失敗リスト変数
        errorlist=[]
        

        if not render_jobs:
            print("レンダージョブがありません。")
        else:
            print(f"{len(render_jobs)} 件のレンダージョブを処理します。")

            for job_list in render_jobs:
                print(f"ジョブ {job_list} を開始します...")
                print(f"jobidは{job_list["JobId"]}")
                project.StartRendering(job_list["JobId"])

                # レンダリングの進行状況を監視
                while project.IsRenderingInProgress():
                    time.sleep(5)  # 5秒待機
                    job_status = project.GetRenderJobStatus(job_list["JobId"])
                    print(f"ジョブステータス：{job_status}")
                    status_info = job_status['JobStatus']
                    print(f"ジョブ {job_list["JobId"]} のステータス: {status_info}")

                    if 'EstimatedTimeRemainingInMs' in job_status:
                        print(f"EstimatedTimeRemainingInMs:[{job_status['EstimatedTimeRemainingInMs']}]")

                    if "失敗しました" in status_info:  # ステータスに「失敗」が含まれている場合
                        print(f"ジョブ {job_list["JobId"]} は失敗しました。次のジョブに進みます。")
                        errorlist.append(job_list['TargetDir'])
                        project.StopRendering()
                        break
                    if 'EstimatedTimeRemainingInMs' in job_status:
                        if job_status['EstimatedTimeRemainingInMs']<0:
                            print(f"EstimatedTimeRemainingInMsがマイナスになっています。{job_status['EstimatedTimeRemainingInMs']}")
                            project.StopRendering()
                            project.StartRendering(job_list["JobId"])
                            break
                        

                    #if status_info[EstimatedTimeRemainingInMs]
                # ジョブ完了後の処理
                job_status = project.GetRenderJobStatus(job_list['JobId'])
                if job_status['JobStatus'] == "完了":
                    print(f"ジョブ {job_list['JobId']} が成功しました。")
                else:
                    print(f"ジョブ {job_list['JobId']} が失敗または中断されました。")

                # レンダリングを明示的に停止
                project.StopRendering()
                print(f"ジョブ {job_list['JobId']} のレンダリングを停止しました。")

                print("すべてのジョブの処理が終了しました。")
            

            for i in errorlist:
                print(f"エラーが出たフォルダは{i}")

            # 番号部分を抽出して整数に変換する
            error_numbers = []
            for path in errorlist:
                match = re.search(r'lu-(\d+)', path)  # パターン 'render-数字' を検索
                if match:
                    number = int(match.group(1))  # マッチした番号を整数に変換
                    error_numbers.append(number)

            print(f"番号リスト: {error_numbers}")

                        # リストを書き出すファイルパス
            list_path = r"H:\Lubed\lubed\error_numbers.txt"  # 保存先のパスに変更してください

            # テキストファイルにリストを書き出す
            try:
                with open(list_path, 'w') as file:
                    for number in error_numbers:
                        file.write(f"{number}\n")  # 各番号を改行付きで書き出し
                print(f"エラー番号のリストが '{list_path}' に書き出されました。")
            except Exception as e:
                print(f"リストの書き出し中にエラーが発生しました: {e}")

        
            

else:
    print(f"'{config.project_name}' プロジェクトをロードできませんでした。")