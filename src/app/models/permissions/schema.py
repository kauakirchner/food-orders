from src.app import ma

class PermissionSchema(ma.Schema):
  class Meta: 
    fields = ('id', 'description')

permission_share_schema = PermissionSchema()
permissions_share_schema = PermissionSchema(many=True)
