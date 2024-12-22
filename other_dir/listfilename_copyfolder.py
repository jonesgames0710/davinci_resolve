'''

'''

import os
import shutil

# コピー元の親ディレクトリ
source_root = r"K:\heyzo"
# コピー先ディレクトリ
destination_folder = r"D:\ダウンロード\heyzo"

# 対象ファイル名リスト
file_list = [
    "heyzo_hd_2015_full.mp4", "heyzo_hd_1949_full.mp4", "heyzo_hd_1988_full.mp4",
    "heyzo_hd_1936_full.mp4", "heyzo_hd_1980_full.mp4", "heyzo_hd_2025_full.mp4",
    "heyzo_hd_1981_full.mp4", "heyzo_hd_2041_full.mp4", "heyzo_hd_2011_full.mp4",
    "heyzo_hd_1896_full.mp4", "heyzo_hd_2051_full.mp4", "heyzo_hd_2019_full.mp4",
    "heyzo_hd_1923_full.mp4", "heyzo_hd_2016_full.mp4", "heyzo_hd_1985_full.mp4",
    "heyzo_hd_2001_full.mp4", "heyzo_hd_2029_full.mp4", "heyzo_hd_2056_full.mp4",
    "heyzo_hd_1948_full.mp4", "heyzo_hd_2081_full.mp4", "heyzo_hd_1971_full.mp4",
    "heyzo_hd_1990_full.mp4", "heyzo_hd_1996_full.mp4", "heyzo-2423-1080p.mp4",
    "heyzo-2504-1080p.mp4", "heyzo_hd_2298_full.mp4", "heyzo_hd_2133_full.mp4",
    "heyzo_hd_2327_full.mp4", "heyzo_hd_2361_full.mp4", "heyzo_hd_2189_full.mp4",
    "heyzo_hd_2182_full.mp4", "heyzo_hd_2164_full.mp4", "heyzo_hd_2098_full.mp4",
    "heyzo_hd_2254_full.mp4", "heyzo_hd_2183_full.mp4", "heyzo_hd_2256_full.mp4",
    "heyzo_hd_2205_full.mp4", "heyzo_hd_2120_full.mp4", "heyzo-2509-1080p.mp4",
    "heyzo-2513-1080p.mp4", "heyzo_hd_2424_full.mp4", "heyzo-2441-1080p.mp4",
    "heyzo-2519-1080p.mp4", "heyzo-2478-1080p.mp4", "heyzo-2162.mp4",
    "heyzo_hd_2091_full.mp4", "heyzo_hd_2238_full.mp4", "heyzo_hd_2517_full.mp4",
    "heyzo_hd_2261_full.mp4", "heyzo_hd_2092_full.mp4", "heyzo_hd_2518_full.mp4",
    "heyzo_hd_2379_full.mp4", "heyzo-2527-1080p.mp4", "heyzo-2542.mp4",
    "heyzo_hd_2328_full (1).mp4", "heyzo-2532.mp4", "heyzo-2528-1080p.mp4",
    "heyzo-2491-1080p.mp4", "heyzo-2457-1080p.mp4", "heyzo-2445-1080p.mp4",
    "heyzo_hd_2406_full.mp4", "heyzo_hd_2400_full.mp4", "heyzo-2496-1080p.mp4",
    "heyzo_hd_2129_full.mp4", "heyzo_hd_2417_full.mp4", "heyzo_hd_2310_full.mp4",
    "heyzo-2550.mp4", "heyzo_hd_2069_full.mp4", "heyzo-2554.mp4",
    "heyzo_hd_2324_full.mp4", "heyzo_hd_2242_full.mp4", "heyzo-2425-1080p.mp4",
    "heyzo_hd_2203_full.mp4", "Heyzo_hd_3229_full.mp4", "heyzo-3007.mp4",
    "heyzo-3162.mp4", "heyzo-3097.mp4", "heyzo-3023.mp4", "heyzo_hd_3138_full.mp4",
    "heyzo-3040.mp4", "heyzo-3202.mp4", "heyzo-2570.mp4", "heyzo-3061.mp4",
    "heyzo-3067.mp4", "Heyzo-3263-1080p.mp4", "heyzo-2872.mp4", "heyzo-3104.mp4",
    "heyzo-2923.mp4", "heyzo-2582.mp4", "Heyzo_hd_3276_full.mp4",
    "Heyzo-3254-1080p.mp4", "heyzo-2846.mp4", "heyzo_hd_3056_full.mp4",
    "heyzo_hd_2159_full.mp4", "Heyzo-3260-1080p.mp4", "heyzo-3145.mp4",
    "heyzo-3027.mp4", "heyzo-2953.mp4", "heyzo-2839.mp4", "heyzo-2992.mp4",
    "heyzo-2858.mp4", "Heyzo-3236-FHD.mp4", "heyzo-3131.mp4", "heyzo-2897.mp4",
    "heyzo-3167.mp4", "heyzo-3144.mp4", "n0338_risako_mamiya.mp4",
    "heyzo-2416-1080p.mp4", "heyzo-2558.mp4", "heyzo-2794.mp4", "heyzo-2996.mp4",
    "heyzo_hd_2253_full.mp4", "heyzo-2561.mp4", "heyzo-3031.mp4", "heyzo-2703.mp4",
    "heyzo_hd_2510_full.mp4", "heyzo-3006.mp4", "heyzo-2912.mp4", "heyzo-2814.mp4",
    "heyzo-2829.mp4", "heyzo-3095.mp4", "heyzo-2845.mp4", "heyzo-2536.mp4",
    "heyzo-2929.mp4", "Heyzo-3148.mp4", "heyzo-3020.mp4", "heyzo-2991.mp4",
    "heyzo-2938.mp4", "heyzo-3019.mp4", "heyzo_hd_2241_full.mp4",
    "heyzo-2705.mp4", "heyzo-2964.mp4", "heyzo-2881.mp4", "Heyzo-3226-FHD.mp4",
    "heyzo-2714.mp4", "heyzo-2941.mp4", "heyzo-3012.mp4", "heyzo_3155.mp4",
    "heyzo-3141.mp4", "heyzo-2947.mp4", "heyzo_hd_2073_full.mp4",
    "heyzo-2548-1080p.mp4", "heyzo-2998.mp4", "Heyzo-3246-1080p.mp4",
    "heyzo_hd_2160_full.mp4", "heyzo_hd_2199_full.mp4", "heyzo-3136.mp4",
    "heyzo_hd_2302_full.mp4", "heyzo_hd_2375_full.mp4", "heyzo_hd_2127_full.mp4",
    "heyzo_hd_3199.mp4", "heyzo-2813.mp4", "heyzo-2854.mp4", "heyzo-2590.mp4",
    "heyzo-2490-1080p.mp4", "Heyzo-3275-1080p.mp4", "heyzo-2541.mp4",
    "heyzo-3125.mp4", "heyzo-2563.mp4", "heyzo_hd_2104_full.mp4",
    "heyzo_hd_3216_full.mp4", "heyzo-2521-1080p.mp4", "heyzo_hd_2249_full.mp4",
    "ARCHIVE-heyzo_hd_3201_full.mp4", "heyzo-2808.mp4", "heyzo-3038.mp4",
    "heyzo-2598.mp4", "heyzo-2600.mp4", "heyzo-2603.mp4", "heyzo-2638.mp4"
]

def copy_files(source_root, destination_folder, file_list):
    # コピー先フォルダが存在しない場合、作成する
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # ファイルをコピーする
    for root, dirs, files in os.walk(source_root):
        for file_name in file_list:
            if file_name in files:
                # ファイルのフルパス
                source_file = os.path.join(root, file_name)
                destination_file = os.path.join(destination_folder, file_name)

                # ファイルをコピー
                shutil.copy2(source_file, destination_file)
                print(f"コピー完了: {source_file} → {destination_file}")

if __name__ == "__main__":
    copy_files(source_root, destination_folder, file_list)
