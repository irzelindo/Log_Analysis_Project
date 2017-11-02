# !/usr/bin/env python3.6
import dbnews

from flask import Flask

app = Flask(__name__)
# Creating html layout to display info from DB
HTML = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Log Analysis</title>
    <link rel="stylesheet"
        href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
        integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
        crossorigin="anonymous">
        <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body class="container">
    <h2>Log Analysis</h2>
    <ul>
        <h4>Most popular three articles of all time</h4>
        <li>{a[0][0]} = {a[0][1]} views </li>
        <li>{a[1][0]} = {a[1][1]} views </li>
        <li>{a[2][0]} = {a[2][1]} views </li>
    </ul>
    <ul>
        <h4>Most popular article author of all time</h4>
        <li>{aut[0][0]} = {aut[0][1]} views </li>
        <li>{aut[1][0]} = {aut[1][1]} views </li>
        <li>{aut[2][0]} = {aut[2][1]} views </li>
        <li>{aut[3][0]} = {aut[3][1]} views </li>
    </ul>
    <ul>
        <h4>Days witch more than 1% of requests lead to errors</h4>
        <li>{e[0][0]} = {e[0][1]}%</li>
    </ul>
  </body>
</html>
'''


@app.route('/', methods=['GET'])
def main():
    # Fetching data from database & formating into html layout
    articles = dbnews.question_one()
    authors = dbnews.question_two()
    errors = dbnews.question_three()
    html = HTML.format(a=articles, aut=authors, e=errors)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
