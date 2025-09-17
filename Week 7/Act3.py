from abc import ABC, abstractmethod
import threading
import time

start_time = time.time()

# Singleton Payment Gateway
class PaymentGateway:
    _instance = None
    _lock = threading.Lock()  # Thread-safe singleton

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def process_payment(self, method, amount):
        print(f"Processing ${amount} with {method.pay()}")

# Abstract Payment Method
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self):
        pass

# Concrete Payment Methods
class CreditCard(PaymentMethod):
    def pay(self): return "Credit Card"

class PayPal(PaymentMethod):
    def pay(self): return "PayPal"

class BankTransfer(PaymentMethod):
    def pay(self): return "Bank Transfer"

class CryptoPayment(PaymentMethod):
    def pay(self): return "Crypto Payment"

class GooglePay(PaymentMethod):
    def pay(self): return "Google Pay"

# Factory for Payment Methods
class PaymentFactory:
    @staticmethod
    def create_payment(method_type):
        if method_type == "creditcard": return CreditCard()
        elif method_type == "paypal": return PayPal()
        elif method_type == "bank": return BankTransfer()
        elif method_type == "crypto": return CryptoPayment()
        elif method_type == "gpay": return GooglePay()
        else: raise ValueError("Unknown payment method")

# Main Program
if __name__ == "__main__":
    gateway = PaymentGateway()  # Singleton instance

    # Example payments with different methods and amounts
    payments = [
        ("creditcard", 250),
        ("paypal", 150),
        ("bank", 500),
        ("crypto", 1000),
        ("gpay", 75)
    ]

    for method_type, amount in payments:
        method = PaymentFactory.create_payment(method_type)
        gateway.process_payment(method, amount)

end_time = time.time()
print(f"Execution time: {end_time - start_time:.6f} seconds")
