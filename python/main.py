import mysql.connector
import json

mydb = mysql.connector.connect(
  host="myhost",
  user="admin",
  password="password123",
  database="admin"
)

def get_users(users=[]):
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM customers WHERE username = {users}")
    myresult = mycursor.fetchall()
    return myresult

def login(username, password):
    print(f'log in user {username} with password {password}')
    try:
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM customers WHERE username = {username}")
        myresult = mycursor.fetchone()
        if myresult['password'] is password:
            return myresult
        else:
            return False
    except:
        pass


def main(event, context):
    if event['path'] == "/login":
        username = event.get('queryStringParameters').get('username')
        password = event.get('queryStringParameters').get('password')
        result = login(username, password)
        response = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': result,
        } 

        return response


    if event['path'] == "/users":
        userList = event.get('queryStringParameters').get('users')
        user_list = userList.split(',')
        users = get_users(users=user_list)
        response = {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(users),
        }

        return response

main()
