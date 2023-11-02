from flask import Flask, jsonify
import mysql.connector


app = Flask(__name__)

def write_to_user_data(user_name: str, email: str):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'sgma'
    }
    connection = mysql.connector.connect(config)
    cursor = connection.cursor()
    query = "INSERT INTO user_data (User_Name, Email) VALUES (%s, %s)"
    values = (user_name, email)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

def user_data():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'sgma'
    }
    connection = mysql.connector.connect(config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT User_Name, Email, Register_Date FROM user_data')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

@app.route('/')
def index():
    write_to_user_data("José Venícius Venâncio dos Santos","joseveniciusvs@gmail.com")
    return jsonify({'User Data': user_data()})


if __name__ == 'main':
    app.run(host='0.0.0.0')