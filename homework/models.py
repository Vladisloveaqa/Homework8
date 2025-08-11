class Product:
    """Класс продукта"""
    def __init__(self, name: str, price: float, description: str, quantity: int):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity: int) -> bool:
        """Проверка, что товара достаточно"""
        return self.quantity >= quantity

    def buy(self, quantity: int):
        """Покупка товара"""
        if not self.check_quantity(quantity):
            raise ValueError("Недостаточно товара")
        self.quantity -= quantity

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """Класс корзины"""
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, count: int = 1):
        """Добавление товара в корзину"""
        if product in self.products:
            self.products[product] += count
        else:
            self.products[product] = count

    def remove_product(self, product: Product, count: int = None):
        """Удаление товара из корзины"""
        if product not in self.products:
            return
        if count is None or count >= self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= count

    def clear(self):
        """Очистка корзины"""
        self.products.clear()

    def get_total_price(self) -> float:
        """Сумма всех товаров"""
        return sum(p.price * qty for p, qty in self.products.items())

    def buy(self):
        """Покупка всех товаров"""
        for product, qty in self.products.items():
            product.buy(qty)
        self.clear()
