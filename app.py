# 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
# https://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@github.com/maja5099/mysite.git


###################################
from bottle import default_app, get, post, static_file, run, template, response, request
import os
# import git
import sqlite3
import pathlib
import uuid
import datetime


###################################
print("#"*30)
print("directory of the script being run")
print(pathlib.Path(__file__).parent.resolve()) # /home/USERNAME/mysite


###################################
@get("/js/<filename>")
def _(filename):
    return static_file(filename, "js")


###################################
def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}


###################################
# CONNECT TO GITHUB AND PYTHONANYWHERE
@post('/secret_url_for_git_hook')
def git_update():
    repo = git.Repo('./mysite')
    origin = repo.remotes.origin
    repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return ""


###################################
# IMPORT AND SHOW WEBP, PNG & JPG IMAGES
@get("/images/<filename:re:.*\.webp>")
def _(filename):
    return static_file(filename, root="./images")

@get("/images/<filename:re:.*\.png>")
def _(filename):
    return static_file(filename, root="./images")

@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images")


###################################
# IMPORT AND SHOW CSS
@get("/app.css")
def _():
    return static_file("app.css", root=".")


###################################
# VIEW AND SHOW LOGIN HTML
@get("/login")
def _():
    return template("login")


# VIEW AND SHOW LOGGED IN USER HTML
@get("/logged_in_user")
def _():
    # Disable cache
    response.add_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)

    # Cookie
    logged_in_user = request.get_cookie("logged_in_user", secret="my-secret")


    # Username
    return template("logged_in_user", logged_in_user=logged_in_user)


# VIEW AND SHOW LOGOUT HTML
@get("/logout")
def _():
    response.set_cookie("logged_in_user", "", expires=0)
    response.status = 303
    response.set_header("Location", "/login")
    return


###################################
# ROUTE, SHOW HTML AND TITLE (INDEX)
@get("/")
def render_index():
    try:
        db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
        db.row_factory = dict_factory
        tweets = db.execute("SELECT * FROM tweets")
        trends = db.execute("SELECT * FROM trends")
        users = db.execute("SELECT * FROM users")
        users_and_tweets = db.execute("SELECT * FROM users_and_tweets")

        return template("index", title="Twitter", tweets=tweets, trends=trends, users=users, users_and_tweets=users_and_tweets)

    except Exception as ex:
        print(ex)
        response.status = 400
        return {"error index": str(ex)}

    finally:
        if "db" in locals(): db.close()





###################################
@get("/<username>")
# @view("profile")
def _(username):
    try:
        db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
        # db = sqlite3.connect(os.getcwd()+"/twitter.db")
        db.row_factory = dict_factory
        # user = db.execute("SELECT * FROM users WHERE user_name=? COLLATE NOCASE",(username,)).fetchall()[0]
        user = db.execute("SELECT * FROM users WHERE user_name=? COLLATE NOCASE",(username,)).fetchone()
        # Get the user's id
        user_id = user["user_id"]
        trends = db.execute("SELECT * FROM trends")
        users = db.execute("SELECT * FROM users")
        users_and_tweets = db.execute("SELECT * FROM users_and_tweets")
        print("#"*30)
        print(f"user id:{user_id}")
        
        # With that id, look up/get the respectives tweets
        tweets = db.execute("SELECT * FROM tweets WHERE tweet_user_fk=?", (user_id,)).fetchall()
        print("#"*30)
        print(tweets)
        print("#"*30)
        
        # pass the tweets to the view. Template it
        print(user) # {'id': '51602a9f7d82472b90ed1091248f6cb1', 'username': 'elonmusk', 'name': 'Elon', 'last_name': 'Musk', 'total_followers': '128900000', 'total_following': '177', 'total_tweets': '22700', 'avatar': '51602a9f7d82472b90ed1091248f6cb1.jpg'}
        return template("profile", title="Twitter", user=user, tweets=tweets, trends=trends, users=users, users_and_tweets=users_and_tweets)

    except Exception as ex:
        print(ex)
        return str(ex)
        
    finally:
        if "db" in locals(): db.close()


###################################
# VIEWS
import views.tweet


###################################
# IMPORT LOGIN.PY
import bridges.login


###################################
# APIS
import apis.api_tweet


###################################
# RUN ON PYTHONANYWHERE ELSE LOCAL HOST
try:
    import production
    application = default_app()
except Exception as ex:
    print("Running local server")
    run(host="127.0.0.1", port=5000, debug=True, reloader=True)


###################################
# API ROUTE
@get("/api-get-name")
def _():
    try: # Best case scenario
        id = request.query.get("id")
        name = request.query.get("name")
        surname = request.query.get("surname")

        if id !="1": raise Exception("the id is wrong")
        if name !="a": raise Exception("the name is wrong")
        if surname !="b": raise Exception("the surname is wrong")

        # Connect/open to the database
        db = sqlite3.connect("twitter.db")
        users = db.execute("SELECT * FROM users").fetchall()
        print(users) #this is for the terminal
        # Get the name from the database

        # Send the name to the client
        return {"id":id, "name": name, "surname":surname}

    except Exception as ex: # Something went wrong
        print(ex)
        # Send a 400 to the client
        response.status = 400
        return {"error": str(ex)}

    finally: # It must be done
        # Close the database
        if "db" in locals(): db.close()
        print("I am here")