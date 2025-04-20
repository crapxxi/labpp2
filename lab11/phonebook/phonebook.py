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
    username = input("Enter the name: ")
    cur.execute(queries['filter'], (f"%{username}%", ))
    checkinf = cur.fetchall()
    phone = input("Enter the phone number: ")
    
    if len(phone) == 12 and phone[0] == '+' and phone[1:12].isdigit():
        if checkinf:
            cur.execute(queries['updatep'], (phone, username))
            conn.commit()
        else:
            cur.execute(queries['insert'],(username, phone))
            conn.commit()
    else:
        print("Invalid phone!")
        input() 
def insert_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(queries['filter'],(f"%{row[0]}%", ))
            checkinf = cur.fetchall()
            if len(row[1]) == 12 and row[1][0] == '+' and row[1][1:12].isdigit():
                if checkinf:
                    cur.execute(queries['updatep'], (row[1],row[0]))
                    conn.commit()
                else:
                    cur.execute(queries['insert'],(row[0],row[1]))
                    conn.commit()

def showusers(filter_value=None):
    if filter_value:
        cur.execute(queries['filter'], (f"%{filter_value}%",))
    else:
        cur.execute(queries['all'])
    rows = cur.fetchall()
    print('='*60)
    print(f"{'Name':<12} {'Phone':<12}")
    for row in rows:
        print(f"{row[1]:<12} {row[2]:<12}")
    print('='*60)

def delete_user(identifier):
    cur.execute(queries['delete'], (identifier,identifier))
    conn.commit()
def insertmanyusers():
    running = True
    print("Enter the name and phone separate by space: ")
    while running:
        try:
            name, phone = input().split(' ')
        except:
            break
        cur.execute(queries['filter'],(f"%{name}%", ))
        checkinf = cur.fetchall()
        if len(phone) == 12 and phone[0] == '+' and phone[1:12].isdigit():
            if checkinf:
                cur.execute(queries['updatep'], (phone, name))
                conn.commit()
            else:
                cur.execute(queries['insert'], (name,phone))
                conn.commit()
def showpagination(limit):
    offset = 0
    while True:
        os.system('clear')
        cur.execute(queries['pagination'], (limit, offset))
        info = cur.fetchall()
        if not info:
            print("No users in this page")
        else:
            print('='*60)
            print(f"{'Name':<12} {'Phone':<12}")
            for inf in info:
                print(f"{inf[1]:<12} {inf[2]:<12}")
            print('='*60)
        print("[n]Next | [p]Previous | [q]Quit")
        action = input("Enter the command: ").lower()
        if action == 'n':
            offset+=limit
        elif action == 'p':
            offset = max(0,offset-limit)
        elif action == 'q':
            break
        else:
            print("Incorrect command.")



if __name__ == '__main__':
    create_table()
    print("PhonEBooK")
    while True:
        os.system("clear")
        print("Enter the query:")
        print("[1]Insert user")
        print("[2]Insert from csv")
        print("[3]Show users")
        print("[4]Delete")
        print("[5]Insert many new users")
        print("[6]Show users with pagination")
        q = input("Enter the number: ")
        match q:
            case '1':
                insert_user()
            case '2':
                filep = input("Enter the file path: ")
                if os.path.exists(filep):
                    insert_from_csv(filep)
                else:
                    print("Invalid path")
                    input()
                    continue
            case '3':
                queryf = input("Enter query filter: ")
                if queryf == '':
                    showusers()
                else:
                    showusers(queryf)
                print("press enter to continue...")
                input()
            case '4':
                showusers()
                id = input("Enter the name or phone: ")
                delete_user(id)
            case '5':
                insertmanyusers()
            case '6':
                try:
                    limit = int(input("Enter the limit(number of users per page): "))
                    showpagination(limit)
                except ValueError:
                    print("Limit and offset must be integers")
                    input()
            case 'q':
                print("BYEBYE")
                quit()
            case _:
                print("Invalid option")
                input()
                continue
