import pymysql

db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='spiders')
cursor = db.cursor()


table = 'students'
condition = 'age > 100'

sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)

try:
    cursor.execute(sql)
    print('删除成功')
    db.commit()
except Exception as e:
    print(f'删除失败: {e}')
    db.rollback()

db.close()


# import pymysql

# db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='spiders')
# cursor = db.cursor()

# data = {
#     'id': '20120007',
#     'name': 'Bob',
#     'age': 120
# }

# table = 'students'

# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))
# sql = 'INSERT INTO {table} ({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)
# update = ', '.join(["{key} = %s".format(key=key) for key in data.keys()])
# sql += update
# try:
#     if cursor.execute(sql, tuple(data.values()) * 2):
#         print('插入成功')
#         db.commit()
# except Exception as e:
#     print(f'插入失败: {e}')
#     db.rollback()
# db.close()









# import pymysql

# db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='spiders')
# cursor = db.cursor()

# data = {
#     'id': '20120007',
#     'name': 'Bob',
#     'age': 20
# }
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))
# sql = 'INSERT INTO {table} ({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)

# try:
#     if cursor.execute(sql, tuple(data.values())):
#         db.commit()
#         print('插入成功')
# except Exception as e:
#     db.rollback()
#     print(f'插入失败: {e}')

# db.close()

# try:
#     cursor.execute(sql, ('1', 'John', 20))
#     db.commit()
#     print('插入成功')
# except:
#     db.rollback()
#     print('插入失败')
    
# try:
#     cursor.execute(sql, ('2', 'John', 20))
#     db.commit()
#     print('插入成功')
# except Exception as e:
#     db.rollback()
#     print(f'插入失败: {e}')

# db.close()



# import pymysql # type: ignore

# db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='spiders')
# cursor = db.cursor()

# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)

# db.close()










# import pymysql

# db = pymysql.connect(host='localhost', user='root', password='', port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# print(cursor.fetchone())

# # 先检查数据库是否存在
# cursor.execute("SHOW DATABASES LIKE 'spiders'")
# if not cursor.fetchone():
#     cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
#     print("Database 'spiders' created successfully")
# else:
#     print("Database 'spiders' already exists")

# db.close()