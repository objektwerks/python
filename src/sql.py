# sqlite3

from datetime import datetime
import sqlite3 as sql

ddl: str = '''
  create table todo (
    id integer primary key autoincrement,
    task text not null,
    created timestamp not null,
    completed timestamp not null
  );
'''

insert: str = '''
  insert into todo (task, created, completed) 
  VALUES (?, ?, ?);
'''

select: str = '''
  select * from todo;
'''

with sql.connect(":memory:", detect_types = sql.PARSE_DECLTYPES | sql.PARSE_COLNAMES) as connection:
  cursor: sql.Cursor = connection.cursor()
  cursor.execute(ddl)
  connection.commit()

  todo = ('wash car', datetime.now, datetime.now)
  cursor.execute(insert, todo)
  connection.commit()

  cursor.execute(select)
  todos = cursor.fetchall()
  print("todos:")
  for todo in todos:
    print(todo)