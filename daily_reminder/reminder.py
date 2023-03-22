import psycopg2
import requests
import datetime
import time
import db
from config import TOKEN, my_id

conn = psycopg2.connect("dbname=reminder_app user=postgres password=qwerty123 host=ovz3.j90259871.0n03n.vps.myjino.ru port=49321") # 9010
cursor = conn.cursor()


while True:
    reminds = db.sel(cursor)
    time_now = str(datetime.datetime.now().strftime("%H:%M"))

    for i in reminds:
        remind_time = i[3]
        remind_time = remind_time.strftime("%H:%M")
        if i[4] != True:
            print(i[4])
        if remind_time == time_now:
            send = f'https://api.telegram.org/bot{TOKEN}/sendmessage?chat_id={i[1]}&text={i[2]} {i[3]}'
            requests.post(send)
            if i[4] != True:
                db.dele(conn, cursor, i[3])
    time.sleep(60)
        
    

cursor.close()
conn.close()
