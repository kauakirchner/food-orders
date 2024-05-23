from src.app import MA
from src.app.entities.role.schema import roles_share_schema
from src.app.entities.city.schema import city_share_schema

class UserSchema(MA.Schema):
  city = MA.Nested(city_share_schema)
  roles = MA.Nested(roles_share_schema)
  class Meta:
    fields = ('id', 'city_id', 'name', 'age', 'email', 'password', 'city', 'roles')

user_share_schema = UserSchema()
users_share_schema = UserSchema(many=True)