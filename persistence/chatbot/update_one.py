import sqlite3


def get_bot_id_from_user():
    print("Please enter a bot id:")
    return int(input())


def display_bot_from_db(id):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()

    sql = f"SELECT * FROM bots WHERE id={id}"
    cursor.execute(sql)
    record = cursor.fetchone()
    db.close()

    print(record)


def get_bot_details_from_user():
    print("Which field?")
    field = input()
    print("New value?")
    value = input()
    return [field, value]


def update_bot_in_db(data, id):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()

    sql = f"UPDATE bots SET {data[0]}='{data[1]}' WHERE id = {id}"
    cursor.execute(sql)
    db.commit()
    db.close()

    print("Updated")


def run():
    id = get_bot_id_from_user()
    display_bot_from_db(id)

    data = get_bot_details_from_user()
    update_bot_in_db(data, id)


if __name__ == "__main__":
    run()