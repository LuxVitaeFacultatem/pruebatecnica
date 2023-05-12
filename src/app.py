from flask import Flask
from config import config


# Routes
from routes import Driver

app = Flask(__name__)


def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # blueprints
    app.register_blueprint(Driver.main, url_prefix='/api')

    # error handlers
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)
