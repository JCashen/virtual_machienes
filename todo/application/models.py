from application import db

class Todo(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))
