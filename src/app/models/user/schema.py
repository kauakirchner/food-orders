from src.app import ma
from src.app.models.role.schema import roles_share_schema
from src.app.models.city.schema import city_share_schema

class UserSchema(ma.Schema):
  city = ma.Nested(city_share_schema)
  roles = ma.Nested(roles_share_schema)
  class Meta:
    fields = ('id', 'city_id', 'name', 'age', 'email', 'password', 'city', 'roles')

user_share_schema = UserSchema()
users_share_schema = UserSchema(many=True)