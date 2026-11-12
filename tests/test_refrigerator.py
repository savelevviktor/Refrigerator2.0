import pytest
from refrigerator.refrigerator import Refrigerator
from refrigerator.product import Product


def test_put_and_take():
    fridge = Refrigerator()
    fridge.open()
    fridge.put(Product("milk", "chilled"))
    fridge.close()

    fridge.open()
    milk = fridge.take("milk")
    fridge.close()

    assert milk.name == "milk"


def test_door_must_be_open_to_put():
    fridge = Refrigerator()
    with pytest.raises(RuntimeError):
        fridge.put(Product("milk", "chilled"))


def test_overflow():
    fridge = Refrigerator()
    fridge.open()
    for i in range(20):
        fridge.put(Product(f"item{i}", "chilled"))
    with pytest.raises(OverflowError):
        fridge.put(Product("extra", "chilled"))
