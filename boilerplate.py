import os

from flask import Flask, make_response

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY", "secret_l801#+#a&^1mz)_p&qyq51j51@20_74c-xi%&i)b*u_dt^2=2key"
)

@app.route("/")
def boilerplate_script():
    script = "git clone --quiet https://github.com/CheesecakeLabs/django-drf-boilerplate.git && echo 'Thanks for cloning our repository! Have a very cheesy day!'"
    response = make_response(script, 200)
    response.mimetype = "text/plain"
    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
