import os

from config_manager import ConfigManager
from test_case_manager import TestCaseManager
from screenshot_taker import ScreenshotTaker


class MainApplication:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.test_case_manager = TestCaseManager("../test_cases.xlsx")
        self.screenshot_taker = ScreenshotTaker(self.config_manager, self.test_case_manager)

    def run(self):
        self.screenshot_taker.start_automatic_screenshot_taking()
        self.test_case_manager.load_test_cases_from_excel('../test_cases.xlsx')
        self.test_case_manager.create_test_case_folders()
        while True:
            print(self.config_manager.get_message("existing_test_cases"))
            existing_cases = os.listdir('../data/')
            for i, case in enumerate(existing_cases, 1):
                print(f"{case}")
            test_case_name = input(self.config_manager.get_message("input_test_case"))
            if test_case_name == 'q':
                break
            while True:
                print(self.config_manager.get_message("image_lists"))
                images = os.listdir(f'../data/{test_case_name}')
                for image in images:
                    print(image)
                step = input(self.config_manager.get_message("input_image_name"))
                split_input = step.split(' ')

                if len(split_input) < 2:
                    if step == ' ':
                        break
                    elif step == 'q':
                        break
                    if '-' in step:
                        split_substep = tuple(map(int, step.split('-')))
                    else:
                        split_substep = int(step)
                    self.screenshot_taker.manual_take_screenshot(test_case_name, split_substep)
                else:
                    image_number, command = split_input[0], split_input[1]
                    if command == '-r':
                        self.screenshot_taker.open_image(test_case_name, image_number)
                    elif command == '-d':
                        self.screenshot_taker.delete_image(test_case_name, image_number)
                    else:
                        print(self.config_manager.get_message("unknown_command").format(command=command))


if __name__ == "__main__":
    app = MainApplication()
    app.run()
