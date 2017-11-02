# !/usr/bin/env python3.6
# Database code for DB news Log Analysis

import psycopg2

DBNAME = "news"


def question_one():
    """ Method Will return question #1 answer from database """
    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    cur.execute("""select articles.slug as article,
                        count(*) as views from articles,
                        log where log.path
                        like(concat('%',articles.slug,'%'))
                        group by article order by views desc limit 3""")
    answer_one = cur.fetchall()
    return answer_one
    conn.close()
    cur.close()


def question_two():
    """ Method Will return question #2 answer from database """
    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    cur.execute("""select name, sum(views) as views from article_views
                        group by name order by views desc""")
    answer_two = cur.fetchall()
    return answer_two
    conn.close()
    cur.close()


def question_three():
    """ Method Will return question #3 answer from database """
    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    cur.execute("""select * from (select day,
                        round((round(errors,2)*100)/round(total,2),2)
                        as percentage from requests) as bad_day where
                        percentage>1""")
    answer_three = cur.fetchall()
    return answer_three
    conn.close()
    cur.close()
