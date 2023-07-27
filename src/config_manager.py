import configparser
import json


class ConfigManager:
    def __init__(self):
        self.config = configparser.ConfigParser()
        with open('../config.ini', 'r', encoding='utf-8') as f:
            self.config.read_file(f)
        with open('../messages.json', 'r', encoding='utf-8') as f:
            self.messages = json.load(f)

    def get_screenshot_region(self):
        left = self.config.getint('Screenshot', 'Left')
        top = self.config.getint('Screenshot', 'Top')
        width = self.config.getint('Screenshot', 'Width')
        height = self.config.getint('Screenshot', 'Height')
        return (left, top, width, height)

    def get_message(self, message_id):
        language = self.config.get('Language', 'language')
        return self.messages[language][message_id]
