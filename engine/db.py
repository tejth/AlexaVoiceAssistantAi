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

# query = "INSERT INTO sys_command VALUES (null,'Microsoftedge', 'C:\Program Files (x86)\Microsoft\Edge\Application')"
# cursor.execute(query)



# query = """
#     UPDATE web_command
#     SET url = 'https://www.canva.com/'
#     WHERE name = 'canva' AND url = 'https://www.canva.com//'
# """
# cursor.execute(query)


# query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)


# query = "INSERT INTO web_command VALUES (null,'canva', 'https://www.canva.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'geek for geeks', 'https://www.geeksforgeeks.org/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'github', 'https://github.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'mdn', 'https://developer.mozilla.org/en-US/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'chatgpt', 'https://chatgpt.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'leetcode', 'https://leetcode.com/')"
# cursor.execute(query)


# query = "INSERT INTO web_command VALUES (null,'w3schools', 'https://www.w3schools.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'instagram', 'https://www.instagram.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'facebook', 'https://www.facebook.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'gmail', 'https://www.gmail.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'googledrive', 'https://drive.google.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'bootstrap', 'https://getbootstrap.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'ilovepdf', 'https://www.ilovepdf.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'flipkart', 'https://www.flipkart.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'amazon', 'https://www.amazon.in/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'google', 'https://google.com/')"
# cursor.execute(query)


# testing module
# app_name = "android studio"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
# results = cursor.fetchall()
# print(results[0][0])






con.commit()
