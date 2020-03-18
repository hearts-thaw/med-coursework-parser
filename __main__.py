from src import reader

if __name__ == '__main__':
    for disease, year in reader.diseases_years():
        print(disease, year)
