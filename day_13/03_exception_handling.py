# try ... except ... finally


def open_db():
    return "connection"


def insert_data(conn, data):
    a = 5 / 0
    print(f"Inserting data -> {data}")
    return conn


def close_db(conn):
    return conn


try:
    conn = open_db()
    data = ["Rututja", 26]
    conn = insert_data(conn, data)
except Exception as err:
    print(err)
finally:
    print("Closing connection")

# Baseclass -> Child
# Exception -> ZeroDivisionError    
