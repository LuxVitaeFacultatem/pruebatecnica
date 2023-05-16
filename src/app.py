from flask import Flask, request
from config import config


# Routes
from routes import Driver
from routes import Rider

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    url = request.url
    return f"<h1>404</h1><p>The resource could not be found: {url}</p>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # blueprints
    app.register_blueprint(Driver.main, url_prefix='/api')
    app.register_blueprint(Rider.main, url_prefix='/api')

    # error handlers
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)
