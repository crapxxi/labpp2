#PhoneBook
import psycopg2
import csv
import os
import json

with open('sqlcodes.json','r') as f:
    queries = json.load(f)

conn = psycopg2.connect(
    host = 'localhost',
    database = 'phonedb',
    user = 'postgres',
    password = 'admin'
)
cur = conn.cursor()

def create_table():
    cur.execute(queries['create_table'])
    conn.commit()
def insert_user():
    username = input("Enter your username: ")
    phone = input("Enter your phone number: ")
    cur.execute(queries['insert'],(username, phone))
    conn.commit()
def insert_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(queries['insert'],(row[0],row[1]))
    conn.commit()
def update_user(old_name, new_name=None, new_phone=None):
    if new_name:
        cur.execute(queries['updaten'], (new_name, old_name))
    if new_phone:
        cur.execute(queries['updatep'], (new_phone, new_name or old_name))
    conn.commit()
def query_users(filter_value=None):
    if filter_value:
        cur.execute(queries['filter'], (f"%{filter_value}%", f"%{filter_value}%"))
    else:
        cur.execute(queries['all'])
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_user(identifier):
    cur.execute(queries['delete'], (identifier,))
    conn.commit()

if __name__ == '__main__':
    create_table()
    print("PhonEBooK")
    while True:
        print("Enter the query:")
        print("[1]Insert user")
        print("[2]Insert from csv")
        print("[3]Update user")
        print("[4]Query with filter")
        print("[5]Delete")
        q = input("Enter the number: ")
        match q:
            case '1':
                insert_user()
            case '2':
                filep = input("Enter the file path: ")
                if os.path.exists(filep):
                    insert_from_csv(filep)
                else:
                    print("Invald path")
                    continue
            case '3':
                query = input("Wanna enter new name or phone?[type n or p]:")
                oname = input("Enter name: ")
                if query == 'n':
                    nname = input("Enter new name: ")
                    update_user(oname,nname)
                elif query == 'p':
                    phonen = input("Enter phone number: ")
                    update_user(oname,None,phonen)
                else:
                    print("Invalid operation")
            case '4':
                queryf = input("Enter query filter: ")
                if queryf == '':
                    query_users()
                else:
                    query_users(queryf)
            case '5':
                id = input("Enter the name: ")
                delete_user(id)
            case 'q':
                print("BYEBYE")
                quit()
            case _:
                print("Invalid option")
                continue
        print("Completed!")