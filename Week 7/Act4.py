class Transport:
    def deliver(self, cargo):
        pass

# Concrete Transport Classes
class RoadTransport(Transport):
    def deliver(self, cargo):
        print(f"Delivering '{cargo}' by TRUCK (road).")

class SeaTransport(Transport):
    def deliver(self, cargo):
        print(f"Delivering '{cargo}' by SHIP (sea).")

# Factory Pattern
class TransportFactory:
    @staticmethod
    def create_transport(mode):
        mode = mode.lower()
        if mode == "road":
            return RoadTransport()
        elif mode == "sea":
            return SeaTransport()
        else:
            raise ValueError("Invalid mode of transport. Choose 'road' or 'sea'.")

# Singleton Pattern
class LogisticsCenter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Initializing Port Logistics Center...\n")
            cls._instance = super().__new__(cls)
            cls._instance.transport_log = []
        return cls._instance

    def transport(self, mode, cargo):
        transport = TransportFactory.create_transport(mode)
        transport.deliver(cargo)
        self.transport_log.append((mode, cargo))

    def show_log(self):
        print("\nTransport Log:")
        for mode, cargo in self.transport_log:
            print(f"- {cargo} transported by {mode}")

# Main Program
if __name__ == "__main__":
    port_center = LogisticsCenter()

    port_center.transport("Road", "Electronics")
    port_center.transport("Sea", "Furniture")
    port_center.transport("Road", "Clothing")
    port_center.transport("Sea", "Automobiles")

    port_center.show_log()