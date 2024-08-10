"""
Model that represents a product on the db
"""
from bson import ObjectId


class Product:
    """
    Model for product, should use @dataclass.
    """
    def __init__(self, company, description, _id=None):
        self._id = _id or ObjectId()
        self.company = company
        self.description = description

    @classmethod
    def from_dict(cls, data):
        """
        deserializes
        """
        return cls(**data)

    def to_dict(self):
        """
        serializes
        """
        return {
            '_id': str(self._id),
            'company': self.company,
            'description': self.description
        }
