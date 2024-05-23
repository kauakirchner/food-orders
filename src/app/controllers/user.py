import json
from flask import Blueprint, request
from flask.wrappers import Response
from src.app.services.user import create_user
from src.app.middlewares.auth import requires_access_level
from src.app.utils import exist_key

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/create', methods=['POST'])
@requires_access_level('WRITE')
def create():
  list_keys = ['city_id', 'name', 'age', 'email', 'password']
  data = exist_key(request.get_json(), list_keys)

  if 'error' in data:
    return Response(
      response=json.dumps(data),
      status=400,
      mimetype='application/json'
    )

  roles = None
  if 'roles' in data:
    roles = data['roles']

  response = create_user(
    data['city_id'],
    data['name'],
    data['age'],
    data['email'],
    data['password'],
    roles
  )

  if 'error' in response:
    return Response(
      response=json.dumps(response),
      status=400,
      mimetype='application/json'
    )
  
  return Response(
    response=json.dumps(response),
    status=201,
    mimetype='application/json'
  )