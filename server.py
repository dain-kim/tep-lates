from flask import Flask, request, render_template

foo = Flask('lates', template_folder='./')

local_db = {}
# food_args = ['beef','chicken','']

@foo.route('/submit', methods=['POST'])
def post_late():
    result = request.form
    # local_db[result['name']] = result
    person_name = result['name']
    restrictions = []
    for key in result.keys():
        if key != 'name' and key != 'other':
            restrictions += [key]
    if result['other'] != "":
        restrictions += [result['other']]
    local_db[person_name] = restrictions
    return render_template("index.html", db = local_db)

@foo.route('/')
def bar():
    return render_template('index.html', db = local_db)

@foo.route('/delete', methods=['POST'])
def delete_late():
    result = request.form
    person_name = result['delete-name']
    if person_name in local_db:
        local_db.pop(person_name)
    return render_template("index.html", db = local_db)