class PaymentMethod:
    def process_payment(self, amount):
        pass

class CardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        print(f"Processing payment of ${amount:.2f} with card ending in {self.card_number[-4:]}...")
        return True

class CashPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Customer will pay ${amount:.2f} via Cash on Delivery.")
        return True