from flask import Flask
from flask_assets import Bundle, Environment


class Webapp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'aslkdfjkvcxkzsdaflk asdlkfewqfds f asdfasdf'

        from .views import views
        self.app.register_blueprint(views, url_prefix = '/')

        self.css = Bundle(
            'style.scss',
            output = 'gen/style.css',
            filters = 'pyscss'
        )

        self.assets = Environment(self.app)

        self.assets.register('main_css', self.css)

