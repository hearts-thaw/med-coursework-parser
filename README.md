# Python Parser
*for medical students' coursework DOCX*


### How DOCX should be formatted:
```
Субъекты федерации | year1 (abs) | year2 (abs) | year1 (rel) | year2 (rel) |
...далее округа..  |    абсолютные значения    |  относителные значения    |
...districts.....  |    absolute    values     |  relative values          |
```
p. s. special cases are processed on an ad hoc basis

## How to use it

### GUIDE FOR CONFIG
1. create **config.ini** in root directory of that project
2. uncomment lines with **config.ini** in *src/parser.py:7* and *src/reader.py:7*
3. put path to directory with DOCX files under key **"path"** in **[READER]** section: 
```ini
[READER]
path : home/your_shiny_new_directory/example_path/
```
4. put all information required to make your psycopg (db lib) work:
```ini
[PARSER]
database : name of your database
user     : your username
password : your password
host     : host of database (localhost by default)
port     : port you chose for database (5432 by default for PostgreSQL)
```
5. run ```pip install -r requirements.txt``` and ```python -m parser```


### GUIDE FOR LOCAL_CONFIG (path pre-written):
1. create database in accordance with UML in parent project (kursach_backend)
2. in **local_config.ini** put your *database*, *user*, *password* and *port* under **[PARSER]**
3. change *src/parser.py:2* and *src/parser.py:18* to match your SQL vendor
4. install required libraries (**python-docx** and **%your-vendor-name-SQL%**) and run ```python -m parser```