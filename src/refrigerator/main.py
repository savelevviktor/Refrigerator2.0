from .product import Product
from .refrigerator import Refrigerator


def main():
    fridge = Refrigerator()

    fridge.open()
    fridge.put(Product("milk", "chilled"))
    fridge.put(Product("meat", "frozen"))
    fridge.close()

    for _ in range(3):
        fridge.cool()

    fridge.open()
    milk = fridge.take("milk")
    fridge.close()

    print(f"Достали: {milk.name}")


if __name__ == "__main__":
    main()
