-- ##############################
-- USERS
DROP TABLE IF EXISTS users;
CREATE TABLE users(
    user_id                     TEXT UNIQUE NOT NULL,
    user_name                   TEXT UNIQUE NOT NULL,
    user_first_name             TEXT NOT NULL,
    user_last_name              TEXT DEFAULT "",
    user_verified               TEXT NOT NULL,
    user_avatar                 TEXT UNIQUE,
    user_cover                  TEXT UNIQUE,
    user_created_at             TEXT NOT NULL,
    user_total_tweets           TEXT DEFAULT 0,
    user_total_following        TEXT DEFAULT 0,
    user_total_followers        TEXT DEFAULT 0,
    PRIMARY KEY(user_id)
) WITHOUT ROWID;

-- Lady Gaga
-- INSERT INTO users VALUES("user_id", "user_name", "user_first_name", "user_last_name", "user_verified", "user_avatar.jpg", "user_cover.jpg", "user_created_at", "user_total_tweets", "user_total_following", "user_total_followers");
INSERT INTO users VALUES("a9890d6a78a344ec87401cdb85e38a14", "ladygaga", "Lady", "Gaga", "true", "046d38ab9a094b8fb4993d9e2f2131b6.jpg", "b7add1c2b384480bacfdc615c8a3e5aa.jpg", "1204326000", "9936", "116300", "84800000");

CREATE INDEX idx_users_user_first_name ON users(user_first_name);
CREATE INDEX idx_users_user_last_name ON users(user_last_name);
CREATE INDEX idx_users_user_avatar ON users(user_avatar);
CREATE INDEX idx_users_user_cover ON users(user_cover);

SELECT name FROM sqlite_master WHERE type = 'index';
SELECT name FROM sqlite_master WHERE type = 'trigger';


-- ##############################
-- TWEETS
DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets(
    tweet_id                    TEXT,
    tweet_message               TEXT,
    tweet_image                 TEXT UNIQUE,
    tweet_created_at            TEXT,
    tweet_user_fk               TEXT,
    tweet_total_comments        TEXT,
    tweet_total_retweets        TEXT,
    tweet_total_likes           TEXT,
    tweet_total_views           TEXT,
    PRIMARY KEY(tweet_id)
)WITHOUT ROWID;

-- Lady Gaga
-- INSERT INTO tweets VALUES("tweet_id", "tweet_message", "tweet_image.jpg", "tweet_created_at", "tweet_user_fk", "tweet_total_comments", "tweet_total_retweets", "tweet_total_likes", "tweet_total_views");
INSERT INTO tweets VALUES("28106db01fdc496b8f8881e1d943a201", "V MAGAZINE: CHROMATICA BALL DIARIES BY HEDI SLIMANE COVER 2", "67ed34300fa640c38cfc5d01d4d8cca3.jpg", "1663099320", "a9890d6a78a344ec87401cdb85e38a14", "1,733", "9,034", "45,500", "");

CREATE INDEX idx_tweets_tweet_image ON tweets(tweet_image);


-- ##############################
-- TRENDS
DROP TABLE IF EXISTS trends;
CREATE TABLE trends(
    trend_id                    TEXT,
    trend_category              TEXT DEFAULT 0,
    trend_title                 TEXT NOT NULL,
    trend_total_tweets          TEXT DEFAULT 0,
    PRIMARY KEY(trend_id)
) WITHOUT ROWID;

-- Trend 1
INSERT INTO trends VALUES("123", "Trend category", "Trend title", "1234");


-- ##############################
-- JOIN TABLES USERS & TWEETS
SELECT * FROM users JOIN tweets ON user_id = tweet_user_fk;

DROP VIEW IF EXISTS users_and_tweets;
CREATE VIEW users_and_tweets AS 
SELECT * FROM users JOIN tweets ON user_id = tweet_user_fk;

SELECT * FROM users_and_tweets;