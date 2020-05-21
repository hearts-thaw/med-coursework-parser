from docx import Document
import configparser
import psycopg2

config = configparser.ConfigParser()
# COMMENT FOR YOUR OWN CONFIG (and uncomment next line after that)
config.read("../config.ini")
# config.read("local_config.ini")
dbinfo = config['PARSER']


def parse(file, disease):
    conn = None
    cur = None
    document = Document('../medical_students_project/' + file.split("/")[-1])

    try:

        conn = psycopg2.connect(database=dbinfo["database"], user=dbinfo["user"],
                                password=dbinfo["password"], host=dbinfo["host"], port=dbinfo["port"])
        cur = conn.cursor()

        query = """ INSERT INTO diseases (disease, year, abs, abs_child, rel, rel_child, district, predicted)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """

        cur.execute("SELECT * FROM federal_districts ")

        districts = [x[0] for x in cur.fetchall()]

        for table in document.tables:
            for i in range(len(table.rows)):
                row_cells = table.row_cells(i)
                district = row_cells[0].text.lower()
                if disease == 'Сахарный диабет':
                    print(district)
                if district in districts:
                    if disease == 'Сахарный диабет':
                        print("matched")
                    len_of_row = len(row_cells)

                    if table.column_cells(1)[0].text:
                        data = getData(table, 1, row_cells, len_of_row != 5)
                        data.insert(0, disease)
                        data.append(district)
                        data.append(False)
                        cur.execute(query, data)
                        if disease == 'Сахарный диабет':
                            print(*data)
                    if table.column_cells(2)[0].text:
                        data = getData(table, 2, row_cells, len_of_row != 5)
                        data.insert(0, disease)
                        data.append(district)
                        data.append(False)
                        cur.execute(query, data)
                        if disease == 'Сахарный диабет':
                            print(*data)
                    conn.commit()
    except psycopg2.Error as error:
        print("Failed inserting record into table {}".format(error))
    finally:
        if (conn):
            cur.close()
            cur.close()
            print("PostgreSQL connection is closed")


def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False


def to_num(string):
    if not string:
        return None
    string = string.replace(',', '.')
    if is_integer_num(string):
        return int(string)
    else:
        return float(string)


def getData(table, order, row_cells, isHiv):
    data = list()

    year = int(table.column_cells(order)[0].text)

    data.append(year)
    if isHiv:
        for i in range(order, len(row_cells), 2):
            text = row_cells[i].text
            if text != "-":
                data.append(to_num(text))
            else:
                data.append(None)
    else:
        for i in range(order, len(row_cells), 2):
            text = row_cells[i].text
            if text != "-":
                data.append(to_num(text))
            else:
                data.append(None)
            data.append(None)

    return data
