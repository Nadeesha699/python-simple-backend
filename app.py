from flask import Flask, jsonify
from db import db_connection

app = Flask(__name__)

con = db_connection()
cursor = con.cursor()

@app.route('/api/user')
def user():
  cursor.execute('SELECT * FROM user WHERE ID = 1')
  user =  cursor.fetchone()
  return jsonify({"data":user,"success":True,})


if __name__ == '__main__':
    app.run(debug=True)    