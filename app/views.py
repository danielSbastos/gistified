from flask import render_template, request, redirect

from app import app, db
from .models import Gist


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/gists/create', methods=['GET', 'POST'])
def gists_create():
    if request.method == 'GET':
        return render_template('gists_create.html')
    else:
        title = request.form['title']
        body = request.form['body']
        new_gist = Gist(title, body)

        db.session.add(new_gist)
        db.session.commit()

        return redirect("/gists/create")
