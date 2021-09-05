from flask import redirect, session
from functools import wraps


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session.get("username") is None:  # TODO TEMPORARY
            return redirect("/login")
        
        # TODO remove later
        session["UUID"] = 0

        return func(*args, **kwargs)
    return decorated_function
