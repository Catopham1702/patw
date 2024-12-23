import sqlite3

CONFIG = {
    "default_table": "users",
    "default_column": "username"
}

def get_data_by_config_value(value):
    query = "SELECT * FROM :table WHERE :column"

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(query, {"table": CONFIG["default_table"], "column": CONFIG["default_column"]})
    result = cursor.fetchall()
    connection.close()

    return result

print(get_data_by_config_value("admin"))
