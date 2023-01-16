from dataclasses import dataclass
from transaction import Transaction
import encrypt


@dataclass
class Block:
    id: str
    date: str
    hash: str
    transactions: list[Transaction]


if __name__ == "__main__":
    pass


