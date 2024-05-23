from src.app import MA

class FoodSchema(MA.Schema):
  class Meta:
    fields = ('id', 'active', 'price', 'units', 'available', 'name', 'description', 'category_id')

food_share_schema = FoodSchema()
foods_share_schema = FoodSchema(many=True)