# sqlite3

from datetime import date
import sqlite3 as sql

ddl = '''
  create table todo (
    id integer primary key auto_increment,
    task text not null,
    created text not null,
    completed text not null
  );
'''

with sql.connect(":memory:") as connection:
  cursor = connection.cursor()

