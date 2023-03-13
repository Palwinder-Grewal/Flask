from flask import Flask, render_template, redirect, request, url_for
import json


def refresh_data():
    with open ('todo_data.json', 'r') as f:
        reading = f.read()
        data = json.loads(reading)
    global mydict
    mydict = data
    return mydict

def update_json():
    with open ('todo_data.json', 'w') as f:
        update_json = json.dumps(mydict)
        f.write(update_json)


app = Flask(__name__)

@app.route('/')
def index():
    mydict = refresh_data()
    return render_template('bootstrap.html', n = len(mydict['title']), task = mydict['title'], description = mydict['desc'])


@app.route('/updateform')
def updateform():
    return render_template('updatetodo.html', task = mydict['title'], description = mydict['desc'])


@app.route('/submit', methods=['GET','POST'])
def submit():
    mydict = refresh_data()
    add_task = request.form.get('title')
    add_desc = request.form.get('description')
    mydict['title'].append(add_task)
    mydict['desc'].append(add_desc)
    update_json()

    return redirect(url_for('index'))

@app.route('/delete', methods=['GET'])
def delete():
    id = int(request.args.get('item'))
    mydict['title'].pop(id)
    mydict['desc'].pop(id)
    with open ('todo_data.json', 'w')as f:
        update_json = json.dumps(mydict)
        f.write(update_json)

    return redirect(url_for('index'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'GET':
        global to_update
        to_update = int(request.args.get('item'))

    if request.method == 'POST':
        update_task = request.form.get('updatetitle')
        update_desc = request.form.get('updatedesc')
        mydict['title'][to_update] = update_task
        mydict['desc'][to_update] = update_desc

        update_json()    
    return render_template('updatetodo.html', )



if __name__ == '__main__':
    app.run(debug = True, port = '5000')