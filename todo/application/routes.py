from application import app, db
from application.models import Todo

@app.route('/add')
def add():
    new_task = Todo(task="task to do")
    db.session.add(new_task)
    db.session.commit()
    return "Added new task onto to do list"

@app.route('/read')
def read():
    all_tasks = Todo.query.all()
    task_string = ""
    for task in all_tasks:
        task_string += "<br>"+ task.task
    return task_string

@app.route('/update/<name>')
def update(task):
    first_task = Todo.query.first()
    first_task.name = name
    db.session.commit()
    return first_task.name

@app.route('/delete')
def delete():
    todo_to_delete = Todo.query.first()
    db.session.delete(todo_to_delete)
    db.session.commit()
    return "deleted todo item"

