def sel(cursor):
        cursor.execute("SELECT * FROM reminds")
        result = cursor.fetchall()
        return result

def ins(conn, cursor, user_tg_id, remind_note, remind_time):
        
        a = sel(cursor)
        iter = 0
        for i in a:
            if iter < i[0]:
                iter = i[0]
        iter += 1
        cursor.execute(f"INSERT INTO reminds (id, user_tg_id, remind_note, remind_time) VALUES ({iter}, {user_tg_id}, '{remind_note}', '{remind_time}')")
        conn.commit()
        print('готово')

def dele(conn, cursor, remind_time):
        cursor.execute(f"DELETE FROM reminds WHERE remind_time = '{remind_time}'")
        conn.commit()