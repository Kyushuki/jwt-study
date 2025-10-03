from flask import Flask, render_template, request, jsonify
import jwt_task
import jwt

LOGIN = "admin"
PASS = "pass"


app = Flask(__name__, template_folder="templates")


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
    data = request.get_json()
    user_name = data.get("username")
    user_password = data.get("password")

    if user_name == LOGIN and user_password == PASS:
        token = jwt_task.jwt_encode(user_name)

        return jsonify({"status": "ok", "token": token})

    return jsonify({"status": "error", "msg": "Неверный логин или пароль"})


@app.route("/meme", methods=["GET"])
def protected_page():
    # Страничка доступ к которой имеется только если токен валиден и не истёк
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"error": "Token missing"}), 401
    try:
        token = auth_header.split(" ")[1]
        jwt_task.jwt_decode(token)
        html = render_template("meme.html")
        return jsonify({"status": "ok", "html": html}), 200

    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401


app.run(port=8080, debug=True)
