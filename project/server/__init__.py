import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask.json import JSONEncoder
from datetime import datetime
import decimal

# instantiate the extensions
bootstrap = Bootstrap()


def create_app(script_info=None):

    # instantiate the app
    app = Flask(
        __name__,
        template_folder="../client/templates",
        static_folder="../client/static",
    )

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    
    #custom encoder
    app.json_encoder = CustomJSONEncoder

    # set up extensions
    bootstrap.init_app(app)

    # register blueprints
    from project.server.main.views import main_blueprint

    app.register_blueprint(main_blueprint)

    # shell context for flask cli
    app.shell_context_processor({"app": app})

    return app

class CustomJSONEncoder(JSONEncoder):
    """Redefine default JSON encoder."""

    def default(self, obj):
        """Default."""
        try:
            if isinstance(obj, datetime):
                DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
                return obj.strftime(DATETIME_FORMAT)
            elif isinstance(obj, decimal.Decimal):
                return str(obj)
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


def from_mongo(cursor):
    """Return a Python."""
    return json.loads(json.dumps(cursor))
