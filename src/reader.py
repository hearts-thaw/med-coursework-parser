import configparser
import os
import re

config = configparser.ConfigParser()
config.read("config.ini")


def diseases_years():
    for _, _, f in os.walk(config["READER"]["path"]):
        for file in f:
            # print(file)
            if file.startswith(".~lock."):
                continue
            yield " ".join(re.findall("([а-яА-ЯёЁ]+)", file)),\
                  tuple(map(int, re.search("([0-9]+)-([0-9]+)", file).groups()))
