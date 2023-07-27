import os
import openpyxl


class TestCaseManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.reload()
        self.test_cases = {}

    def load_test_cases_from_excel(self, excel_path):
        workbook = openpyxl.load_workbook(excel_path)
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=2, values_only=True):  # 1行目はヘッダーなので読み飛ばす
            if row[0]:  # Check if testcase name is not empty
                test_case_name = row[0]
                steps = [i for i, x in enumerate(row[1:], start=1) if x is not None]
                self.test_cases[test_case_name] = steps

    def create_test_case_folders(self):
        for test_case_name in self.test_cases:
            os.makedirs(f"../data/{test_case_name}", exist_ok=True)

    def reload(self):
        self.wb = openpyxl.load_workbook(self.file_path)
        self.sheet = self.wb.active
        self.current_row = 2
        self.current_step = 1

    def get_next_test_case(self):
        while self.sheet.cell(row=self.current_row, column=1).value:
            while self.sheet.cell(row=self.current_row, column=self.current_step + 1).value:
                self.current_step += 1
                return self.sheet.cell(row=self.current_row, column=1).value, self.current_step - 1
            self.current_row += 1
            self.current_step = 1
        return None, None
