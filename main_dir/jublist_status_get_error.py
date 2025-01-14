'''
レンダリングが失敗しているジョブをジョブリストのステータスから取得してテキストに書き出し
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

 
        # レンダージョブのリストを取得

    render_jobs = project.GetRenderJobList()

    #失敗リスト変数
    errorlist=[]

    if project.IsRenderingInProgress():

        for render in render_jobs:

            job_status = project.GetRenderJobStatus(render["JobId"])
            status_info = job_status['JobStatus']

            print(f"ジョブリスト：{render["JobId"]}")

            if "失敗しました" in status_info:  # ステータスに「失敗」が含まれている場合
                print(f"ジョブ {render["JobId"]} は失敗しました。次のジョブに進みます。")
                errorlist.append(render['TargetDir'])

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