import db.connection as connection

cdb = connection.db
cursor = cdb.cursor()
secret_db   = connection.secret_db

# __DROP/DELETE__
def drop_db(db = secret_db, reg = False):
    cursor.execute(f"DROP DATABASE IF EXISTS {db};")
    if reg: print("Database:", cursor.rowcount, "record(s) deleted.")

def drop_table(table, db = secret_db, reg = False):
    cursor.execute(f"DROP TABLE IF EXISTS {db}.{table};")
    if reg: print("Table:", cursor.rowcount, "record(s) deleted.")
    
def delete_row(table, key, value, db = secret_db, reg = False):
    # Rather for deleting by IDs
    cursor.execute(f"DELETE FROM {db}.{table} WHERE {key} = {value}")
    cdb.commit()
    if reg: print(f"{key} {value} was deleted.")

# __CREATE__
def create_db(db = secret_db, dropIfExists = False, reg = False):
    if dropIfExists:
        drop_db(db = db)
    cursor.execute(f"CREATE DATABASE {db};")
    if reg: print("Database:", cursor.rowcount, "record(s) created.")
    
def create_table(table, data, db = secret_db, dropIfExists = False, reg = False):
    if dropIfExists:
        drop_table(table, reg = reg)

    if not table in show_tables(returnValues=True):
        cursor.execute(f"CREATE TABLE {db}.{table}({data});")

        if reg: print("Table:", cursor.rowcount, "record(s) created.")
    elif reg: print(f"Table {table} is already created")
    
## __INSERT__
def insert_table_values(table, keys, values, db = secret_db, reg = False):
    percent_s = ", ".join(["%s" for x in range(len(keys))])
    keys = ", ".join(keys)
    cursor.executemany(
        "INSERT INTO {0}.{1} ({2}) VALUES ({3})"
        .format(db, table, keys, percent_s),
        values
    )
    cdb.commit()
    if reg: print("Table:", cursor.rowcount, "record(s) inserted.")
    
# __POST/UPDATE__
def update_table_value(table, key, replace, db = secret_db, reg = False):
    replace = (replace[1], replace[0]) # old then new
    cursor.execute(
        f"UPDATE {db}.{table} SET {key} = %s WHERE {key} = %s",
        replace
    )
    cdb.commit()
    if reg: print("Table:", cursor.rowcount, "record(s) updated.")

# __SHOW__
def show_tables(db = secret_db, returnValues = False, reg = False):
    cursor.execute(f"SHOW TABLES FROM {db}")
    l = list()
    index = 0
    for x in cursor:
        l.append(x[index])
        index += 1

    if returnValues: return l
    if reg: print(f"TABLES: {l}\nTotal {index} tables.")
        
def show_values(table, key, db = secret_db, limit = "", orderByKey = "", reg = False, returnValues = False):
    if limit != "":
        limit = f" LIMIT {limit}"
    if orderByKey != "":
        orderByKey = f" ORDER BY {orderByKey}";
    cursor.execute(f"SELECT {key} FROM {db}.{table}{orderByKey}{limit}")
    myresult = cursor.fetchall()
    if reg:
        for x in myresult:
            print(x)
        
    if returnValues:
        return myresult
    