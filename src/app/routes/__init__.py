from src.app.controllers.auth import auth
from src.app.controllers.user import user

def routes(app):
  app.register_blueprint(user)
  app.register_blueprint(auth)
