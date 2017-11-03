# !/usr/bin/env python3.6
# Database code for DB news Log Analysis

import psycopg2


def connect(DBNAME="news"):
    try:
        db = psycopg2.connect("dbname={}".format(DBNAME))
        cursor = db.cursor()
        return db, cursor
    except:
        print("error trying to connect to DB")


def close_connection(db,cursor):
    cursor.close()
    db.close()


def question_one():
    """ Method Will return question #1 answer from database """
    db, cursor = connect()
    cursor.execute("""select articles.title as article,
                    count(*) as views from log,
                    articles where log.path = concat('/article/',articles.slug)
                    group by article order by views desc limit 3""")
    answer_one = cursor.fetchall()
    close_connection(db,cursor)
    return answer_one


def question_two():
    """ Method Will return question #2 answer from database """
    db, cursor = connect()
    cursor.execute("""select name, sum(views) as views from (select authors.name,
                    articles.title, count(*) as views from log, articles,
                    authors where log.path = concat('/article/',
                    articles.slug) AND authors.id = articles.author
                    group by authors.name, articles.title order by views desc)
                    as article_views group by name order by views desc""")
    answer_two = cursor.fetchall()
    close_connection(db,cursor)
    return answer_two


def question_three():
    """ Method Will return question #3 answer from database """
    db, cursor = connect()
    cursor.execute("""select * from (select day,
                    round((round(errors,2)*100)/round(total,2),2)
                    as percentage from requests) as bad_day where
                    percentage>1""")
    answer_three = cursor.fetchall()
    close_connection(db,cursor)
    return answer_three
