import os
import pyautogui
import keyboard


class ScreenshotTaker:
    def __init__(self, config_manager, test_case_manager):
        self.config_manager = config_manager
        self.test_case_manager = test_case_manager
        self.test_case_name = None

    def take_screenshot(self):
        if self.test_case_name:
            image = pyautogui.screenshot(region=self.config_manager.get_screenshot_region())
            path = f"../data/{self.test_case_name}/{self.step}.png"
            os.makedirs(os.path.dirname(path), exist_ok=True)
            image.save(path)

    def manual_take_screenshot(self, test_case_name, step):
        self.test_case_name = test_case_name
        self.step = self.test_case_manager.test_cases[test_case_name][step-1]
        self.take_screenshot()

    def automatic_take_screenshot(self):
        test_case_name, step = self.test_case_manager.get_next_test_case()
        if test_case_name and step:
            self.manual_take_screenshot(test_case_name, step)

    def start_automatic_screenshot_taking(self):
        keyboard.add_hotkey('f9', self.automatic_take_screenshot)
