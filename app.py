from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql'  # Update with your MySQL host
app.config['MYSQL_USER'] = 'root'  # Update with your MySQL username
app.config['MYSQL_PASSWORD'] = 'root@123'  # Update with your MySQL password
app.config['MYSQL_DB'] = 'to_do'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tasks')
    tasks = cur.fetchall()
    cur.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    new_task = request.form.get('new_task')
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO tasks (task) VALUES (%s)', (new_task,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

@app.route('/remove/<int:task_id>', methods=['POST'])
def remove_task(task_id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
