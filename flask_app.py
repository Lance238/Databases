
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
        try:
            self.cur.execute("INSERT INTO Supplier (SupplierID, SupplierName) VALUES (%s, %s)", (SupplierID, SupplierName))
            self.con.commit()
            self.con.close()
        except pymysql.Error as e:
                #return "Duplicate PK!!!"
                return "Error: " + e.args[1]

        return "OK"

    def customer(self, CustomerID, Name, Email, Address):
        try:
            self.cur.execute("INSERT INTO Customer (CustomerID, Name, Email, Address) VALUES (%s, %s, %s, %s)", (CustomerID, Name, Email, Address))
            self.con.commit()
            self.con.close()
        except pymysql.Error as e:
                #return "Duplicate PK!!!"
                return "Error: " + e.args[1]

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



@app.route('/customer', methods=['GET', 'POST'])
def customer():
    msg = ""
    if request.method == "POST":
        data = request.form
        CustomerID = data['CustomerID']
        Name = data['Name']
        Email = data['Email']
        Address = data['Address']

        db = Database()
        msg = db.Customer(CustomerID, Name, Email, Address)

    return render_template('customer.html', msg=msg)





