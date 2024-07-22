from flask import Flask, request, redirect, send_from_directory
import psycopg2
from datetime import datetime
import pandas as pd
import os

app = Flask(__name__, static_url_path='', static_folder='.')

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="db",
            database="mydatabase",
            user="myuser",
            password="mypassword"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def save_to_excel(data):
    filename = '/app/submissions.xlsx'

    try:
        if os.path.exists(filename):
            df = pd.read_excel(filename)
            df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)
        else:
            df = pd.DataFrame(data)

        df.to_excel(filename, index=False)
    except Exception as e:
        print(f"Error saving to Excel: {e}")

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    matriculation = request.form['matriculation']
    signature = request.form['signature']
    datetime_submitted = request.form['datetime']

    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute('INSERT INTO students (name, matriculation, signature, datetime_submitted) VALUES (%s, %s, %s, %s)',
                        (name, matriculation, signature, datetime_submitted))
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            print(f"Error saving to database: {e}")

    data = {
        'name': [name],
        'matriculation': [matriculation],
        'signature': [signature],
        'datetime_submitted': [datetime_submitted]
    }
    save_to_excel(data)

    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
