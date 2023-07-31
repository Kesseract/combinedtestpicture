import os
import pyautogui
import keyboard
import subprocess
import platform


class ScreenshotTaker:
    def __init__(self, config_manager, test_case_manager):
        self.config_manager = config_manager
        self.test_case_manager = test_case_manager
        self.test_case_name = None

    def take_screenshot(self):
        if self.test_case_name:
            image = pyautogui.screenshot(region=self.config_manager.get_screenshot_region())
            path = f"../data/{self.test_case_name}/{self.step}"
            if self.sub_step:
                path += f"-{self.sub_step}"
            path += ".png"
            os.makedirs(os.path.dirname(path), exist_ok=True)
            image.save(path)

    def manual_take_screenshot(self, test_case_name, step):
        self.test_case_name = test_case_name
        self.step = None
        self.sub_step = None

        if isinstance(step, tuple):
            self.step = step[0]
            self.sub_step = step[1]
        else:
            self.step = step

        self.take_screenshot()

    def automatic_take_screenshot(self):
        test_case_name, step = self.test_case_manager.get_next_test_case()
        if test_case_name and step:
            self.manual_take_screenshot(test_case_name, step)

    def start_automatic_screenshot_taking(self):
        keyboard.add_hotkey('f9', self.automatic_take_screenshot)

    def open_image(self, test_case_name, image_number):
        image_path = f"../data/{test_case_name}/{image_number}.png"

        if platform.system() == 'Darwin':  # If it's MacOS
            subprocess.call(['open', image_path])
        elif platform.system() == 'Windows':  # If it's Windows
            subprocess.call(['start', image_path], shell=True)
        else:
            print(self.config_manager.get_message("delete_not_exist"))

    def delete_image(self, test_case_name, image_number):
        image_path = f"../data/{test_case_name}/{image_number}.png"
        if os.path.exists(image_path):
            os.remove(image_path)
            print(self.config_manager.get_message("deleted").format(image_path=image_path))
        else:
            print(self.config_manager.get_message("delete_not_exist"))
