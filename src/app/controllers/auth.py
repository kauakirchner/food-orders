import requests
import json
from flask import Blueprint, request, current_app
from flask.wrappers import Response
from flask.globals import session
from werkzeug.utils import redirect
from google_auth_oauthlib.flow import Flow
from google import auth as google_auth
from google.oauth2 import id_token
from src.app.services.user import create_user, get_user_by_email
from src.app.services.auth import login_user
from src.app.utils import exist_key, generate_jwt


auth = Blueprint('auth', __name__, url_prefix='/auth')

flow = Flow(
  client_secrets_file='src/app/db/client_secret.json',
  scopes=[
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid"
  ],
  redirect_uri='http://localhost:5000/auth/callback'
)

@auth.route('/login', methods=['POST'])
def login():
  list_keys = ['email', 'password']

  data = exist_key(request.get_json(), list_keys)

  response = login_user(data['email'], data['password'])

  if 'error' in response:
    return Response(
      response=json.dumps({ 'error': response['error'] }),
      status=response['status_code'],
      mimetype='application/json'
    )

  return Response(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )

@auth.route('/auth/google', methods=['POST'])
def auth_google():
  authorization_url, state = flow.authorization_url()
  session['state'] = state

  return Response(
    response=json.dumps({ 'url': authorization_url }),
    status=200,
    mimetype='application/json'
  )

@auth.route('/auth/callback', methods=['GET'])
def callback():
  flow.fetch_token(authorization_response=request.url)
  credentials = flow.credentials
  google_token = google_auth.transport.requests.Request(session=requests.session())

  user_google_dict = id_token.verify_oauth2_token(
    id_token=credentials.id_token,
    request=google_token,
    audience=current_app.config['GOOGLE_CLIENT_ID']
  )

  user = get_user_by_email(
  user_google_dict['email'])

  if 'error' in user:
    user = create_user(
      50,
      user_google_dict['name'],
      25,
      user_google_dict['email'],
      "PASSWORD_DEFAULT",
      None
    )
  
  
  user_google_dict['user_id'] = user['id']
  user_google_dict['roles'] = user['roles']
  session['google_id'] = user_google_dict.get('sub')
  del user_google_dict['aud']
  del user_google_dict['azp']

  return redirect(f'{current_app.config['FRONTEND_URL']}?jwt={generate_jwt(user_google_dict)}')

@auth.route('/logout', methods=['POST'])
def logout():
  session.clear()
  return Response(
    response=json.dumps({ "message":"User has been logged out" }),
    status=202,
    mimetype='application/json'
  )