# Python Parser
*for medical students' coursework DOCX*

## How to use it:
* create **config.ini** in root directory of that project
* put path to directory with DOCX files under key **"path"** in **[READER]** section: 
```ini
[READER]
path : home/your_shiny_new_directory/example_path/
```
* put all information required to make your psycopg (db lib) work:
```ini
[PARSER]
database : name of your database
user     : your username
password : your password
host     : host of database (localhost by default)
port     : port you chose for database (5432 by default for PostgreSQL)
```

### How DOCX should be formatted:
```
Субъекты федерации | year1 (abs) | year2 (abs) | year1 (rel) | year2 (rel) |
...далее округа..  |    абсолютные значения    |  относителные значения    |
```
p. s. special cases are processed on an ad hoc basis 