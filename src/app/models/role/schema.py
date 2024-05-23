from src.app import ma
from src.app.models.permissions.schema import permissions_share_schema

class RoleSchema(ma.Schema):
  permissions = ma.Nested(permissions_share_schema)
  class Meta:
    fields = ('id', 'description', 'permissions')

role_share_schema = RoleSchema()
roles_share_schema = RoleSchema(many=True)