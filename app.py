from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models và routes sau khi tạo db
from models import create_models
from routes import register_routes

# Tạo models
Task = create_models(db)

# Đăng ký routes
register_routes(app, db, Task)



if __name__ == '__main__':
    app.run(debug=True)