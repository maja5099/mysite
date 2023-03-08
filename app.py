# 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
# https://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@github.com/maja5099/mysite.git


###################################
from bottle import default_app, get, post, static_file, run, template, response, request
import git
import sqlite3
import pathlib
import uuid
import datetime


###################################
print("#"*30)
print("directory of the script being run")
print(pathlib.Path(__file__).parent.resolve()) # /home/USERNAME/mysite


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
# ROUTE, SHOW HTML AND TITLE
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
        return {"error": str(ex)}

    finally:
        if "db" in locals(): db.close()


###################################
@get("/<username>")
# @view("profile")
def _(username):
    try:
        db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
        db.row_factory = dict_factory
        user = db.execute("SELECT * FROM users WHERE username=? COLLATE NOCASE",(username,)).fetchall()[0]
        # Get the user's id
        user_id = user["id"]
        print("#"*30)
        print(f"user id:{user_id}")
        # With that id, look up/get the respectives tweets
        tweets = db.execute("SELECT * FROM tweets WHERE user_fk=?", (user_id,)).fetchall()
        print("#"*30)
        print(tweets)
        print("#"*30)
        # pass the tweets to the view. Template it
        print(user) # {'id': '51602a9f7d82472b90ed1091248f6cb1', 'username': 'elonmusk', 'name': 'Elon', 'last_name': 'Musk', 'total_followers': '128900000', 'total_following': '177', 'total_tweets': '22700', 'avatar': '51602a9f7d82472b90ed1091248f6cb1.jpg'}
        return template("profile", user=user)

    except Exception as ex:
        print(ex)
        return "error"
        
    finally:
        if "db" in locals(): db.close()


###################################
# RUN ON PYTHONANYWHERE ELSE LOCAL HOST
try:
    import production
    application = default_app()
except Exception as ex:
    print("Running local server")
    run(host="127.0.0.1", port=3000, debug=True, reloader=True)


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