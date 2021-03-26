import sqlite3


def retrieve_bot():
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()

    sql = "SELECT * FROM bots;"
    cursor.execute(sql)

    record = cursor.fetchone()
    db.close()

    print(record)


def retrieve_bots():
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()

    sql = "SELECT * FROM bots;"
    cursor.execute(sql)

    records = cursor.fetchall()
    db.close()

    for record in records:
        print(record)


def run():
    retrieve_bots()

if __name__=="__main__":
    run()