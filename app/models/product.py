from bson import ObjectId

class Product:
    def __init__(self, company, description, _id=None):
        self._id = _id or ObjectId()
        self.company = company
        self.description = description

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return {
            '_id': str(self._id),
            'company': self.company,
            'description': self.description
        }