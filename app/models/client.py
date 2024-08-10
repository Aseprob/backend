from bson import ObjectId

class Client:
    def __init__(self, email, notes=None, _id=None):
        self._id = _id or ObjectId()
        self.email = email
        self.notes = notes

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return {
            '_id': str(self._id),
            'email': self.email,
            'notes': self.notes
        }