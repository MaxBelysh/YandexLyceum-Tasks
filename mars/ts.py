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


@app.route("/promotion_image")
def promotion_image():
    return f'''<!doctype html>
                       <html lang="en">
                         <head>
                           <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href='/static/css/style.css'>
                           <title>Колонизация</title>
                         </head>
                         <body>
                           <h1>Жди нас Марс!</h1>
                           <img src="/static/img/mars.png" alt="здесь должна быть картинка">
                           <div class="cont grey">Человечество вырастает из детства.</div>
                           <div class="cont green">Человечеству мала одна планета.</div>
                           <div class="cont grey">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                           <div class="cont yellow">И начнем с Марса!</div>
                           <div class="cont red">Присоединяйся!</div>
                         </body>
                       </html>'''


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")