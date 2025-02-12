from flask import Blueprint, jsonify, request

from database.db import db_connection

con = db_connection()
cursor = con.cursor()
product_route = Blueprint('product_route',__name__)

@product_route.route('/get-all',methods=['GET'])
def get_all_product():
    try:
      cursor.execute('SELECT * FROM product')
      products = cursor.fetchall()
      return jsonify({"data":products,"success":True})
    except Exception as e:
      return jsonify({"message":e.message,"success":False}),500

@product_route.route('/add',methods=['POST'])
def add_product():
    try:
      data = request.json
      name = data.get('Name')
      price = data.get('Price')
      category = data.get('Category')
      cursor.execute('INSERT INTO product (Name,Price,Category) VALUES (%s,%s,%s)',(name,price,category))
      con.commit()
      return jsonify({"success":True,"message":"Product created successfully"})
    except Exception as e:
      return jsonify({"message":e.message,"success":False}),500

@product_route.route('/edit/by-id/<int:id>',methods=['PUT'])
def edit_product_by_id(id):
    try:
      data = request.json
      name = data.get('Name')
      price = data.get('Price')
      category = data.get('Category')
      cursor.execute('UPDATE product SET Name = %s , Price = %s, Category= %s WHERE ID = %s ',(name,price,category,id))
      con.commit()
      return jsonify({"success":True,"message":"Product updated successfully"})
    except Exception as e:
      return jsonify({"message":e.message,"success":False}),500

@product_route.route('/get-product/by-id/<int:id>',methods=['GET'])
def get_product_by_id(id):
    try:
      cursor.execute('SELECT * FROM product WHERE ID = %s',(id,))
      product = cursor.fetchone()
      return jsonify({"data":product,"success":True})
    except Exception as e:
      return jsonify({"message":e.message,"success":False}),500
 
@product_route.route('/delete-product/by-id/<int:id>',methods=['DELETE'])
def delete_product_by_id(id):
    try:
      cursor.execute('DELETE FROM product WHERE ID= %s',(id,))
      con.commit()
      return jsonify({"success":True,"message":"Product deleted successfully"})
    except Exception as e:
      return jsonify({"message":e.message,"success":False}),500


