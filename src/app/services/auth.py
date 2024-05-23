from datetime import datetime, timedelta
from src.app.utils import generate_jwt
from src.app.entities.user import User
from src.app.entities.user.schema import user_share_schema

def login_user(email, password):
  try:
    user_query = User.query.filter_by(email=email).first_or_404()
    user_dict = user_share_schema.dump(user_query)

    if not user_query.check_password(password):
      return { 'error': 'Your credentials are incorrect', 'status_code': 401 }
    
    payload = {
      'user_id': user_query.id,
      'exp': datetime.now() + timedelta(days=1),
      'roles': user_dict['roles']
    }

    return { 'access_token': generate_jwt(payload) }
  except:
    return { 'error': 'Something wrong', 'status_code': 500 }
