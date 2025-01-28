# sqlite3

from datetime import date
import sqlite3 as sql

ddl: str = '''
  create table todo (
    id integer primary key auto_increment,
    task text not null,
    created timestamp not null,
    completed timestamp not null
  );
'''

with sql.connect(":memory:", detect_types = sql.PARSE_DECLTYPES | sql.PARSE_COLNAMES) as connection:
  cursor: sql.Cursor = connection.cursor()
  cursor.execute(ddl)
  connection.commit()