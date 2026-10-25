class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(f"Added to order: {product.name}")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.get_final_price()
        return total

    def checkout(self, payment_method):
        total = self.calculate_total()
        print(f"\nInitiating checkout for {self.customer.name}. Total bill: ${total:.2f}")
        
        if payment_method.process_payment(total):
            print("Checkout Successful! Order is complete.")
        else:
            print("Payment failed. Please try again.")