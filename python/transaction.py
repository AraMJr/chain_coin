from dataclasses import dataclass


@dataclass
class Transaction:
    trans_id: str
    date: str
    instigator_id: str
    recpricator_id: str
    amount: float
    description: str
    


