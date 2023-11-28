import requests

class ProductConsumer(object):
    def __init__(self, base_uri):
        self.base_uri = base_uri

    def get_product(self, id):
        """Get product by ID"""
        uri = self.base_uri + '/product/' + id
        response = requests.get(uri)
        if response.status_code == 404:
            return None

        json = response.json()
        return Product(json['id'], json['type'], json['name'], json['updated_by'], json['new_required_field'])


class Product(object):
    def __init__(self, id, type, name, updated_by, new_required_field):
        self.id = id
        self.type = type
        self.name = name
        self.updated_by = updated_by
        self.new_required_filed = new_required_field
