from flask import Flask, render_template, request, redirect, url_for
from models import db, Project


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///portfolio.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects = projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get(project_id)
    return render_template('project_detail.html', project = project)

@app.route('/add_project', methods = ['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image_url = request.form['image_url']
        link = request.form['link']

        new_project = Project(title = title, description = description, image_url = image_url, link = link)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_project.html')

if __name__ == '__main__':
    app.run(debug=True)