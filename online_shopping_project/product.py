class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_final_price(self):
        return self.price

class PhysicalProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def get_final_price(self):
        shipping_cost = self.weight * 2.0  # $2 per kg shipping
        return self.price + shipping_cost

class DigitalProduct(Product):
    def __init__(self, name, price, download_link):
        super().__init__(name, price)
        self.download_link = download_link