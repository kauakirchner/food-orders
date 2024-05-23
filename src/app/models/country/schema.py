from src.app import ma

class CountrySchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'language')

country_share_schema = CountrySchema()
countries_share_schema = CountrySchema(many = True)