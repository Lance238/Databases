
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import pymysql

app = Flask(__name__, template_folder="templates")

##### SUPPLIER DATABASE #####

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

    def delete_Supplier(self, SupplierID):

        self.cur.execute("DELETE FROM Supplier WHERE SupplierID = %s", (SupplierID, ))
        self.con.commit()
        self.con.close()

        return "Ok"

    def modify_Supplier(self, SupplierID, SupplierName):

        self.cur.execute("UPDATE Supplier SET SupplierName = %s WHERE SupplierID = %s", (SupplierName, SupplierID))
        self.con.commit()
        self.con.close()

        return "Ok"

##### CUSTOMER DATABASE #####

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

    def delete_Customer(self, CustomerID):

        self.cur.execute("DELETE FROM Customer WHERE CustomerID = %s", (CustomerID, ))
        self.con.commit()
        self.con.close()

        return "Ok"

    def modify_Customer(self, CustomerID, Name, Email, Address):

        self.cur.execute("UPDATE Customer SET Name = %s WHERE CustomerID = %s", (Name, CustomerID))
        self.cur.execute("UPDATE Customer SET Email = %s WHERE CustomerID = %s", (Email, CustomerID))
        self.cur.execute("UPDATE Customer SET Address = %s WHERE CustomerID = %s", (Address, CustomerID))
        self.con.commit()
        self.con.close()

        return "Ok"


##### PAYMENT DATABASE #####

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

    def Payment(self, PaymentID, PaymentDate, PaymentAmount, PaymentMethod):
        try:
            self.cur.execute("INSERT INTO Payment (PaymentID, PaymentDate, PaymentAmount, PaymentMethod) VALUES (%s, %s, %s, %s)", (PaymentID, PaymentDate, PaymentAmount, PaymentMethod))
            self.con.commit()
            self.con.close()
        except pymysql.Error as e:
                #return "Duplicate PK!!!"
                return "Error: " + e.args[1]

        return "OK"

    def delete_Payment(self, PaymentID):

        self.cur.execute("DELETE FROM Payment WHERE PaymentID = %s", (PaymentID, ))
        self.con.commit()
        self.con.close()

        return "Ok"

    def modify_Payment(self, PaymentID, PaymentDate, PaymentAmount, PaymentMethod):

        self.cur.execute("UPDATE Payment SET PaymentDate = %s WHERE PaymentID = %s", (PaymentDate, PaymentID))
        self.cur.execute("UPDATE Payment SET PaymentAmount = %s WHERE PaymentID = %s", (PaymentAmount, PaymentID))
        self.cur.execute("UPDATE Payment SET PaymentMethod = %s WHERE PaymentID = %s", (PaymentMethod, PaymentID))
        self.con.commit()
        self.con.close()

        return "Ok"



##### PRODUCT DATABASE #####
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

    def delete_Product(self, ProductID):

        self.cur.execute("DELETE FROM Product WHERE ProductID = %s", (ProductID, ))
        self.con.commit()
        self.con.close()

        return "Ok"

    def modify_Product(self, ProductID, Supplier, ProductName, Price, Stock):

        self.cur.execute("UPDATE Product SET Supplier = %s WHERE ProductID = %s", (Supplier, ProductID))
        self.cur.execute("UPDATE Product SET ProductName = %s WHERE ProductID = %s", (ProductName, ProductID))
        self.cur.execute("UPDATE Product SET Price = %s WHERE ProductID = %s", (Price, ProductID))
        self.cur.execute("UPDATE Product SET Stock = %s WHERE ProductID = %s", (Stock, ProductID))
        self.con.commit()
        self.con.close()

        return "Ok"



