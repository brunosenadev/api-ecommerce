from utils import json_format
from flask import jsonify

class ProductClass:
    def __init__(self, db_class):
        self.commit_db = db_class.commit_database
        self.product_db = db_class.Product
        
    def add_product(self, name, price, description):
        product_added = self.product_db(name=name, price=price, description=description)
        self.commit_db(product_added)
        return json_format('Product added successfully')

    def delete_product(self, product_id):
        product_deleted = self.product_db.query.get(product_id)
        if product_deleted:
            self.commit_db(product_deleted, 'delete')
            return json_format('Product deleted successfully')
        return json_format('Product not found', 404)

    def get_product_details(self, product_id):
        product_details = self.product_db.query.get(product_id)
        if product_details:
            return jsonify({
                "id": product_details.id,
                "name": product_details.name,
                "description": product_details.description,
                "price": product_details.price
            })
        return json_format('Product not found', 404) 

    def update_product(self, product_id, name, price, description):
        product_updated = self.product_db.query.get(product_id)
        if not product_updated:
            return json_format('Product not found', 404)
        if name != '':
            product_updated.name = name
        if price != '':
            product_updated.price = price
        if description != '':
            product_updated.description = description
        self.commit_db(product_updated)
        return json_format('Product updated successfully')

    def get_all_products(self):
        products = self.product_db.query.all()
        products_list = []
        for product in products:
            product_data = {
                "id": product.id,
                "name": product.name,
                "price": product.price
            } 
            products_list.append(product_data)
        return jsonify(products_list)