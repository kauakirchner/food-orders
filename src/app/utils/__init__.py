from flask import current_app
from jwt import encode

def generate_jwt(payload):
  return encode(payload, current_app.config["SECRET_KEY"], "HS256")
  
def exist_key(request_json, list_keys):
  keys_not_have_in_request = []
  for key in list_keys:
    if not key in request_json:
      keys_not_have_in_request.append(key)
  
  if len(keys_not_have_in_request) == 0:
    return request_json
  
  return { 'error': f'Está faltando o item {keys_not_have_in_request}'}