from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__)
global msg

try:
    with sql.connect("database1.db") as con:
        cur = con.cursor()
        cur.execute("CREATE TABLE students(name TEXT, addr TEXT, city TEXT, pin TEXT)")
        cur.execute("INSERT INTO students(name, addr, city, pin) values('John', 'abc123xyz', 'asdf', '12345')")
        con.commit()
        msg = "Record Successfully Added"
except:
    con.rollback()
    msg="Error in Insert Operation"
finally:
    con.close()


@app.route('/')
def showlist():
    return render_template('home.html')


@app.route('/list')
def list():
    con = sql.connect("database1.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("Select * from students")
    rows = cur.fetchall()
    return render_template('list.html', rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
