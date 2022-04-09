from database import cursor, db

def add_log(text, user):
    sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")
    cursor.execute(sql, (text, user,))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))

def get_logs():
    sql = ("SELECT * FROM logs ORDER BY created DESC")
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row[1])

def get_log(id):
    sql = ("SELECT * FROM logs WHERE id = %s")
    cursor.execute(sql, (id,))
    result = cursor.fetchone()

    for row in result:
        print(row)

def update_log(id, text):
    sql = ("(%s, %s)")
    cursor.execute(sql, (text, user,))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))

#add_log('This is log one', 'Brad')
#add_log('This is log two', 'Jeff')
#add_log('This is log three', 'Jane')

#get_logs()
get_log(2)