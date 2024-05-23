from src.app import ma

class CategorieSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'active')

categorie_share_schema = CategorieSchema()
categories_share_schema = CategorieSchema(many=True)