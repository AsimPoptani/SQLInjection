from flask import Flask, render_template , request
import mysql.connector
app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="rookie",
  passwd="rookie",
  database="employees"
)
mycursor = mydb.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/3ast3r3gg')
def easterEgg():
    return render_template('3ast3r3gg.html')

@app.route('/results', methods=['POST', 'GET'])
def results():
    if (request.form['results']):
        formResults=request.form['results']
        c=mycursor.execute("select first_name, last_name,hire_date from employees where emp_no ="+formResults+";",multi=True)
        for a in c:
            print(a)
            result=a.fetchall()
        print(result)
        return render_template('results.html',results=result)
    else:
        return render_template('results.html',error=True)

app.run('0.0.0.0',3000, debug=True)