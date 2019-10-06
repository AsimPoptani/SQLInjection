from flask import Flask, render_template , request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST', 'GET'])
def results():
    if (request.method=='POST' and request.form['results']):
        formResults=request.form['results']
        return render_template('results.html',results=formResults)
    else:
        return render_template('results.html',error=True)

app.run('0.0.0.0',3000, debug=True)