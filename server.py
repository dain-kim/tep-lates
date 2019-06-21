from flask import Flask, request, render_template, redirect
import sqlite3
conn = sqlite3.connect('lates.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS lates (name TEXT, restrictions TEXT, refrigerate INTEGER, date TEXT)')
c.execute('DELETE FROM lates WHERE date < date("now")')
conn.commit()
conn.close()


foo = Flask('lates', template_folder='./')

# local_db = {}
# TODO clear at the end of every day
def get_db():
    # print("GETTING DB..")
    conn = sqlite3.connect('lates.db')
    c = conn.cursor()
    c.execute('SELECT * FROM lates WHERE date = date("now")')
    db = c.fetchall() # list of items: [('a', '2019-06-20'), ('b', '2019-06-20')]
    conn.close()
    print('returning', db)
    return db

@foo.route('/', methods=['GET'])
@foo.route('/submit', methods=['GET'])
@foo.route('/delete', methods=['GET'])
def home():
    # return render_template('index.html', db = local_db)
    return render_template('index.html', db = get_db())


@foo.route('/submit', methods=['POST'])
# @foo.route('/', methods=['POST'])
def post_late():
    result = request.form
    print(result)
    person_name = result['name']
    # restrictions = ['refrigerate' in result.keys()]
    # restrictions = []
    # for key in result.keys():
    #     if key not in ('name','other','refrigerate'):
    #         restrictions.append(key)
    # if result['other'] != "":
    #     restrictions.append(result['other'])
    # local_db[person_name] = restrictions
    restrictions = [key for key in result.keys() if key not in ('name','other','refrigerate')]
    if result['other']:
        restrictions.append(result['other'])
    restr = ', '.join(restrictions)

    # SQL TEST
    # restrictions = ', '.join(restrictions)
    conn = sqlite3.connect('lates.db')
    c = conn.cursor()
    refr = 1 if 'refrigerate' in result.keys() else 0
    # c.execute('SELECT * FROM lates WHERE name = ?', (person_name,))
    # if c.fetchall():
    #     c.execute('DELETE FROM lates WHERE name = ?', (person_name,))
    c.execute('DELETE FROM lates WHERE name = ?', (person_name,))
    c.execute('INSERT INTO lates VALUES (?,?,?,date("now"))', (person_name, restr, refr))
    # print("INSERTING")
    conn.commit()
    conn.close()
    # END SQL TEST

    # return render_template("index.html", db = local_db)
    # return render_template('index.html', db = get_db())
    return redirect('/')

@foo.route('/delete', methods=['POST'])
def delete_late():
    result = request.form
    person_name = result['delete-name']
    # if person_name in local_db:
    #     local_db.pop(person_name)
    # SQL TEST
    conn = sqlite3.connect('lates.db')
    c = conn.cursor()
    c.execute('DELETE FROM lates WHERE name = ?', (person_name,))
    conn.commit()
    conn.close()
    # END SQL TEST
    # return render_template("index.html", db = local_db)
    # return render_template('index.html', db = get_db())
    return redirect('/')

# import schedule, time
# def clear_db():
#     print("clearing db...")
#     local_db.clear()
# schedule.every().second.do(clear_db)
# 
# while True:
#     schedule.run_pending()
#     time.sleep(3)

