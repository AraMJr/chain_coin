from dataclasses import dataclass
from hashlib import sha256
from transaction import Transaction


@dataclass
class Block:
    id: str
    date: str
    hash: str
    transaction: Transaction


