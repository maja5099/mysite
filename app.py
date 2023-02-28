# 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
# https://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@github.com/maja5099/mysite.git

#########################
from bottle import default_app, get, post, static_file, run, template
import git

@post('/secret_url_for_git_hook')
def git_update():
    repo = git.Repo('./mysite')
    origin = repo.remotes.origin
    repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return ""


##############################
# @get("/")
# def _():
#     return "Three"

################################### 
# Import and show webp images via the folder
@get("/images/<filename:re:.*\.webp>")
def _(filename):
    return static_file(filename, root="./images")

################################### 
# Import and show png images via the folder
@get("/images/<filename:re:.*\.png>")
def _(filename):
    return static_file(filename, root="./images")

################################### 
# Import and show jpg images via the folder
@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images")

################################### 
# Import and show CSS
@get("/app.css")
def _():
    return static_file("app.css", root=".")

##############################
try:
    import production
    application = default_app()
except Exception as ex:
    print("Running local server")
    run(host="127.0.0.1", port=80, debug=True, reloader=True)


################################### 
# Route, shows html (index) and variable title
@get("/")
def render_index():
    return template("index", title="Twitter")


