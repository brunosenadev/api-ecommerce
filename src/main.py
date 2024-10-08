from flask import Flask, request
from flask_cors import CORS
from flask_login import LoginManager, login_required, current_user
from database import config_database_uri
from utils import json_format
from login import login, logout
from product import add_product, delete_product, get_product_details, update_product, get_all_products
from user import returns_current_user, add_user
from cart import add_to_cart, delete_from_cart, view_cart_items, checkout

app = Flask(__name__)
login_manager = LoginManager()
app.config['SECRET_KEY'] = "my_key_python"
login_manager.init_app(app)
login_manager.login_view = 'login'
config_database_uri(app)
CORS(app)

@login_manager.user_loader
def load_user(user_id):
    return returns_current_user(int(user_id))

@app.route('/login', methods=['POST'])
def route_login():
    data = request.json
    response = login(data.get('username'), data.get('password'))
    return response

@app.route('/logout', methods=['POST'])
@login_required
def route_logout():
    response = logout()
    return response

@app.route('/api/products/add', methods=['POST'])
@login_required
def route_add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        response = add_product(data['name'], data['price'], data.get('description', ''))
        return response
    return json_format('Invalid product data', 400)

@app.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
@login_required
def route_delete_product(product_id):
    response = delete_product(product_id)
    return response

@app.route('/api/products/<int:product_id>', methods=['GET'])
def route_get_product_details(product_id):
    response = get_product_details(product_id)
    return response

@app.route('/api/products/update/<int:product_id>', methods=['PUT'])
@login_required
def route_update_product(product_id):
    data = request.json
    name = data.get('name', '')
    price = data.get('price', '')
    description = data.get('description', '')
    response = update_product(product_id, name, price, description)
    return response

@app.route('/api/products', methods=['GET'])
def route_get_all_products():
    response = get_all_products()
    return response

@app.route('/api/users/add', methods=['POST'])
def route_add_user():
    data = request.json
    response = add_user(data.get('username', ''), data.get('password', ''))
    return response

@app.route('/api/cart/add/<int:product_id>', methods=['POST'])
@login_required
def route_add_to_cart(product_id):
    response = add_to_cart(product_id, current_user.id)
    return response
        
@app.route('/api/cart/remove/<int:product_id>', methods=["POST"])
@login_required
def route_remove_from_cart(product_id):
    response = delete_from_cart(product_id, current_user.id)
    return response

@app.route('/api/cart', methods=['GET'])
@login_required
def route_view_cart():
    response = view_cart_items(int(current_user.id))
    return response

@app.route('/api/cart/checkout', methods=["POST"])
@login_required
def route_checkout():
    response = checkout(int(current_user.id))
    return response

if __name__ == '__main__':
    app.run(debug=True, port=3333)