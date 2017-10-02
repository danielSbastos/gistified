from flask import render_template, request, redirect, session

from app import app, db
from .models import Gist


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/gists/create', methods=['GET', 'POST'])
def gists_create():
    """
    Create new gist
    """
    if request.method == 'GET':
        return render_template('gists_create.html')
    else:
        title = request.form['title']
        body = request.form['body']
        new_gist = Gist(title, body)

        db.session.add(new_gist)
        db.session.commit()

        return redirect(f'/gist/{new_gist.id}')


@app.route('/gists', methods=['GET'])
def gists():
    """
    List all gists
    """
    return render_template('gists.html')


@app.route('/gist/<id>', methods=['GET'])
def gists_id(id):
    """
    Show single gist
    """
    gist = Gist.query.filter_by(id=id).first()
    return render_template('gist_id.html', gist=gist)
