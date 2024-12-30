# /mnt/d/testpatchwork/testpatch/patw/index.py

## Summary
This Python script connects to an SQLite database and retrieves data based on a configuration value. It uses hardcoded SQL queries and does not handle user input or errors gracefully.

## Inputs
- None (the function `get_data_by_config_value` is called with a hardcoded string "admin")

## Outputs
- A list of tuples representing rows from the database table specified in the configuration

## Usage
This script can be used to fetch data from an SQLite database using a predefined SQL query. It is not designed for dynamic input or error handling, making it less flexible and potentially unsafe.

```python
import sqlite3

CONFIG = {
    "default_table" : "users", 
    "default_column" : "username" 
}

def get_data_by_config_value(value):
    query = "SELECT * FROM " + CONFIG["default_table"] + " WHERE " + CONFIG["default_column"]

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()

    return result

print(get_data_by_config_value("admin"))
```

### Inputs
- `value`: A string representing the value to filter by in the database.

### Outputs
- Returns a list of tuples, where each tuple represents a row from the database table specified in the configuration.
