import sys
import os

# DaVinci Resolve APIのパスを設定
resolve_api_path = r"/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules"
sys.path.append(resolve_api_path)

# DaVinci Resolve APIをインポート
try:
    import DaVinciResolveScript
except ImportError:
    print("DaVinci Resolve APIが見つかりません。パスを確認してください。")

# DaVinci Resolveに接続
resolve = DaVinciResolveScript.scriptapp("Resolve")
if resolve is None:
    print("DaVinci Resolveに接続できません。Resolveが起動しているか確認してください。")
else:
    print("DaVinci Resolveに接続成功！")


resolve = None
try:
    resolve = DaVinciResolveScript.scriptapp("Resolve")
except Exception as e:
    print(f"エラー: {e}")
