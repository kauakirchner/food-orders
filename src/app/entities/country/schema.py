from src.app import MA

class CountrySchema(MA.Schema):
  class Meta:
    fields = ('id', 'name', 'language')

country_share_schema = CountrySchema()
countries_share_schema = CountrySchema(many = True)