from parser import reader, parser

if __name__ == '__main__':
    for file, disease in reader.read():
        parser.parse(file, disease)
