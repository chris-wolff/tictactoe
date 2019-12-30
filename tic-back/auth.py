import re

import flask
import flask_login
import sqlalchemy

import db
import model

# TODO: Figure out the easiest way to insert these into the register template
USERNAME_REGEX = "\w+"
PASSWORD_REGEX = "\w+"

USERNAME_FEEDBACK = "username must be a letter, number, and/or underscore"
PASSWORD_FEEDBACK = "password must be a letter, number, and/or underscore"


def current_user():
    """Return the currently authenticated user"""
    return flask_login.current_user.get_id()


def create_user(username, password):
    """Attempts to create a new user and commit to database
    Args:
        username (str): The username for the new user
        password (str): The password for the new user
    Returns:
        True if the user was successfully created, False otherwise.
    """
    user = load_user(username)
 
    if user is None:
        new_user = model.User(username=username, password=password)
        db.Session.add(new_user)
        db.Session.commit()
        return True
    else:
        return False


def authenticate_user(username, password):
    """Checks if the given credentials are correct
    Args:
        username (str): username to check
        password (str): password to check
    Returns:
        True if the given credentials refer to a valid user, False otherwise
    """
    user = load_user(username)

    if user is not None:

        if user.password == password:
            flask_login.login_user(user)
            return True

    return False


def load_user(username):
    """Loads the user object with the given username
    Args:
        username: The username of the user to load
    Returns:
        The user with the given username or None if the user doesn't exist.
    """
    return db.Session.query(model.User).filter_by(username=username).scalar()


def string_match(string, regex):
    """Checks that a given string conforms to our regex constraints.
    Args:
        username (str): The username to be vetted
    Returns:
        True if the username is valid, False otherwise.
    """
    return re.fullmatch(regex, string) is not None
