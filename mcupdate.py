import os
import requests

vv_filename = ''


# ファイルをURLからmcupdateフォルダにダウンロードする
def download_file(url, save_path):

    save_path = './mcupdate/'+save_path

    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"ダウンロードが完了しました: {save_path}")
    else:
        print("ファイルのダウンロードに失敗しました")


def geyser():
    # ダウンロードするファイルのURLと保存先パス
    download_url = "https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/spigot"
    save_file_path = "Geyser-spigot.jar"

    # ファイルのダウンロード
    download_file(download_url, save_file_path)
    
    print("最新のGeyserMCをダウンロードしました。")

def floodgate():
    # ダウンロードするファイルのURLと保存先パス
    download_url = "https://download.geysermc.org/v2/projects/floodgate/versions/latest/builds/latest/downloads/spigot"
    save_file_path = "floodgate-spigot.jar"

    # ファイルのダウンロード
    download_file(download_url, save_file_path)
    
    print("最新のFloodgateをダウンロードしました。")

def viaversion():
    # 最新のバージョン番号を取得
    url = "https://hangar.papermc.io/api/v1/projects/ViaVersion/ViaVersion/latestrelease"
    response = requests.request("GET", url)
    latest_version = response.text
    print(f"最新のViaVersionバージョン: {latest_version}")

    # ファイルのダウンロード
    download_url = f"https://hangar.papermc.io/api/v1/projects/ViaVersion/ViaVersion/versions/{latest_version}/PAPER/download"
    save_file_path = "ViaVersion.jar"
    download_file(download_url, save_file_path)

    print("最新のViaVersionをダウンロードしました。")

def viabackwards():
    # 最新のバージョン番号を取得
    url = "https://hangar.papermc.io/api/v1/projects/ViaVersion/ViaBackwards/latestrelease"
    response = requests.request("GET", url)
    latest_version = response.text
    print(f"最新のViaBackwardsバージョン: {latest_version}")

    # ファイルのダウンロード
    download_url = f"https://hangar.papermc.io/api/v1/projects/ViaVersion/ViaBackwards/versions/{latest_version}/PAPER/download"
    save_file_path = "ViaBackwards.jar"
    download_file(download_url, save_file_path)

    print("最新のViaBackwardsをダウンロードしました。")


def mcupdate():
    geyser()
    floodgate()
    viaversion()
    viabackwards()

if __name__ == "__main__":
    if not os.path.exists('./mcupdate'):
        os.makedirs('./mcupdate')
    mcupdate()
    print("全てのプラグインのダウンロードが完了しました。")
