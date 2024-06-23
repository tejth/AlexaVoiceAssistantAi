import csv
import sqlite3

con = sqlite3.connect("eco.db")
cursor = con.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'notion', 'C:\\Users\\tejth\\AppData\\Local\\Programs\\Notion\\Notion.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'vs code', 'C:\\Users\\tejth\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'eDEX-UI', 'C:\\Users\\tejth\\AppData\\Local\\Programs\\eDEX-UI\\eDEX-UI.exe')"
# cursor.execute(query)


query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
cursor.execute(query)


query = "INSERT INTO web_command VALUES (null,'canva', 'https://www.canva.com//')"
cursor.execute(query)

con.commit()
