from flask import Flask

app = Flask(__name__)


@app.route('/')
def mars():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    return "</br>".join(["Человечество вырастает из детства.", "Человечеству мала одна планета.",
                         "Мы сделаем обитаемыми безжизненные пока планеты.",
                         "И начнем с Марса!", "Присоединяйся!"])


@app.route("/image_mars")
def img_mars():
    return f'''<!doctype html>
                   <html lang="en">
                     <head>
                       <meta charset="utf-8">
                       <title>Привет, Марс!</title>
                     </head>
                     <body>
                       <h1>Жди нас Марс!</h1>
                       <img src="/static/img/mars.png" alt="здесь должна быть картинка">
                       <div>Вот она какая красная планета.</div>
                     </body>
                   </html>'''


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")