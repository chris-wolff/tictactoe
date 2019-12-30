import flask
import flask_login
import jinja2

import auth

auth_bp = flask.Blueprint("auth", __name__)

@auth_bp.route("/user", methods=["GET"])
def user():
    print(str(auth.current_user()))
    return str(auth.current_user())

@auth_bp.route("/login", methods=["GET"])
def login():
    return flask.render_template("login.html", invalidLogin=False)


@auth_bp.route("/login", methods=["POST"])
def login_post():
    username = flask.request.form["username"]
    password = flask.request.form["password"]

    # Link to the TTT React application
    if auth.authenticate_user(username, password):
       return flask.redirect("http://localhost:3000")
    else:
        flask.flash("Whoops, we don't recognize that account! Please try again.")
        return flask.render_template("login.html")

@auth_bp.route("/logout")
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for("auth.login"))


@auth_bp.route("/register", methods=["GET"])
def register():
    return flask.render_template("register.html")


@auth_bp.route("/register", methods=["POST"])
def register_post():
    username = flask.request.form["username"]
    password = flask.request.form["password"]
    confirm = flask.request.form["confirm"]

    if confirm != password:
        flask.flash("Passwords entered do not match! Please try again.")
        return flask.render_template("register.html")

    if not auth.string_match(username, auth.USERNAME_REGEX):
        flask.flash(auth.USERNAME_FEEDBACK)
        return flask.render_template("register.html")

    if not auth.string_match(password, auth.PASSWORD_REGEX):
        flask.flash(auth.PASSWORD_FEEDBACK)
        return flask.render_template("register.html")

    created = auth.create_user(username, password)

    if created:
        return flask.redirect(flask.url_for("auth.login"))
    else:
        flask.flash("Username already exists!")
        return flask.render_template("register.html")

