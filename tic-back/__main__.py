from flask import Flask

app = Flask(__name__, template_folder="../templates/")

def main():
    """
        Configure everything and kick off the flask server.
    """
    
    configure_flask_login()
    register_blueprints()
    configure_database()

    # This should only be a problem when testing because trying to send requests between two different ports on localhost.
    from flask_cors import CORS
    CORS(app) 

    # Starts the flask server in debug mode.
    app.run(debug=True) 
   

def configure_flask_login():
    """
        Configuration helper.
    """
     # Make a secret key for flask_login sessions 
    import os
    gen_secret_key = os.urandom(16)
    app.secret_key = gen_secret_key

     # Configure flask_login LoginManager
    import flask_login
    login_manager = flask_login.LoginManager(app)
    login_manager.login_view = "auth.login"

    import auth
    login_manager.user_loader(auth.load_user)

def register_blueprints():
    """
        Configuration helper.
    """
    from game_view import game_bp
    from auth_view import auth_bp

    app.register_blueprint(game_bp)
    app.register_blueprint(auth_bp)

def configure_database():
    """
        Configuration helper.
    """
    # Set up and create a session with the database.
    import db 
    import sqlalchemy
    
    engine = sqlalchemy.create_engine("sqlite:///../db.sqlite" )
    db.SessionFactory.configure(bind=engine)

    # Configure Data Models
    import model
    model.Model.metadata.create_all(engine)


if __name__ == "__main__":
    main()

    