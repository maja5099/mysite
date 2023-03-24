from bottle import get, template
import x

@get("/profile")
def _():
    return template ("profile")