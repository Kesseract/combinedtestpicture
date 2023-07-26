import os
import pyautogui

base_dir = "../data/combinedtest"  # 保存先ディレクトリを指定

# ディレクトリが存在しない場合、作成
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

test_case_dir = base_dir


def print_dir_contents(directory):
    print("Current directories:")
    for name in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, name)):
            print(name)


while True:
    print_dir_contents(base_dir)
    print("Please enter the test case directory name (or 'q' to quit):")
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
        print("Please enter the filename number (or ' ' to change directory or 'q' to quit):")
        filename_num = input()

        if filename_num == 'q':
            exit()
        elif filename_num == " ":
            break

        # 画面全体のスクリーンショットを取得
        screenshot = pyautogui.screenshot(region=(0, 110, 1920, 970))
        # 入力された番号でファイル名を作成
        filename = f"{filename_num}.png"
        # ファイルを保存
        screenshot.save(os.path.join(test_case_dir, filename))
