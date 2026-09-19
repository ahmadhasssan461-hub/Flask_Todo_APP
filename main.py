import os
from flask_sqlalchemy import SQLAlchemy 
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

db_url = os.getenv("DATABASE_URL", "sqlite:///Todo.db")
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = db_url
db = SQLAlchemy(app)
class todo(db.Model):
    sno = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200),nullable = False)
    des = db.Column(db.String(500),nullable = False)
    priority = db.Column(db.String(50), nullable=False)  
    def __repr__(self):
        return f"sno is {self.sno} title is {self.title}"
@app.route("/")
def home():
    all_task = todo.query.all()
    return render_template("index.html", tasks=all_task)

@app.route("/add", methods=["POST"])
def add():
    title = request.form["task"]
    date = request.form["date"]
    priority = request.form["priority"]
    
    new_task = todo(title=title, des=date , priority = priority )
    db.session.add(new_task)
    db.session.commit()
    
    return redirect("/")
@app.route("/delete/<int:sno>")
def delete(sno):
    task = todo.query.filter_by(sno=sno).first()
    db.session.delete(task)
    db.session.commit()
    return redirect("/") 
@app.route("/update/<int:sno>")
def update(sno):
    task = todo.query.filter_by(sno=sno).first()
    return render_template("update.html",task=task)
@app.route("/update/<int:sno>", methods=["POST"])
def update_post(sno):
    task = todo.query.filter_by(sno=sno).first()
    task.title = request.form["task"]
    task.des = request.form["date"]
    task.priority = request.form["priority"]
    db.session.commit()
    return redirect("/")
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)