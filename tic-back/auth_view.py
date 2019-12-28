import flask
import jinja2

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET"])
def login():
    return flask.render_template("login.html", invalidLogin=False)


@auth_bp.route("/login", methods=["POST"])
def login_post():
    username = flask.request.form["username"]
    password = flask.request.form["password"]

    authorized = predict.auth.authenticate_user(username, password)

    if authorized:
        return flask.redirect(
            flask.request.args.get("next", flask.url_for("main.dashboard"))
        )
    else:
        flask.flash("Unrecognized credentials! Please try again.")
        return flask.render_template("login.html")


@auth_bp.route("/logout")
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for("main.base"))


@auth_bp.route("/register", methods=["GET"])
def register():
    return flask.render_template(
        "register.html",
        user_regex=flask.current_app.config["USERNAME_REGEX"],
        password_regex=flask.current_app.config["PASSWORD_REGEX"],
    )


@auth_bp.route("/register", methods=["POST"])
def register_post():
    username = flask.request.form["username"]
    password = flask.request.form["password"]
    confirm = flask.request.form["confirm"]

    if confirm != password:
        flask.flash("Passwords entered do not match! Please try again.")
        return flask.render_template("register.html")

    if not predict.auth.string_match(
        username, flask.current_app.config["USERNAME_REGEX"]
    ):
        flask.flash(flask.current_app.config["USERNAME_FEEDBACK"])
        return flask.render_template("register.html")

    if not predict.auth.string_match(
        password, flask.current_app.config["PASSWORD_REGEX"]
    ):
        flask.flash(flask.current_app.config["PASSWORD_FEEDBACK"])
        return flask.render_template("register.html")

    whitelist = flask.current_app.config.get("WHITELIST")
    if whitelist is not None and username not in whitelist:
        flask.flash(
            "Username not in the whitelist. Please register using your "
            + "whitelisted username."
        )
        return flask.render_template("register.html")

    created = predict.auth.create_user(username, password)

    if created:
        return flask.redirect(flask.url_for("main.login"))
    else:
        flask.flash("That username already exists! Please try again.")
        return flask.render_template("register.html")

