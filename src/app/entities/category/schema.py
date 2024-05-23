from src.app import MA

class CategorySchema(MA.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'active')

category_share_schema = CategorySchema()
categories_share_schema = CategorySchema(many=True)