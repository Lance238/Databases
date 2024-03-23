
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import pymysql

app = Flask(__name__, template_folder="templates")

##### DATABASE #####

class Database:
    def __init__(self):
        host = "callumtait78.mysql.pythonanywhere-services.com"
        user = "callumtait78"
        pwd = "Lemon10587"
        db = "callumtait78$GroceryStock"

        self.con = pymysql.connect(host=host, user=user, password = pwd, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def select(self):
        self.cur.execute("SELECT * FROM Supplier")
        result = self.cur.fetchall()
        self.con.close()
        return result

    def insert(self, SupplierID, SupplierName):
        self.cur.execute("INSERT INTO Supplier (SupplierID, SupplierName) VALUES (%s, %s)", (SupplierID, SupplierName))
        self.con.commit()
        self.con.close()

        return "OK"



@app.route('/')
def hello_world():
    myvar = 'INFR3810'
    return render_template('index.html', msg=myvar)

@app.route('/list')
def list():
    db = Database()
    result = db.select()
    return render_template('results.html', result=result)

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    msg = ""
    if request.method == "POST":
        data = request.form
        SupplierID = data['SupplierID']
        SupplierName = data['SupplierName']

        db = Database()
        msg = db.insert(SupplierID, SupplierName)


    return render_template('form.html', msg=msg)



