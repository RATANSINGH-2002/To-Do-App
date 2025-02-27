from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager # Manages login related things 

db = SQLAlchemy()
DB_Name = "Notes"

def create_App():
    app = Flask(__name__)
    app.config['SECRET_KEY']= "Learning"
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_Name}' # in DB_Name mention.db at end i.e. Notes.db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flaskadmin:Flask%40123@localhost:5432/Notes'
    # app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False # Auto commit is OFF 
    # app.config['SQLALCHEMY_ECHO'] = True  # Shows SQL queries in the console

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Attendee,Note
    create_database(app)

    Login_manager = LoginManager()
    Login_manager.login_view = 'auth.login' # If user is not login manager redirects to the auth.login page
    Login_manager.init_app(app)
  
    @Login_manager.user_loader
    def load_user(id):
       return Attendee.query.get(int(id)) # looks for primary key similar to filter by in database
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_Name):
        with app.app_context():
         db.create_all()

        print('Created Database!')