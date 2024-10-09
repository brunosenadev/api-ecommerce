from utils import json_format
from flask import jsonify

class CartClass:
    def __init__(self, db_class):
        self.commit_db = db_class.commit_database
        self.user_db = db_class.User
        self.product_db = db_class.Product
        self.cart_item_db = db_class.Cart
        
    def add_to_cart(self, product_id, current_user_id):
        user_cart = self.user_db.query.get(current_user_id)
        product_to_cart = self.product_db.query.get(product_id)
        if user_cart and product_to_cart:
            cart_item = self.cart_item_db(user_id=user_cart.id, product_id=product_to_cart.id)
            self.commit_db(cart_item)
            return json_format('Item added to the cart successfully')
        return json_format('Failed to add item to the cart', 400)

    def delete_from_cart(self, product_id, current_user_id):
        cart_user_items = self.cart_item_db.query.filter_by(user_id=current_user_id, product_id=product_id).first()
        if cart_user_items:
            self.commit_db(cart_user_items, 'delete')
            return json_format('Item removed from the cart successfully')
        return json_format('Failed to remove item from the cart', 400)

    def view_cart_items(self, current_user_id):
        user_view_cart = self.user_db.query.get(current_user_id)
        cart_items = user_view_cart.cart
        cart_content = []
        for item in cart_items:
            product_get = self.product_db.query.ger(item.product_id)
            cart_content.append({
                "id": item.id,
                "product_id": item.product_id,
                "product_name": product_get.name,
                "product_price": product_get.price
            })
        return jsonify(cart_content)

    def checkout(self, current_user_id):
        user_checkout = self.user_db.query.get(current_user_id)
        cart_items = user_checkout.cart
        for item in cart_items:
            self.commit_db(item, 'delete')
        return json_format('Checkout successful. Cart has been cleared')