# sqlite3

import sqlite3 as sql

with sql.connect(":memory:") as connection:
  cursor = connection.cursor()

