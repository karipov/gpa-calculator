import sqlite3

conn = sqlite3.connect('user_classes.db', check_same_thread=False)
c = conn.cursor()

def create_table(message):
    """Create a table within a database based on user ID."""
    uid = message.from_user.id
    query = "CREATE TABLE IF NOT EXISTS user" + str(uid) + "(class TEXT, grade TEXT)"

    c.execute(query)
    conn.commit()

def write_table(subject, grade, message):
    """Insert values into a user table within a database."""
    subject = ''.join(subject) # since both variables come as lists
    grade = ''.join(grade)
    uid = message.from_user.id
    query = "INSERT INTO user" + str(uid) + "(class, grade) VALUES (?, ?)"

    c.execute(query, (subject, grade))
    conn.commit()

def delete_table(message):
    """Delete table for user with user_id"""
    uid = message.from_user.id
    query = "DROP TABLE IF EXISTS user" + str(uid)

    c.execute(query)
    conn.commit()

def pull_data(message):
    """ Pull data from user table if it exists."""
    uid = message.chat.id
    query = "SELECT * FROM user" + str(uid)
    check_table_query = "SELECT name FROM sqlite_master WHERE name = \'user" + str(uid) + "' and type='table'"

    c.execute(check_table_query)

    if not c.fetchall():
        return []

    c.execute(query)

    data = []
    for entry in c.fetchall():
        data.append(list(entry)) # turn tuples into lists (because I like lists)

    return data
