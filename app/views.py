from app import app


@app.route('/')
def root():
    return 'Hello, World!'
