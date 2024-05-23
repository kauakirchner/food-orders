from src.app import MA
from src.app.entities.permissions.schema import permissions_share_schema

class RoleSchema(MA.Schema):
  permissions = MA.Nested(permissions_share_schema)
  class Meta:
    fields = ('id', 'description', 'permissions')

role_share_schema = RoleSchema()
roles_share_schema = RoleSchema(many=True)