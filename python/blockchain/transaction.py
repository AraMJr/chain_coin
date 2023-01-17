from dataclasses import dataclass


@dataclass
class Transaction:
    trans_id: str
    date: str
    instigator_id: str
    recipient_id: str
    amount: float
    description: str


if __name__ == "__main__":
    pass


