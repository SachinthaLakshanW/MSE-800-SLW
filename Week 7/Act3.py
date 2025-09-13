from abc import ABC, abstractmethod
import threading

class PaymentGateway:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    def process_payment(self, method, amount):
        payment_method = method.pay()
        print(f"Processing {amount} with {payment_method}")

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self): pass

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

class PaymentFactory:
    @staticmethod
    def create_payment(method_type):
        if method_type == "creditcard": return CreditCard()
        if method_type == "paypal": return PayPal()
        if method_type == "bank": return BankTransfer()
        if method_type == "crypto": return CryptoPayment()
        if method_type == "gpay": return GooglePay()
        raise ValueError("Unknown payment method")

if __name__ == "__main__":
    gateway = PaymentGateway()
    for m in ["creditcard", "paypal", "bank", "crypto", "gpay"]:
        method = PaymentFactory.create_payment(m)
        gateway.process_payment(method, 100)