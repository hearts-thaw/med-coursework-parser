import reader
import parser

if __name__ == '__main__':
    for file, disease in reader.read():
        parser.parse(file, disease)
