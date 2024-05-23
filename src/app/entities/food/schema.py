from src.app import MA
from src.app.entities.category.schema import category_share_schema

class FoodSchema(MA.Schema):
  category = MA.Nested(category_share_schema)
  class Meta:
    fields = ('id', 'category_id', 'active', 'price', 'units', 'available', 'name', 'description')

food_share_schema = FoodSchema()
foods_share_schema = FoodSchema(many=True)