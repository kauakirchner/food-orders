from src.app.controllers.user import user
from src.app.controllers.auth import auth

def routes(app):
  app.register_blueprint(user)
  app.register_blueprint(auth)
