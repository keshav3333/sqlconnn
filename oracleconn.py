import cx_Oracle
import csv
conn=cx_Oracle.Connection('Faculty/Faculty@mother')
cur=conn.cursor()

def createtable():
    query='''create table mcafaculty(id number(2) primary key,name varchar(50))
    '''
    cur.execute(query)
def insertrecord(sid,name):
    record={'id':str(sid),'name':name}
    
    cur.execute("insert into mcafaculty(id,name) values(:id,:name)",record)
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
    for row in records:
        print(row)
    # with open('records.csv','w',newline='') as csvfile:
    #     data=csv.writer(csvfile)
    #     data.writerow(['id','name'])
    #     for row in records:
    #         data.writerow(row)


def fetch_record(sid):
    record={'id':str(sid)}
    query = 'select * from mcafaculty where id = :id'
    cur.execute(query,record)
    record=cur.fetchall()
    for row in record:
        print(row)


def update_name(sid):
    fetch_record(sid)
    name=input('enter new name to update :- ')
    record={'id':str(sid),'name':name}
    query = 'update mcafaculty set name = :name where id = :id'
    cur.execute(query,record)
    conn.commit()
    fetch_record(sid)

def delete_record(sid):
    record={'id':str(sid)}
    query = 'delete from mcafaculty where id = :id'
    cur.execute(query,record)
    conn.commit()

def truncate():
    query ='truncate table mcafaculty'
    cur.execute(query)

def insert_from_csv():
    with open('records.csv','r') as csvfile:
        data=csv.reader(csvfile)
        data= list(data)
        for row in range(1,len(data)):
            insertrecord(*data[row])



