from dataclasses import dataclass
import encrypt
import uuid


@dataclass
class User:
    username: str
    email: str
    password: str
    uid: str
    private_keys: dict = None
    public_keys: dict = None

    def add_key_pairs(self, coin_id) -> None:
        if self.private_keys is None:
            self.private_keys = {}
        if self.public_keys is None:
            self.public_keys = {}
        private_key, public_key = encrypt.generate_key_pair()
        self.private_keys[coin_id] = private_key
        self.public_keys[coin_id] = public_key


def user_data(user: User) -> tuple[str, str, str, str, dict, dict]:
    return user.username, user.email, user.password, user.uid, user.private_keys, user.public_keys


def hydrate_user(username: str, email: str, password: str, uid: str, private_keys: dict, public_keys: dict) -> User:
    return User(username=username, email=email, password=password, uid=uid,
                private_keys=private_keys, public_keys=public_keys)


def create_user(username: str, email: str, password: str) -> User:
    return User(username=username, email=email, password=password, uid=uuid.uuid4().hex)


if __name__ == "__main__":
    user = create_user("username", "email@email.com", "password")
    print(user)
    user.add_key_pairs("test_coin")
    print(user.private_keys.get("test_coin"))
    print(user.public_keys.get("test_coin"))
    username, email, password, uid, private_keys, public_keys = user_data(user)
    print(username, email, password, uid, private_keys, public_keys)
    print(hydrate_user(username, email, password, uid, private_keys, public_keys))



