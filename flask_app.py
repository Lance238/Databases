
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
            self.cur.execute("INSERT INTO Supplier (SupplierID, SupplierName) VALUES (%s, %s)", (SupplierID, SupplierName
            ))
            self.con.commit()
            self.con.close()
        except pymysql.Error as e:
                #return "Duplicate PK!!!"
                return "Error: " + e.args[1]

        return "OK"


class CustomerDB:
    def __init__(self):
        host = "callumtait78.mysql.pythonanywhere-services.com"
        user = "callumtait78"
        pwd = "Lemon10587"
        db = "callumtait78$GroceryStock"

        self.con = pymysql.connect(host=host, user=user, password = pwd, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def select(self):
        self.cur.execute("SELECT * FROM Customer")
        result = self.cur.fetchall()
        self.con.close()
        return result

    def Customer(self, CustomerID, Name, Email, Address):
        try:
            self.cur.execute("INSERT INTO Customer (CustomerID, Name, Email, Address) VALUES (%s, %s, %s, %s)", (CustomerID, Name, Email, Address))
            self.con.commit()
            self.con.close()
        except pymysql.Error as e:
                #return "Duplicate PK!!!"
                return "Error: " + e.args[1]

        return "OK"

class PaymentDB:
    def __init__(self):
        host = "callumtait78.mysql.pythonanywhere-services.com"
        user = "callumtait78"
        pwd = "Lemon10587"
        db = "callumtait78$GroceryStock"

        self.con = pymysql.connect(host=host, user=user, password = pwd, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def select(self):
        self.cur.execute("SELECT * FROM Payment")
        result = self.cur.fetchall()
        self.con.close()
        return result

    def Payment(self, PaymentID, OrderID, PaymentDate, PaymentAmount, PaymentMethod):
        try:
            self.cur.execute("INSERT INTO Payment (PaymentID, OrderID, PaymentDate, PaymentAmount, PaymentMethod) VALUES (%s, %s, %s, %s, %s)", (PaymentID, OrderID, PaymentDate, PaymentAmount, PaymentMethod))
            self.con.commit()
            self.con.close()
        except pymysql.Error as e:
                #return "Duplicate PK!!!"
                return "Error: " + e.args[1]

        return "OK"

class ProductDB:
    def __init__(self):
        host = "callumtait78.mysql.pythonanywhere-services.com"
        user = "callumtait78"
        pwd = "Lemon10587"
        db = "callumtait78$GroceryStock"

        self.con = pymysql.connect(host=host, user=user, password = pwd, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def select(self):
        self.cur.execute("SELECT * FROM Product")
        result = self.cur.fetchall()
        self.con.close()
        return result

    def Product(self, ProductID, Supplier, ProductName, Price, Stock):
        try:
            self.cur.execute("INSERT INTO Product (ProductID, Supplier, ProductName, Price, Stock) VALUES (%s, %s, %s, %s, %s)", (ProductID, Supplier, ProductName, Price, Stock))
            self.con.commit()
            self.con.close()
        except pymysql.Error as e:
                #return "Duplicate PK!!!"
                return "Error: " + e.args[1]

        return "OK"

class OrderDB:
    def __init__(self):
        host = "callumtait78.mysql.pythonanywhere-services.com"
        user = "callumtait78"
        pwd = "Lemon10587"
        db = "callumtait78$GroceryStock"

        self.con = pymysql.connect(host=host, user=user, password = pwd, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def select(self):
        self.cur.execute("SELECT * FROM Order")
        result = self.cur.fetchall()
        self.con.close()
        return result

    def Order (self, OrderID, CustomerID, PaymentID, OrderDate, OrderPriceAmount):
        try:
            self.cur.execute("INSERT INTO Order (OrderID, CustomerID, PaymentID, OrderDate, OrderPriceAmount) VALUES (%s, %s, %s, %s, %s)", (OrderID, CustomerID, PaymentID, OrderDate, OrderPriceAmount))
            self.con.commit()
            self.con.close()
        except pymysql.Error as e:
                #return "Duplicate PK!!!"
                return "Error: " + e.args[1]

        return "OK"

class OrderItemsDB:
    def __init__(self):
        host = "callumtait78.mysql.pythonanywhere-services.com"
        user = "callumtait78"
        pwd = "Lemon10587"
        db = "callumtait78$GroceryStock"

        self.con = pymysql.connect(host=host, user=user, password = pwd, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def select(self):
        self.cur.execute("SELECT * FROM OrderItems")
        result = self.cur.fetchall()
        self.con.close()
        return result

    def OrderItems(self, OrderItemID, OrderID, ProductID, Quantity, Subtotal):
        try:
            self.cur.execute("INSERT INTO OrderItems (OrderItemID, OrderID, ProductID, Quantity, Subtotal) VALUES (%s, %s, %s, %s, %s)", (OrderItemID, OrderID, ProductID, Quantity, Subtotal))
            self.con.commit()
            self.con.close()
        except pymysql.Error as e:
                #return "Duplicate PK!!!"
                return "Error: " + e.args[1]

        return "OK"

@app.route('/')
def hello_world():
    myvar = 'Grocery Stock'
    return render_template('index.html', msg=myvar)

@app.route('/list')
def list():
    db = Database()
    result = db.select()

    cDB = CustomerDB()
    result2 = cDB.select()

    pDB = PaymentDB()
    result3 = pDB.select()

    prodDB = ProductDB()
    result4 = prodDB.select()

    orderDB = OrderDB()
    result5 = orderDB.select()

    orderItemDB = OrderItemsDB()
    result6 = orderItemDB.select()

    return render_template('results.html', result=result, result2 = result2, result3=result3, result4=result4, result5=result5, result6=result6)

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

        #Access the Customer Table#
        db = CustomerDB()
        msg = db.Customer(CustomerID, Name, Email, Address)

    return render_template('customer.html', msg=msg)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    msg = ""
    if request.method == "POST":
        data = request.form
        PaymentID = data['PaymentID']
        OrderID = data['OrderID']
        PaymentDate = data['PaymentDate']
        PaymentAmount = data['PaymentAmount']
        PaymentMethod = data['PaymentMethod']

        db = PaymentDB()
        msg = db.Payment(PaymentID, OrderID, PaymentDate, PaymentAmount, PaymentMethod)

    return render_template('payment.html', msg=msg)

@app.route('/product', methods=['GET', 'POST'])
def product():
    msg = ""
    if request.method == "POST":
        data = request.form
        ProductID = data['ProductID']
        Supplier = data['Supplier']
        ProductName = data['ProductName']
        Price = data['Price']
        Stock = data['Stock']

        db = ProductDB()
        msg = db.Product(ProductID, Supplier, ProductName, Price, Stock)

    return render_template('product.html', msg=msg)

@app.route('/order', methods=['GET', 'POST'])
def order():
    msg = ""
    if request.method == "POST":
        data = request.form
        OrderID = data['OrderID']
        CustomerID = data['CustomerID']
        PaymentID = data['PaymentID']
        OrderDate = data['OrderDate']
        OrderPriceAmount = data['OrderPriceAmount']

        db = OrderDB()
        msg = db.Order(OrderID, CustomerID, PaymentID, OrderDate, OrderPriceAmount)

    return render_template('order.html', msg=msg)



@app.route('/orderItems', methods=['GET', 'POST'])
def orderItems():
    msg = ""
    if request.method == "POST":
        data = request.form
        OrderItemID = data['OrderItemID']
        OrderID = data['OrderID']
        ProductID = data['ProductID']
        Quantity = data['Quantity']
        Subtotal = data['Subtotal']

        db = OrderItemsDB()
        msg = db.OrderItems(OrderItemID, OrderID, ProductID, Quantity, Subtotal)

    return render_template('orderItems.html', msg=msg)









