from bson import ObjectId

class Order:
    def __init__(self, client_id, product_id, _id=None):
        self._id = _id or ObjectId()
        self.client_id = client_id
        self.product_id = product_id

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return {
            '_id': str(self._id),
            'client_id': str(self.client_id),
            'product_id': str(self.product_id)
        }