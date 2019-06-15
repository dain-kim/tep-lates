from flask import Flask, request, render_template

foo = Flask('lates', template_folder='./')

local_db = {}
# TODO clear at the end of every day

@foo.route('/')
def home():
    return render_template('index.html', db = local_db)

@foo.route('/submit', methods=['POST'])
def post_late():
    result = request.form
    person_name = result['name']
    restrictions = ['refrigerate' in result.keys()]

    for key in result.keys():
        if key not in ('name','other','refrigerate'):
            restrictions.append(key)
    if result['other'] != "":
        restrictions.append(result['other'])
    local_db[person_name] = restrictions

    return render_template("index.html", db = local_db)

@foo.route('/delete', methods=['POST'])
def delete_late():
    result = request.form
    person_name = result['delete-name']
    if person_name in local_db:
        local_db.pop(person_name)
    return render_template("index.html", db = local_db)