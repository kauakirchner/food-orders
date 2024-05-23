from src.app import MA

class CategorieSchema(MA.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'active')

categorie_share_schema = CategorieSchema()
categories_share_schema = CategorieSchema(many=True)