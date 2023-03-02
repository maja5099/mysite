DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets(
    tweet_id        TEXT,
    tweet_message   TEXT,
    PRIMARY KEY(tweet_id)
)WITHOUT ROWID;

INSERT INTO tweets VALUES("1", "Hej");