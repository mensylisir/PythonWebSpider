import pymysql
data = {
    'id': '10003',
    'name': 'Andy',
    'age': 25,
    'address':'Beijing'
}
table = 'person'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
db = pymysql.connect(host='localhost', user='mensyli4',
                    password='xiaoming98', port=3306, db='person')
cursor = db.cursor()
sql = '''INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE''' \
            .format(table=table, keys=keys, values=values)
print(sql)
try:
    cursor.execute(sql, tuple(data.values()))
    db.commit()
except:
    db.rollback()
finally:
    db.close()
