from flask import Flask, render_template, redirect, request, url_for

task_title = []
task_description = []

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bootstrap.html', n = len(task_title), task = task_title, description = task_description)


@app.route('/updateform', methods = ['POST', 'GET'])
def updateform():
    return render_template('updatetodo.html', task = task_title, description = task_description)


@app.route('/submit', methods=['POST'])
def submit():
    add_task = request.form.get('title')
    add_desc = request.form.get('description')
    task_title.append(add_task)
    task_description.append(add_desc)
    return redirect(url_for('index'))


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    id = int(request.args.get('item'))
    del task_title[id]
    del task_description[id]
    return redirect(url_for('index'))


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'GET':
        global item
        item = int(request.args.get('item'))
    if request.method == 'POST':
        task_title[item] = request.form.get('updatetitle')
        task_description[item] = request.form.get('updatedesc')
    return render_template('updatetodo.html')



if __name__ == '__main__':
    app.run(debug = True, port = '5000')