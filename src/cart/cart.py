from database import User, Product, CartItem, commit_database
from utils import json_format
from flask import jsonify

def add_to_cart(product_id, current_user_id):
    user_cart = User.query.get(current_user_id)
    product_to_cart = Product.query.get(product_id)
    if user_cart and product_to_cart:
        cart_item = CartItem(user_id=user_cart.id, product_id=product_to_cart.id)
        commit_database(cart_item)
        return json_format('Item added to the cart successfully')
    return json_format('Failed to add item to the cart', 400)

def delete_from_cart(product_id, current_user_id):
    cart_user_items = CartItem.query.filter_by(user_id=current_user_id, product_id=product_id).first()
    if cart_user_items:
        commit_database(cart_user_items, 'delete')
        return json_format('Item removed from the cart successfully')
    return json_format('Failed to remove item from the cart', 400)

def view_cart_items(current_user_id):
    user_view_cart = User.query.get(current_user_id)
    cart_items = user_view_cart.cart
    cart_content = []
    for item in cart_items:
        product_get = Product.query.ger(item.product_id)
        cart_content.append({
            "id": item.id,
            "product_id": item.product_id,
            "product_name": product_get.name,
            "product_price": product_get.price
        })
    return jsonify(cart_content)

def checkout(current_user_id):
    user_checkout = User.query.get(current_user_id)
    cart_items = user_checkout.cart
    for item in cart_items:
        commit_database(item, 'delete')
    return json_format('Checkout successful. Cart has been cleared')