from flask import Flask, render_template, request, jsonify


app = Flask(__name__, template_folder="templates")


SECRET_KEY = ""
ALGORITHM = "HS256"

# TODO: В качестве username укажите фамилию
uLogin = "a"
password = "a"


def encoding(username):
    """
    Функция для создания токена

    Её вам и нужно реализовать

    Возвращать она должна токен
    """

    # TODO: сделать начинку, сгенерировать и вернуть токен
    return


@app.route("/meme", methods=["GET"])
def protected_page():
    # Страничка доступ к которой имеется только если токен валиден и не истёк
    # Клиент (фронтенд) хранит ваш отправленный токен, поэтому с помощью request получите ответ от фронтенда (пример есть в login() ниже)

    # TODO: Реализуйте доступ к страничке с помощью токена (т.е. декодируйте его и примените остальную магию)
    # TODO 2: Пусть доступ закрывается по истичению срока жизни токена
    # TODO 3: Пусть доступ закрывается если нет прав( нужной роли )
    # В качестве ответа клиенту посылать jsonify({"status": "Нужный статус", "msg": "соответствующее сообщение"})

    html = render_template("meme.html")
    return jsonify({"status": "ok", "html": html}), 200

# Всё что ниже, не трогать, желательно


@app.route("/")
def vhod():
    # страничка с формой входа
    return render_template('index.html')


@app.route("/home")
def standart():
    # страничка после входа
    return render_template('home.html')


@app.route("/login", methods=['POST'])
def login():
    # Вход
    # Здесь ничего не менять
    # Ну если сильно хочется то можете конечно, но как сами знаете
    data = request.get_json()
    user_name = data.get("username")
    user_password = data.get("password")
    global login, password
    if user_name == uLogin and user_password == password:
        token = encoding(user_name)

        return jsonify({"status": "ok", "token": token})

    return jsonify({"status": "error", "msg": "Неверный логин или пароль"})


app.run(port=8080, debug=True)
