import configparser
import os
import re

config = configparser.ConfigParser()
# UNCOMMENT FOR YOUR OWN CONFIG (and comment next line after that)
# config.read("config.ini")
config.read("local_config.ini")
path = config["READER"]["path"]


def read():
    for _, _, f in os.walk(path):
        for file in f:
            if file.startswith(".~lock."):
                continue
            yield path + file, " ".join(re.findall("([а-яА-ЯёЁ]+)", file)).replace('\n', ' ')
