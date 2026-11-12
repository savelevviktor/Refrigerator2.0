from datetime import datetime, timedelta
from refrigerator.product import Product


def test_not_expired_without_date():
    p = Product("milk", "chilled")
    assert p.is_expired() is False


def test_expired_after_date():
    past = datetime.now() - timedelta(days=1)
    p = Product("milk", "chilled", expires_at=past)
    assert p.is_expired() is True
