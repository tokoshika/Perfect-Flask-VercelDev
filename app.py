from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/deploy')
def deploy():
    return render_template('deploy.html')

if __name__ == "__main__":
    app.run()