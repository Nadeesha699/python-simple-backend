from flask import Flask
from routes.user import user_route
from routes.product import product_route
app = Flask(__name__)

app.register_blueprint(user_route,url_prefix="/api/user")
app.register_blueprint(product_route,url_prefix="/api/product")


if __name__ == '__main__':
    app.run(debug=True)    