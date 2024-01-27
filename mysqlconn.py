import pymysql
import csv
conn=pymysql.Connection(
    user='root',
    password='root',
    host='localhost',
    port=3306,
    db='sqlconn')
cur=conn.cursor()
def createtable():
    query='''create table mcafaculty(id int primary key,name varchar(50))
    '''
    cur.execute(query)
def insertrecord(sid,name):
    record=[sid,name]
    
    cur.execute("insert into mcafaculty(id,name) values(%s,%s)",record)
    conn.commit()
# insertrecord(3,'kataramma')
# insertrecord(4,'kanaka')
# insertrecord(5,'kamakshi')
# insertrecord(6,'kamalakshi')
# insertrecord(7,'kavya')
    
def read_records():
    query = 'select * from mcafaculty'
    cur.execute(query)
    records = cur.fetchall()
    with open('records.csv','w',newline='') as csvfile:
        data=csv.writer(csvfile)
        data.writerow(['id','name'])
        for row in records:
            data.writerow(row)
        

def fetch_record(sid):
    
    query = 'select * from mcafaculty where id = %s'
    cur.execute(query,sid)
    record=cur.fetchall()
    for row in record:
        print(row)
def update_name(sid):
    fetch_record(sid)
    name=input('enter new name to update :- ')
    record=[name,sid]
    query = 'update mcafaculty set name = %s where id = %s'
    cur.execute(query,record)
    conn.commit()
    fetch_record(sid)
def delete_record(sid):
    query = 'delete from mcafaculty where id = %s'
    cur.execute(query,sid+)
    conn.commit()

