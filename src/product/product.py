from database import Product, commit_database
from utils import json_format
from flask import jsonify

def add_product(name, price, description):
        product_added = Product(name=name, price=price, description=description)
        commit_database(product_added)
        return json_format('Product added successfully')

def delete_product(product_id):
    product_deleted = Product.query.get(product_id)
    if product_deleted:
        commit_database(product_deleted, 'delete')
        return json_format('Product deleted successfully')
    return json_format('Product not found', 404)

def get_product_details(product_id):
    product_details = Product.query.get(product_id)
    if product_details:
        return jsonify({
            "id": product_details.id,
            "name": product_details.name,
            "description": product_details.description,
            "price": product_details.price
        })
    return json_format('Product not found', 404) 

def update_product(product_id, name, price, description):
    product_updated = Product.query.get(product_id)
    if not product_updated:
        return json_format('Product not found', 404)
    if name != '':
        product_updated.name = name
    if price != '':
        product_updated.price = price
    if description != '':
        product_updated.description = description
    commit_database(product_updated)
    return json_format('Product updated successfully')

def get_all_products():
    products = Product.query.all()
    products_list = []
    for product in products:
        product_data = {
            "id": product.id,
            "name": product.name,
            "price": product.price
        } 
        products_list.append(product_data)
    return jsonify(products_list)