import os
import configparser

config_obj = configparser.ConfigParser()
config_obj.read('./config/base.ini', encoding='utf-8')

if __name__ == "__main__":
    print("sections", config_obj.sections())