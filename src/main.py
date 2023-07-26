import os
import pyautogui
import configparser

# 現在のスクリプトのあるディレクトリを取得
current_dir = os.path.dirname(os.path.abspath(__file__))

# 設定ファイルのパスを指定
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../config.ini')

# configparserの設定
config = configparser.ConfigParser()
config.read(config_path)

# スクリーンショットの範囲を設定ファイルから読み込む
left = config.getint('DEFAULT', 'Left')
top = config.getint('DEFAULT', 'Top')
width = config.getint('DEFAULT', 'Width')
height = config.getint('DEFAULT', 'Height')

base_dir = "../data"  # 保存先ディレクトリを指定

# ディレクトリが存在しない場合、作成
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

test_case_dir = base_dir


def print_dir_contents(directory):
    print("テストケース一覧:")
    for name in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, name)):
            print(name)


while True:
    print_dir_contents(base_dir)
    print("テストケース名を入力してください。 ('q'キーで終了):")
    dir_name = input()

    if dir_name == 'q':
        break
    elif dir_name == " ":
        continue
    else:
        test_case_dir = os.path.join(base_dir, dir_name)
        if not os.path.exists(test_case_dir):
            os.makedirs(test_case_dir)

    while True:
        print("保存する画像名を入力してください。 (スペースキーでフォルダ変更、'q'キーで終了):")
        filename_num = input()

        if filename_num == 'q':
            exit()
        elif filename_num == " ":
            break

        # 画面全体のスクリーンショットを取得
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        # 入力された番号でファイル名を作成
        filename = f"{filename_num}.png"
        # ファイルを保存
        screenshot.save(os.path.join(test_case_dir, filename))
