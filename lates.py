from flask import Flask, request, render_template, redirect
import sqlite3
conn = sqlite3.connect('lates.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS lates (name TEXT, restrictions TEXT, refrigerate INTEGER, date TEXT)')
c.execute('DELETE FROM lates WHERE date < date("now","localtime")')
conn.commit()
conn.close()

foo = Flask('lates', template_folder='./')

def get_db():
    conn = sqlite3.connect('lates.db')
    c = conn.cursor()
    c.execute('DELETE FROM lates WHERE date < date("now","localtime")')
    c.execute('SELECT * FROM lates')
    db = c.fetchall()
    conn.commit()
    conn.close()
    return db

@foo.route('/', methods=['GET'])
@foo.route('/submit', methods=['GET'])
@foo.route('/delete', methods=['GET'])
def home():
    return render_template('index.html', db = get_db())

@foo.route('/submit', methods=['POST'])
def post_late():
    result = request.form
    name = result['name']
    restrictions = [key for key in result.keys() if key not in ('name','other','refrigerate')]
    if result['other']:
        restrictions.append(result['other'])
    restr = ', '.join(restrictions)
    refr = 1 if 'refrigerate' in result.keys() else 0
    conn = sqlite3.connect('lates.db')
    c = conn.cursor()
    # c.execute('DELETE FROM lates WHERE name = ?', (name,))
    c.execute('INSERT INTO lates VALUES (?,?,?,date("now","localtime"))', (name, restr, refr))
    conn.commit()
    conn.close()
    return redirect('/')

@foo.route('/delete', methods=['POST'])
def delete_late():
    result = request.form
    name = result['delete-name']
    conn = sqlite3.connect('lates.db')
    c = conn.cursor()
    c.execute('DELETE FROM lates WHERE name = ?', (name,))
    conn.commit()
    conn.close()
    return redirect('/')
