from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global task list
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_text = request.form.get('task')
    if task_text:
        tasks.append({'text': task_text, 'done': False})
    return redirect(url_for('index'))

@app.route('/toggle/<int:index>')
def toggle_done(index):
    tasks[index]['done'] = not tasks[index]['done']
    return redirect(url_for('index'))

@app.route('/clear')
def clear_tasks():
    tasks.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
