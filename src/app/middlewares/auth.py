from functools import wraps
from jwt import decode
from flask import request, jsonify, current_app
from src.app.models.user import User

def requires_access_level(permission):
  def jwt_required(current_function):
    @wraps(current_function)
    def wrapper(*args, **kwargs):

      if not 'Authorization' in request.headers:
        return jsonify({ 'error': "UNAUTHORIZED" }), 403

      token = request.headers['Authorization']
      
      if not 'Bearer' in token:
        return jsonify({ 'error': 'UNAUTHORIZED' }), 401
      
      try:
        token_pure = token.replace('Bearer', '')
        decoded_token = decode(token_pure, current_app.config['SECRET_KEY'], 'HS256')
        current_user = User.query.get(decoded_token['user_id'])
      except:
        return jsonify({ 'error': 'INVALID TOKEN' }), 403
      
      founded_permission = 0
      for role in current_user.roles:
        for permission_in_roles in role.permissions:
          if permission_in_roles.description == permission:
            founded_permission += 1

      if founded_permission == 0:
        return jsonify({ 'error': "USER UNAUTHORIZED"}), 403
      
      return current_function(current_user=current_user, *args, **kwargs)
    return wrapper
  return jwt_required