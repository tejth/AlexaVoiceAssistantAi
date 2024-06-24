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


# Create a table with the desired columns
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')
# con.commit()

# cursor.execute('''DELETE FROM contacts''')
# con.commit()


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 31]

#Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# con.commit()
# con.close()


# query = 'kunal'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])

query = "INSERT INTO contacts VALUES (null,'sparsh ', '8126244177',null)"
cursor.execute(query)
con.commit()