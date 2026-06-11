"""
Polymorphism and interfaces (i.e abstract classes) are used to make code compliant with the OCP. 
Now, we can extend the functionality of our code without modifying existing base class code, thus adhering to the principle.
"""
from abc import ABC, abstractmethod

#Interface (Abstract class)
class Discount(ABC):
    @abstractmethod
    def calculate_price(self, price):
        pass

# Child classes that implement the interface.
class RegularCustomerDiscount(Discount):
    """10% discount for regular customers."""
    customer_type = "regular"
    def calculate_price(self, price):
        return price * 0.9   

class PremiumCustomerDiscount(Discount):
    """20% discount for premium customers."""
    customer_type = "premium"
    def calculate_price(self, price):
        return price * 0.8

class VIPCustomerDiscount(Discount):
    """50% discount for VIP customers."""
    customer_type = "vip"
    def calculate_price(self, price):
        return price * 0.5
# Now, if we want to add a new customer type, we can simply create a new class that implements the Discount interface without modifying existing code.
class FirstTimer_No_Discount(Discount):
    """No discount for first-time customers."""
    customer_type = "first_timer"
    def calculate_price(self, price):
        return price
    
# Orchestration function that uses the Discount interface to calculate the price.
def calculate_price(price, discount: Discount) :
    return discount.calculate_price(price)

if __name__ == "__main__":
    price = 1000

    # Orchestration: choose which discount strategy to use
    print(f"Original price: {price}")
    discount = VIPCustomerDiscount()        # or RegularCustomerDiscount(), PremiumCustomerDiscount(), NoDiscount()
    final_price = calculate_price(price, discount)
    print(f"Final price with discount for {discount.customer_type}: {final_price}")

    discount = RegularCustomerDiscount()
    print(f"Final price with discount for {discount.customer_type}: {calculate_price(price, discount)}")
    discount = PremiumCustomerDiscount()
    print(f"Final price with discount for {discount.customer_type}: {calculate_price(price, discount)}")
    discount = FirstTimer_No_Discount()
    print(f"Final price with discount for {discount.customer_type}: {calculate_price(price, discount)}")    