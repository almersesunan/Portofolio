from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:admin@localhost:5432/postgres"
db = SQLAlchemy(app)

#create table
class User(db.Model):
    __table_args__ = {"schema": "digital_skola"}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(30))
    address = db.Column(db.String(50))

    def __init__(self, username, email, address):
        self.username = username
        self.email = email
        self.address = address

class Product(db.Model):
    __table_args__ = {"schema": "digital_skola"}
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), unique=True)
    product_price = db.Column(db.Numeric(19,2))
    product_qty = db.Column(db.Integer)
    
    def __init__(self, product_name, product_price, product_qty):
        self.product_name = product_name
        self.product_price = product_price
        self.product_qty = product_qty

class Order(db.Model):
    __table_args__ = {"schema": "digital_skola"}
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True)
    product_id = db.Column(db.Integer, unique=True)

    def __init__(self, user_id, product_id):
        self.user_id = user_id
        self.product_id = product_id

#user_orm
@app.route("/user", methods=["GET", "POST"])
def api_user():
    if request.method == "GET":
        data = User.query.all()
        result = []
        for d in data:
            res = {"username": d.username, "email": d.email, "address": d.address}
            result.append(res)
            
        return jsonify(result)

    elif request.method == "POST":
        data = request.get_json()
        for d in data:
            user = User(username=d.get("username"), email=d.get("email"), address=d.get("address"))
            db.session.add(user)
        db.session.commit()

        return jsonify({"message": "data berhasil ditambahkan!"})

@app.route("/user/<id>", methods=["GET"])
def api_user_onlyone(id):
    try:
        data = db.session.query(User).get(id)
        result = {"username": data.username, "email": data.email, "address": data.address}
        return jsonify(result)
    except:
        return jsonify({"message": "id tidak ditemukan!"})

#product_orm
@app.route("/product", methods=["GET", "POST"])
def api_product():
    if request.method == "GET":
        data = Product.query.all()
        result = []
        for d in data:
            res = {"product_name": d.product_name, "product_price": d.product_price, "product_qty": d.product_qty}
            result.append(res)
            
        return jsonify(result)

    elif request.method == "POST":
        data = request.get_json()
        for d in data:
            product = Product(product_name=d.get("product_name"), product_price=d.get("product_price"), product_qty=d.get("product_qty"))
            db.session.add(product)
        db.session.commit()

        return jsonify({"message": "data berhasil ditambahkan!"})

@app.route("/product/<id>", methods=["GET"])
def api_product_onlyone(id):
    try:
        data = db.session.query(Product).get(id)
        result = {"product_name": data.product_name, "product_price": data.product_price, "product_qty": data.product_qty}
        return jsonify(result)
    except:
        return jsonify({"message": "id tidak ditemukan!"})

#order_orm
@app.route("/order", methods=["GET", "POST"])
def api_order():
    if request.method == "GET":
        data = Order.query.all()
        result = []
        for d in data:
            res = {"user_id": d.user_id, "product_id": d.product_id}
            result.append(res)
            
        return jsonify(result)

    elif request.method == "POST":
        data = request.get_json()
        for d in data:
            order = Order(user_id=d.get("user_id"), product_id=d.get("product_id"))
            db.session.add(order)
        db.session.commit()

        return jsonify({"message": "data berhasil ditambahkan!"})

@app.route("/order/<id>", methods=["GET"])
def api_order_onlyone(id):
    try:
        data = db.session.query(Order).get(id)
        result = {"user_id": data.user_id, "product_id": data.product_id}
        return jsonify(result)
    except:
        return jsonify({"message": "id tidak ditemukan!"})

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)