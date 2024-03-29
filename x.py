from bottle import request
import sqlite3
import pathlib 

##############################
def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}

##############################
def db():
    try:
        db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db") 
        db.row_factory = dict_factory
        return db
    except Exception as ex:
        print(ex)
    finally:
        pass


TWEET_MIN_LEN = 1
TWEET_MAX_LEN = 200

def validate_tweet():
    error = f"Message must contain a minimum of {TWEET_MIN_LEN} and a maximum of {TWEET_MAX_LEN} characters."
    if len(request.forms.message) < TWEET_MIN_LEN: raise Exception(error)
    if len(request.forms.message) > TWEET_MAX_LEN: raise Exception(error)
    return request.forms.get("message")