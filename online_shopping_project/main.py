
from product import PhysicalProduct, DigitalProduct
from payment import CardPayment, CashPayment
from order import Customer, Order

def main():

    customer = Customer("Ali", "ali@example.com")
    
    
    keyboard = PhysicalProduct("Mechanical Keyboard", 80.0, 1.5)
    course = DigitalProduct("Python Course", 45.0, "link.com/download")
    
   
    my_order = Order(customer)
    my_order.add_item(keyboard)
    my_order.add_item(course)
    
   
    my_card = CardPayment("1234567890129999")
    my_order.checkout(my_card)

if __name__ == "__main__":
    main()