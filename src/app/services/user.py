from src.app.models.user import User
from src.app.models.role import Role
from src.app.models.user.schema import user_share_schema

def create_user(city_id, name, age, email, password, roles):
  try:
    if roles == None:
      roles = 'HELPER'
      
    roles_query = Role.query.filter_by(description=roles).all()

    User.seed(
      city_id=city_id,
      name=name,
      age=age,
      email=email,
      password=password,
      roles=roles_query
    )

    exist_user = get_user_by_email(email)

    if exist_user:
      return exist_user
    
    return { 'message': 'User created successfuly' }
  except:
    return { 'error': 'Something wrong creating user' }
    
def get_user_by_email(email: str):
  try: 
    user_query = User.query.filter_by(email=email).first_or_404()
    user_dict = user_share_schema(user_query)
    return { 'id': user_dict['id'], 'roles': user_dict['roles'] }
  
  except:
    return { 'error': 'User not founded', 'status_code': 500 }