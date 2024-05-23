from src.app import MA

class PermissionSchema(MA.Schema):
  class Meta: 
    fields = ('id', 'description')

permission_share_schema = PermissionSchema()
permissions_share_schema = PermissionSchema(many=True)
