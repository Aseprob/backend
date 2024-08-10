"""
Model that represents a client on the db
"""
from bson import ObjectId


class Client:
    """
    Model for client, should use @dataclass.
    """
    def __init__(self, email, notes=None, _id=None):
        self._id = _id or ObjectId()
        self.email = email
        self.notes = notes

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
            'email': self.email,
            'notes': self.notes
        }
