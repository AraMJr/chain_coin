from dataclasses import dataclass
from hashlib import sha256


@dataclass
class User:
    username: str
    email: str
    password: str
    id: str
    keys: dict = None


def generate_id() -> str | None:
    return sha256().hexdigest()


def create_user(username: str, email: str, password: str) -> User:
    return User(username=username, email=email, password=password, id=str(generate_id()))


if __name__ == "__main__":
    user = create_user("User", "email@email.com", "password")
    print(user)



