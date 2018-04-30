import pymysql

pswd = input('Insert password:')
params = {
    'user': 'root',
    'password' : pswd,
    'host' : 'localhost',
    'database' : 'to_do_list',
    'use_unicode' : True
}


sql_insert = 'INSERT INTO todo_list (todo) VALUES (%s)'
sql_insert_urgent = 'INSERT INTO todo_list (todo,urgent)' \
                    ' VALUES (%s,%s)'
sql_get_id = 'SELECT * ' \
      'FROM todo_list ' \
      'WHERE id_task = %s'
sql_get_name = 'SELECT * ' \
             'FROM todo_list ' \
             'WHERE todo = %s'
sql_showall = 'SELECT * FROM todo_list'
sql_delete = 'DELETE FROM todo_list WHERE id_task = %s'
sql_match = 'SELECT * FROM todo_list WHERE todo LIKE %s'
sql_remove_all = 'DELETE FROM todo_list WHERE todo LIKE %s'
sql_update = 'UPDATE todo_list SET todo = %s, urgent = %s WHERE id_task = %s'


def insert(name):
    conn = pymysql.connect(**params)
    cursor = conn.cursor()
    cursor.execute(sql_insert,(name,))
    conn.commit()
    cursor.close()
    conn.close()

def insert_urgent(name):
    conn = pymysql.connect(**params)
    cursor = conn.cursor()
    cursor.execute(sql_insert_urgent,(name,True))
    conn.commit()
    cursor.close()
    conn.close()

def remove(id):
    conn = pymysql.connect(**params)
    cursor = conn.cursor()
    cursor.execute(sql_get_id, (id,))
    if cursor.fetchone() == None:
        print("Not in the database")
    else:
        cursor.execute(sql_delete,(id,))
        conn.commit()
    cursor.close()
    conn.close()

def check_name(name):
    res = False
    conn = pymysql.connect(**params)
    cursor = conn.cursor()
    cursor.execute(sql_get_name, (name,))
    if cursor.fetchone() != None:
        res = True
    cursor.close()
    conn.close()
    return res

def check_id(id):
    res = False
    conn = pymysql.connect(**params)
    cursor = conn.cursor()
    cursor.execute(sql_get_id, (id,))
    if cursor.fetchone() != None:
        res = True
    cursor.close()
    conn.close()
    return res

def match(name):
    conn = pymysql.connect(**params)
    cursor = conn.cursor()
    name = "%"+name+"%"
    cursor.execute(sql_match, (name,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def removeAll(name):
    conn = pymysql.connect(**params)
    cursor = conn.cursor()
    name = "%" + name + "%"
    cursor.execute(sql_remove_all, (name,))
    conn.commit()
    cursor.close()
    conn.close()


def showAll():
    conn = pymysql.connect(**params)
    cursor = conn.cursor()
    cursor.execute(sql_showall)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_id(id):
    conn = pymysql.connect(**params)
    cursor = conn.cursor()
    cursor.execute(sql_get_id, (id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def get_name(name):
    conn = pymysql.connect(**params)
    cursor = conn.cursor()
    cursor.execute(sql_get_name, (name,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update(id, new_todo, new_status):
    conn = pymysql.connect(**params)
    cursor = conn.cursor()
    cursor.execute(sql_update, (new_todo,new_status,id))
    conn.commit()
    cursor.close()
    conn.close()
