from enum import Enum, auto


class OrderStatus(Enum):
    PENDING = auto()
    PROCESSING = auto()
    PROCESSED = auto()


os = OrderStatus(12)

print(OrderStatus.PENDING)
print(os.PENDING)