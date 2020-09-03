from flask import Flask


def create_app():
    _app = Flask(__name__)
    from .account import account
    _app.register_blueprint(account, url_prefix='/api')

    return _app


app = create_app()

if __name__ == "__main__":
    print(type(app))
    print(app, type(app))