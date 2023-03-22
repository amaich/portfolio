import sqlite3


def stroke_creator(tfile):
    tlist = []
    tfile = tfile[:tfile.find('\n')]

    for j in range(tfile.count(',')):
        tlist.append(tfile[:tfile.find(',')])
        tfile = tfile[tfile.find(',') + 1:]
    tlist.append(tfile)

    return tlist


file = open('goods.txt', 'r')
text_file = file.read()
if text_file[:-2] != '\n':
    text_file += '\n'
final_list = []


for i in range(text_file.count('\n')):
    final_list.append(stroke_creator(text_file))
    text_file = text_file[text_file.find('\n')+1:]


conn = sqlite3.connect('goods.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS goods(
    id INT PRIMARY KEY,
    catalog_id INT UNIQUE,
    name VARCHAR,
    price INT
    )""")
conn.commit()

cur.executemany("INSERT INTO goods VALUES(?,?,?,?)", final_list)
conn.commit()

cur.execute("SELECT name FROM goods")
result = cur.fetchall()


print(result)