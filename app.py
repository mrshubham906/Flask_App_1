from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Shubham@2'
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/hello')
def hello_world():
    return render_template('hello.html')

@app.route('/users')
def all_users():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return render_template("users_list.html", users = users)

@app.route('/new_user_form')
def new_user_form():
    return render_template('new_user_form.html')

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    msg = ''
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
                'SELECT * FROM users WHERE id = % s',
                      (id, ))
        user = cursor.fetchone()
        if(user):
            msg = "User already exist"
            print(msg)
        else:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            sql = "INSERT INTO users (id, name, email, role) VALUES (%s, %s, %s, %s)"
            val = (id, name, email, role)
            resp = cursor.execute(sql, val)
            mysql.connection.commit()
            print(resp , val)
            msg = "New user added into database"
    return redirect('/users')

@app.route('/users/<int:id>/',  methods=['GET'])
def getUserByID(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users where id = %s',(id,))
    user = cursor.fetchall()
    print(user)
    if(user == ()):
        return "Not Found"
    else:
        return render_template("users_list.html", users = user)
    
@app.route('/users/search')
def search():
    return render_template('search.html')
    




    

if __name__ == "__main__":
    app.run(debug=True)