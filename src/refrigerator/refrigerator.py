class Refrigerator:
    def __init__(self):
        self.items = []
        self.temperature = 4
        self.is_open = False
        self.capacity = 20

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def put(self, product):
        if not self.is_open:
            raise RuntimeError("Дверь закрыта")
        if len(self.items) >= self.capacity:
            raise OverflowError("Холодильник переполнен")
        self.items.append(product)
        print(f"[put] {product.name}")

    def take(self, name):
        if not self.is_open:
            raise RuntimeError("Дверь закрыта")
        for i in range(len(self.items)):
            if self.items[i].name == name:
                return self.items.pop(i)
        raise KeyError(f"Продукт '{name}' не найден")

    def cool(self):
        self.temperature -= 1
        print(f"[temp] {self.temperature}°C")