##### ORDER DATABASE #####
class OrdersDB:
    def __init__(self):
        host = "callumtait78.mysql.pythonanywhere-services.com"
        user = "callumtait78"
        pwd = "Lemon10587"
        db = "callumtait78$GroceryStock"

        self.con = pymysql.connect(host=host, user=user, password = pwd, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def select(self):
        self.cur.execute("SELECT * FROM Orders")
        result = self.cur.fetchall()
        self.con.close()
        return result

    def Orders (self, OrderID, CustomerID, PaymentID, OrderDate, OrderPriceAmount):
        try:
            self.cur.execute("INSERT INTO Orders (OrderID, CustomerID, PaymentID, OrderDate, OrderPriceAmount) VALUES (%s, %s, %s, %s, %s)", (OrderID, CustomerID, PaymentID, OrderDate, OrderPriceAmount))
            self.con.commit()
            self.con.close()
        except pymysql.Error as e:
                #return "Duplicate PK!!!"
                return "Error: " + e.args[1]

        return "OK"

    def delete_Orders(self, OrderID):

        self.cur.execute("DELETE FROM Orders WHERE OrderID = %s", (OrderID, ))
        self.con.commit()
        self.con.close()

        return "Ok"

    def modify_Orders(self, OrderID, CustomerID, PaymentID, OrderDate, OrderPriceAmount):

        self.cur.execute("UPDATE Orders SET CustomerID = %s WHERE OrderID = %s", (CustomerID, OrderID))
        self.cur.execute("UPDATE Orders SET PaymentID = %s WHERE OrderID = %s", (PaymentID, OrderID))
        self.cur.execute("UPDATE Orders SET OrderDate = %s WHERE OrderID = %s", (OrderDate, OrderID))
        self.cur.execute("UPDATE Orders SET OrderPriceAmount = %s WHERE OrderID = %s", (OrderPriceAmount, OrderID))
        self.con.commit()
        self.con.close()

        return "Ok"





##### ORDER ITEMS DATABASE #####
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

    def delete_OrderItems(self, OrderItemsID):

        self.cur.execute("DELETE FROM OrderItems WHERE OrderItemID = %s", (OrderItemsID, ))
        self.con.commit()
        self.con.close()

        return "Ok"

    def modify_OrderItems(self, OrderItemID, OrderID, ProductID, Quantity, Subtotal):

        self.cur.execute("UPDATE OrderItems SET OrderID = %s WHERE OrderItemID = %s", (OrderID, OrderItemID))
        self.cur.execute("UPDATE OrderItems SET ProductID = %s WHERE OrderItemID = %s", (ProductID, OrderItemID))
        self.cur.execute("UPDATE OrderItems SET Quantity = %s WHERE OrderItemID = %s", (Quantity, OrderItemID))
        self.cur.execute("UPDATE OrderItems SET Subtotal = %s WHERE OrderItemID = %s", (Subtotal, OrderItemID))
        self.con.commit()
        self.con.close()

        return "Ok"

#################################################################################################################################################################################################################################################

@app.route('/')
def hello_world():
    myvar = 'Grocery Stock Database'
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

    ordersDB = OrdersDB()
    result5 = ordersDB.select()

    orderItemDB = OrderItemsDB()
    result6 = orderItemDB.select()

    return render_template('results.html', result=result, result2 = result2, result3=result3, result4=result4, result5=result5, result6=result6)


##### SUPPLIER #####
@app.route('/supplier', methods=['GET', 'POST'])
def insert():
    msg = ""
    if request.method == "POST":
        data = request.form
        SupplierID = data['SupplierID']
        SupplierName = data['SupplierName']

        db = Database()
        msg = db.insert(SupplierID, SupplierName)

    return render_template('form.html', msg=msg)

@app.route('/delete', methods=['GET', 'POST'])
def deleteSupplier():
    msg = ""
    if request.method == "POST":
        data = request.form
        SupplierID = data['SupplierID']

        db = Database()
        msg = db.delete_Supplier(SupplierID)

    return render_template('deleteSupplier.html', msg=msg)

@app.route('/modify', methods=['GET', 'POST'])
def modifySupplier():
    msg = ""
    if request.method == "POST":
        data = request.form
        SupplierID = data['SupplierID']
        SupplierName = data['SupplierName']

        db = Database()
        msg = db.modify_Supplier(SupplierID, SupplierName)

    return render_template('modifySupplier.html', msg=msg)




##### CUSTOMER #####
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

@app.route('/deleteCustomer', methods=['GET', 'POST'])
def deleteCustomer():
    msg = ""
    if request.method == "POST":
        data = request.form
        CustomerID = data['CustomerID']

        db = CustomerDB()
        msg = db.delete_Customer(CustomerID)

    return render_template('deleteCustomer.html', msg=msg)

@app.route('/modifyCustomer', methods=['GET', 'POST'])
def modifyCustomer():
    msg = ""
    if request.method == "POST":
        data = request.form
        CustomerID = data['CustomerID']
        Name = data['Name']
        Email = data['Email']
        Address = data['Address']

        db = CustomerDB()
        msg = db.modify_Customer(CustomerID, Name, Email, Address)

    return render_template('modifyCustomer.html', msg=msg)





##### PAYMENT #####
@app.route('/payment', methods=['GET', 'POST'])
def payment():
    msg = ""
    if request.method == "POST":
        data = request.form
        PaymentID = data['PaymentID']
        PaymentDate = data['PaymentDate']
        PaymentAmount = data['PaymentAmount']
        PaymentMethod = data['PaymentMethod']

        db = PaymentDB()
        msg = db.Payment(PaymentID, PaymentDate, PaymentAmount, PaymentMethod)

    return render_template('payment.html', msg=msg)


@app.route('/deletePayment', methods=['GET', 'POST'])
def deletePayment():
    msg = ""
    if request.method == "POST":
        data = request.form
        PaymentID = data['PaymentID']

        db = PaymentDB()
        msg = db.delete_Payment(PaymentID)

    return render_template('deletePayment.html', msg=msg)

@app.route('/modifyPayment', methods=['GET', 'POST'])
def modifyPayment():
    msg = ""
    if request.method == "POST":
        data = request.form
        PaymentID = data['PaymentID']
        PaymentDate = data['PaymentDate']
        PaymentAmount = data['PaymentAmount']
        PaymentMethod = data['PaymentMethod']

        db = PaymentDB()
        msg = db.modify_Payment(PaymentID, PaymentDate, PaymentAmount, PaymentMethod)

    return render_template('modifyPayment.html', msg=msg)




##### PRODUCT #####
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

@app.route('/deleteProduct', methods=['GET', 'POST'])
def deleteProduct():
    msg = ""
    if request.method == "POST":
        data = request.form
        ProductID = data['ProductID']

        db = ProductDB()
        msg = db.delete_Product(ProductID)

    return render_template('deleteProduct.html', msg=msg)

@app.route('/modifyProduct', methods=['GET', 'POST'])
def modifyProduct():
    msg = ""
    if request.method == "POST":
        data = request.form
        ProductID = data['ProductID']
        Supplier = data['Supplier']
        ProductName = data['ProductName']
        Price = data['Price']
        Stock = data['Stock']

        db = ProductDB()
        msg = db.modify_Product(ProductID, Supplier, ProductName, Price, Stock)

    return render_template('modifyProduct.html', msg=msg)

##### ORDERS #####
@app.route('/orders', methods=['GET', 'POST'])
def orders():
    msg = ""
    if request.method == "POST":
        data = request.form
        OrderID = data['OrderID']
        CustomerID = data['CustomerID']
        PaymentID = data['PaymentID']
        OrderDate = data['OrderDate']
        OrderPriceAmount = data['OrderPriceAmount']

        db = OrdersDB()
        msg = db.Orders(OrderID, CustomerID, PaymentID, OrderDate, OrderPriceAmount)

    return render_template('order.html', msg=msg)

@app.route('/deleteOrders', methods=['GET', 'POST'])
def deleteOrders():
    msg = ""
    if request.method == "POST":
        data = request.form
        OrderID = data['OrderID']

        db = OrdersDB()
        msg = db.delete_Orders(OrderID)

    return render_template('deleteOrders.html', msg=msg)

@app.route('/modifyOrders', methods=['GET', 'POST'])
def modifyOrders():
    msg = ""
    if request.method == "POST":
        data = request.form
        OrderID = data['OrderID']
        CustomerID = data['CustomerID']
        PaymentID = data['PaymentID']
        OrderDate = data['OrderDate']
        OrderPriceAmount = data['OrderPriceAmount']

        db = OrdersDB()
        msg = db.modify_Orders(OrderID, CustomerID, PaymentID, OrderDate, OrderPriceAmount)

    return render_template('modifyOrders.html', msg=msg)



##### ORDER ITEMS #####
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


@app.route('/deleteOrderItems', methods=['GET', 'POST'])
def deleteOrderItems():
    msg = ""
    if request.method == "POST":
        data = request.form
        OrderItemsID = data['OrderItemsID']

        db = OrderItemsDB()
        msg = db.delete_OrderItems(OrderItemsID)

    return render_template('deleteOrderItems.html', msg=msg)

@app.route('/modifyOrderItems', methods=['GET', 'POST'])
def modifyOrderItems():
    msg = ""
    if request.method == "POST":
        data = request.form
        OrderItemID = data['OrderItemID']
        OrderID = data['OrderID']
        ProductID = data['ProductID']
        Quantity = data['Quantity']
        Subtotal = data['Subtotal']

        db = OrderItemsDB()
        msg = db.modify_OrderItems(OrderItemID, OrderID, ProductID, Quantity, Subtotal)

    return render_template('modifyOrderItems.html', msg=msg)










