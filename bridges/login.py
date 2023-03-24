from bottle import post, response
import time

@post("/login")
def _():
    # Redirection
    # The redirected page

    # Status code
    # response.status = 300

    #This is a get
    # response.set_header("Location", "/login")

    logged_in_user = {
        "logged_in_user_name": "MajaSorensen",
        "logged_in_user_first_name": "Maja",
        "logged_in_user_last_name": "Sorensen"
    }
    # Expires in 2 hours, 1 hour is 3600
    cookie_expiration_date = int(time.time()) + 7200
    response.set_cookie("logged_in_user", logged_in_user, secret="my-secret", httponly=True)
    response.status = 303
    response.set_header("Location", "/logged_in_user")
    return 