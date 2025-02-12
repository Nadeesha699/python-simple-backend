from flask import app, jsonify,Blueprint, request

from database.db import db_connection


con = db_connection()
cursor = con.cursor()
user_route = Blueprint('user_routes',__name__)

@user_route.route('/get-all',methods=['GET'])
def get_all_users():
  cursor.execute('SELECT * FROM user')
  user =  cursor.fetchall()
  return jsonify({"data":user,"success":True,})


@user_route.route('/get/by-id/<int:id>', methods=['GET'])
def get_user_by_id(id):
  cursor.execute('SELECT * FROM user WHERE ID = %s',(id,))
  users = cursor.fetchone()
  return jsonify({"data":users,"success":True})

@user_route.route('/create',methods=['POST'])
def set_user():
  data = request.json
  name = data.get("Name")
  age = data.get("Age")
  cursor.execute('INSERT INTO user (Name,Age)VALUES(%s,%s)',(name,age))
  con.commit()
  return jsonify({"success":True})

@user_route.route('/edit/by-id/<int:id>',methods=['PUT'])
def update_user_by_id(id):
  data = request.json
  name = data.get('Name')
  age = data.get('Age')
  cursor.execute('UPDATE user SET Name = %s, Age =%s WHERE ID = %s',(name,age,id,))
  con.commit()
  return jsonify({"success":True})


@user_route.route('/delete/by-id/<int:id>',methods=['DELETE'])
def delete_by_id(id):
  cursor.execute('DELETE FROM user WHERE ID = %s',(id,))
  con.commit()
  return jsonify({"success":True})