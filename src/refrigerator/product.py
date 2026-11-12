from datetime import datetime


class Product:
    def __init__(self, name, category, expires_at=None):
        self.name = name
        self.category = category       # "frozen" / "chilled" / "fresh"
        self.expires_at = expires_at

    def is_expired(self):
        if self.expires_at is None:
            return False
        return datetime.now() >= self.expires_at

    def __repr__(self):
        return f"Product({self.name!r}, {self.category!r})"
